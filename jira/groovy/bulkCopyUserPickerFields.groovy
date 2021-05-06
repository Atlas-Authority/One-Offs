/*

Copy source field to destination field in Bulk

Last tested on Jira 8.13.3

*/ 

import com.atlassian.jira.component.ComponentAccessor

import com.atlassian.jira.event.type.EventDispatchOption

import com.atlassian.jira.issue.CustomFieldManager

import com.atlassian.jira.user.ApplicationUser

import com.atlassian.jira.issue.fields.CustomField

import com.atlassian.jira.issue.MutableIssue

import com.atlassian.jira.user.ApplicationUser

import com.atlassian.jira.user.util.UserManager

import com.atlassian.jira.web.bean.PagerFilter

import com.atlassian.jira.bc.issue.search.SearchService

import com.atlassian.jira.jql.parser.JqlQueryParser

import com.atlassian.jira.issue.search.SearchProvider

import com.atlassian.jira.issue.UpdateIssueRequest

import com.atlassian.jira.issue.Issue

import com.atlassian.jira.util.ImportUtils;

import com.atlassian.jira.issue.index.IssueIndexingService;


def jqlQueryParser = ComponentAccessor.getComponent(JqlQueryParser)

def searchProvider = ComponentAccessor.getComponent(SearchProvider)

def issueManager = ComponentAccessor.getIssueManager()

def userManager = ComponentAccessor.getUserManager()

def user = userManager.getUserByKey("Acting Username")

def issue

def customFieldManager = ComponentAccessor.getCustomFieldManager()

def searchService = ComponentAccessor.getComponent(SearchService.class)


CustomField UserPickerField1 = ComponentAccessor.getCustomFieldManager().getCustomFieldObject("customfield_XXXXX")

CustomField UserPickerField2 = ComponentAccessor.getCustomFieldManager().getCustomFieldObject("customfield_XXXXX")


/*

 Include the syntax " 'UserPickerField1' is not EMPTY " here.

 We don't care about querying on issues with no value in the source field.

*/


//def query = jqlQueryParser.parseQuery("String JQL - Issue to act on")

def query = jqlQueryParser.parseQuery("String JQL query")


def results = searchService.search(user, query, PagerFilter.getUnlimitedFilter())

log.warn("Total issues: ${results.total}")

 

results.getResults().each { singleIssue ->;

 
    // Grabing existing Update Date timestamp for later user below.

    def timestamp = singleIssue.getUpdated().toTimestamp()


    // Start Action

    List<ApplicationUser> users
    

    // Create a list based on existing users in destination field.

    users = UserPickerField2.getValue(singleIssue)

    log.warn("Initial Field value for ${singleIssue.key}: ${users}")


    // If destination field is empty, create an empty list for adding source field values into.

    if(users == null) {

        users = new ArrayList();

    }
  

    // Add existing source field users to list of new users

    UserPickerField1.getValue(singleIssue).each { fv ->

        users.add(ComponentAccessor.getUserManager().getUserByName(fv.getName().toString()))

    }


    log.warn("New field value for ${singleIssue.key}: ${users}")


    // Make issue mutable for updates.

    MutableIssue mutableIssue = issueManager.getIssueObject(singleIssue.id) as MutableIssue


    // Update push new values into destination field.

    mutableIssue.setCustomFieldValue(UserPickerField2, users);

    UpdateIssueRequest updateIssueRequest = UpdateIssueRequest.builder().eventDispatchOption(EventDispatchOption.DO_NOT_DISPATCH).sendMail(false).build()

    issueManager.updateIssue(user,

            mutableIssue,

            updateIssueRequest)     


    users = null

    users = new ArrayList();


    // Set updated date field back to what it was before we performed the actions. Optional

    mutableIssue.setUpdated(timestamp);


    // This is needed to apply changes to system date fields

    mutableIssue.store()
  

    // Re-index issue

    boolean isIndex = ImportUtils.isIndexIssues();

    ImportUtils.setIndexIssues(true);

    IssueIndexingService IssueIndexingService = (IssueIndexingService) ComponentAccessor.getComponent(IssueIndexingService.class);

    IssueIndexingService.reIndex(mutableIssue);


    ImportUtils.setIndexIssues(isIndex);
 
}
