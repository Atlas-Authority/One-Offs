-- Written for PostgreSQL but should work anywhere
-- https://confluence.atlassian.com/jirakb/jira-get-list-of-all-filters-shared-with-everyone-808486334.html
SELECT sr.filtername, sp.sharetype AS current_share_state, sr.username AS owner_name, sr.reqcontent AS JQL
FROM searchrequest sr
INNER JOIN sharepermissions sp ON sp.entityid = sr.id 
WHERE sp.sharetype='global' and sp.entitytype ='SearchRequest';