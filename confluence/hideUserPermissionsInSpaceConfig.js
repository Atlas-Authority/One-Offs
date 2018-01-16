// Super hacky but it helps prevent individual users from getting space permissions
AJS.$("#uPermissionsTable").next().hide() 
AJS.$("#uPermissionsTable").prev().prev().prev().hide() 
AJS.$("#uPermissionsTable").prev().prev().hide() 
AJS.$("#uPermissionsTable").prev().hide() AJS.$("#uPermissionsTable").hide()