/*
Please be aware that these scripts are not officially supported by Atlassian Support. They utilize internal unpublished APIs which have more restricted rate limiting rules and could change at any time. They're are best used in batches of smaller lists of users.

You can also run this as an org admin from the browser console using this script. However, this is based on the Atlassian account ID's not the email addresses. You can get the user AAIDs by exporting managed accounts. https://support.atlassian.com/organization-administration/docs/export-managed-accounts/

Provide the AAIDs, on line 3.
Provide the Org ID, on line 4.
Access the Org admin, on admin.atlassian.com.  You need to be added as an org admin.
Open the browser console (On Chrome, you can press command + option + I).
Paste the updated script.
Hit enter.


*/


//Insert the AAIDs on line 3, between double quotes.
//Inser the Org ID on line 4, between double quotes.
var users = ["<aaid>","<aaid>",...];
var Org_ID = "<ORG-ID>";

function bulkDeactivate (users, size, Org_ID){
    var users_array = users;
    var user_size = size;
    var OrgID = Org_ID;
    if (user_size > 0){
        fetch("https://admin.atlassian.com/gateway/api/users/"+users[size-1]+"/deactivate", {
            "headers": {
                "accept": "*/*",
                "content-type": "application/json",
            },
            "referrer": "https://admin.atlassian.com/o/"+Org_ID+"/members/users[size-1]",
            "body": null,
            "method": "POST",
            "credentials": "include"
        }).then(function(response){
            console.log("User: "+users[size-1]+" Status: "+response.status+". Remaining "+(size-1)+" user(s).");
            bulkDeactivate(users_array,user_size-1, OrgID);
        });
    }
}

bulkDeactivate (users, users.length, Org_ID);
