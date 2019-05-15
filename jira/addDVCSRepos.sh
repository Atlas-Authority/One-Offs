// This works for Bitbucket and GitHub, but has not been tested with GitHub Enterprise.

// Get your repo list 
curl --request GET \
  --url http://<BASE URL>/rest/bitbucket/1.0/repositories \
  --header 'accept: application/json' \
  --header 'authorization: Basic <AUTH INFO>' 

// Add the repo to Jira to sync
curl --request POST \
  --url http://<BASEURL>/rest/bitbucket/1.0/repo/<REPO ID FROM PREVIOUS STEP>/autolink \
  --header 'authorization: Basic <AUTH INFO>' \
  --header 'content-type: application/json' \
  --data '{"payload": true}'
