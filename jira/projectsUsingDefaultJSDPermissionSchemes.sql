SELECT p.pname  AS ProjectName,
       p.lead   AS ProjectLead,
       p.pkey   AS ProjectKey,
       ps.name  AS PermissionScheme
FROM   project p JOIN nodeassociation na ON p.id = na.source_node_id
                 JOIN permissionscheme ps ON ps.id=na.sink_node_id
AND sink_node_entity = 'PermissionScheme'
AND ps.name like 'JIRA Service Desk Permission Scheme for%'
order by PermissionScheme asc;
