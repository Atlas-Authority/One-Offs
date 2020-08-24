select
  au.lower_user_name
  ,ps.propertyvalue
from app_user au
join propertyentry pe
  on au.id = pe.entity_id
  and pe.entity_name = 'ApplicationUser'
  and pe.property_key = 'user.notifications.mimetype'
join propertystring ps
  on pe.id = ps.id
where ps.propertyvalue = 'text';
