import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.issue.CustomFieldManager
import com.atlassian.jira.issue.fields.CustomField

CustomFieldManager customFieldManager = ComponentAccessor.getCustomFieldManager();
//Collection<CustomField> customFields = customFieldManager.getCustomFieldObjects(); //get ALL customFields
Collection<CustomField> customFields_to_be_deleted = []

Fields_to_be_deleted().each{fieldName -> 
customFields_to_be_deleted.add(customFieldManager.getCustomFieldObjects().find {it.name == fieldName})
    }
//debug
//return customFields_to_be_deleted
for (CustomField field: customFields_to_be_deleted) {
	if(field){ //checking if field is exist
    	customFieldManager.removeCustomField(field);
        }
}

List<String> Fields_to_be_deleted(){
    return [
        "Field Name 1",
		"Another field name",
        "No one expected a third"
    ]
}
