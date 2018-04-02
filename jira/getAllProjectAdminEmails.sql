# It's not 100% but it gets pretty damn close,

SELECT projectkey, string_agg(distinct(emails),',') from (
--Project Leads

select p.PKEY as projectkey, u.lower_email_address as emails
from project p
JOIN app_user au ON au.lower_user_name = p.lead
JOIN cwd_user u ON u.lower_user_name = au.user_key

UNION

--Users in roles
SELECT p.pkey as projectkey, u.lower_email_address as emails
FROM projectroleactor pra
INNER JOIN projectrole pr ON pr.ID = pra.PROJECTROLEID
INNER JOIN project p ON p.ID = pra.PID
INNER JOIN app_user au ON au.lower_user_name = pra.ROLETYPEPARAMETER
INNER JOIN cwd_user u ON u.lower_user_name = au.user_key
WHERE pr.NAME = 'Administrators'
AND pra.roletype = 'atlassian-user-role-actor'

UNION

--Groups in roles
SELECT p.pkey as projectkey, u.lower_email_address as emails
from projectroleactor pra
INNER JOIN projectrole pr ON pr.ID = pra.PROJECTROLEID
INNER JOIN project p ON p.ID = pra.PID
INNER JOIN cwd_membership cmem ON cmem.parent_name = pra.roletypeparameter
INNER JOIN app_user au ON au.lower_user_name = cmem.lower_child_name
INNER JOIN cwd_user u ON u.lower_user_name = au.user_key
where pra.roletype = 'atlassian-group-role-actor'
AND pr.NAME = 'Administrators'

UNION

--Direct users in permission schemes
select p.pkey as projectkey, u.lower_email_address as emails
from project p
JOIN nodeassociation na ON p.id = na.source_node_id
JOIN schemepermissions sp ON na.sink_node_id = sp.scheme
JOIN app_user au ON au.lower_user_name = sp.perm_parameter
JOIN cwd_user u ON u.lower_user_name = au.user_key
WHERE na.sink_node_entity='PermissionScheme'
AND sp.perm_type = 'user'
AND sp.permission_key = 'ADMINISTER_PROJECTS'

UNION

--Direct groups in permission schemes

select p.pkey as projectkey, u.lower_email_address as emails
from project p
JOIN nodeassociation na ON p.id = na.source_node_id
JOIN schemepermissions sp ON na.sink_node_id = sp.scheme
JOIN cwd_membership cmem ON cmem.parent_name = sp.perm_parameter
JOIN app_user au ON au.lower_user_name = cmem.lower_child_name
JOIN cwd_user u ON u.lower_user_name = au.user_key
WHERE na.sink_node_entity='PermissionScheme'
AND sp.perm_type = 'group'
AND sp.permission_key = 'ADMINISTER_PROJECTS') as errything

group by projectkey