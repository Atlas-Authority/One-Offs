DECLARE @date date = '2018-01-01'; 

-- Customfield Changes
(select distinct(project.pkey) from  jiraissue
join changegroup on jiraissue.ID = changegroup.issueid
join changeitem on changegroup.id = changeitem.groupid
join project on jiraissue.PROJECT = project.ID
where 
jiraissue.CREATED > @date
OR jiraissue.UPDATED > @date)

UNION

-- new issues
(select distinct(project.pkey) from jiraissue
join project on jiraissue.PROJECT = project.ID
where jiraissue.CREATED > @date
or jiraissue.UPDATED > @date)

UNION


-- comments since
(select distinct(project.pkey) from jiraaction
join jiraissue on jiraaction.issueid = jiraissue.id
join project on jiraissue.PROJECT = project.ID
WHERE jiraaction.CREATED > @date
OR jiraaction.UPDATED > @date)
