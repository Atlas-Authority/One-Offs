/*This can also use json_agg but that doesn't work with large result sets for some reason. Same goes for running this on the command line with psql having a direct file to output to */
SELECT
DISTINCT CONCAT(p.pkey, '-', ji.issuenum)
FROM
jiraissue ji
JOIN project p ON ji.project = p.id
JOIN customfieldvalue cfv ON ji.id = cfv.issue
JOIN customfield cf ON cfv.customfield = cf.id
WHERE
cf.cfname IN ('Time to first response', 'Time to resolution')
AND cfv.textvalue LIKE '%"timeline%ongoingSLAData":null,"completeSLAData":[]%';

