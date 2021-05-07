#
# Add a user to a bulk set of permission schemes
# Example below is adding the user to MANAGE_WATCHER permisison
#

for i in "XXXXX" "XXXXX" "XXXXX"; 

do curl {flags: however you authenticate} -X POST "https://example.com" \  
--header 'Accept: application/json' \  
--header 'Content-Type: application/json' \  
--data '{  
"holder": {    
    "parameter": "username",    
    "type": "user"  
}, 
  "permission": "MANAGE_WATCHERS"
}'
;done
