import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.permission.ProjectPermissions
import com.atlassian.jira.security.plugin.ProjectPermissionKey
import com.atlassian.jira.scheme.SchemeEntity
import org.ofbiz.core.entity.GenericValue;

def permissionSchemeManager = ComponentAccessor.permissionSchemeManager
def projectManager = ComponentAccessor.projectManager

// Add jira-auditors group to Browse Projects permission in all permission schemes
// Matt Doar

// See ProjectPermissions for the other permissions
permission_name = ProjectPermissions.BROWSE_PROJECTS
    
// Make sure the group exists before using this script
group_name = "jira-auditors"
    
def schemes = permissionSchemeManager.getSchemeObjects()
for (scheme in schemes) {
    
    entries = permissionSchemeManager.getPermissionSchemeEntries(scheme, permission_name)
    if (entries != null && entries.size() > 0) {
	found = false
        for (entry in entries) {
            if (entry.type == "group" && entry.parameter == group_name) {
                found = true
            }
        }
        if (found) {
	    // The group all ready has the permission, no change is needed
	    continue
        }
    }
    
    try {
        def dryrun = true;
        if (dryrun) {
            log.warn("(DRYRUN) Adding the " + permission_name + " permission for the group: " + group_name + "\n");
        } else {
            log.warn("Adding the " + permission_name + " permission for the group: " + group_name + "\n");
            SchemeEntity schemeEntity = new SchemeEntity("group", group_name, permission_name);
            GenericValue schemeAsGenericValue = permissionSchemeManager.getScheme(scheme.id);
            permissionSchemeManager.createSchemeEntity(schemeAsGenericValue, schemeEntity);
        }
    } catch (Exception e) {
        log.error("Error updating scheme: " + scheme.name +" and permission " + permission_name + " " + e  + "\n");
    }
}
