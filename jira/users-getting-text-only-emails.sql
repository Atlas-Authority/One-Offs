select
  au.lower_user_name
  ,ps.propertyvalue
from cwd_user u, app_user au
join propertyentry pe
  on au.id = pe.entity_id
  and pe.entity_name = 'ApplicationUser'
  and pe.property_key = 'user.notifications.mimetype'
join propertystring ps
  on pe.id = ps.id
where
u.lower_user_name = au.lower_user_name
AND u.active = 1
AND ps.propertyvalue = 'text';
