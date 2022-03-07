const fetch = require('node-fetch');

let baseUrl = 'https://example.atlassian.net/wiki/rest/api/space?expand=permissions';
let username = 'username';
let password = 'make sure to use an API key not a password';
let url = 'https://atlasauthority.atlassian.net/wiki/rest/api/space?expand=permissions';


let start = 0;


function recurssionAlwaysEndsBadly(){
  fetch(url, {
    method: 'GET',
    headers: {
      'Authorization': 'Basic ' + Buffer.from(username + ":" + password).toString('base64'),
      'Accept': 'application/json'
    }
  })
    .then(response => {
      //console.log(
      //  `Response: ${response.status} ${response.statusText}`
      //);
      return response.json();
    })
    .then(response => {
      const results = response.results;

      

      for (r in results){

        let result = results[r]

        let permissions = result.permissions

        for (p in permissions){

          let permission = permissions[p]

          if (permission.operation.operation == 'administer' && permission.operation.targetType == 'space' && permission.subjects.user){

              console.log(result.key + "," + result.name + "," + result.status + "," + result.type + "," + permission.subjects.user.results[0].displayName + ',' + permission.subjects.user.results[0].accountType)
            
          }
        }

      }
      
      if (response.size > 0) {
        start = start + 25;
        url = baseUrl + '&start=' + start;
        recurssionAlwaysEndsBadly();
      } else {
        process.exit()
      }
    })
    .catch(err => console.error(err));

}

console.log("space_key,space_name,space_status,space_type,admin_display_name,user_type")
recurssionAlwaysEndsBadly();
