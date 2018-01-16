var request = require('sync-request');

var username = "admin@example.com",
    password = "sphere",
    url = "http://localhost:8080/rest/api/2/project",
    auth = "Basic " + new Buffer(username + ":" + password).toString("base64"),
    projectToKeep = 'KEY';

var res = request('GET', url, {
	  'headers': {
		      "Authorization" : auth
		    }
});

var d = JSON.parse(res.body.toString('utf-8'));
var k = [];
for (var i in d) {
	if (d[i].key !== projectToKeep){
		k.push(d[i].key);
	}	
}
for (var c in k){
	deleteProject(k[c]);
}

function deleteProject(key){
	console.log("deleting " + key);
	var durl = url + "/" + key,
	drequest = require('sync-request');
	var dres = request('DELETE', durl, {
	  'headers': {
		      "Authorization" : auth
		    }
	});	
	console.log(dres.body.toString('utf-8'));
}
