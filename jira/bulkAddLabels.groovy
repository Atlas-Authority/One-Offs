/*
Bulk add labels to existing issues via JQL query
Last tested on Jira 8.13.3
*/

import com.atlassian.jira.component.ComponentAccessor

import com.atlassian.jira.issue.label.LabelManager

import com.atlassian.jira.jql.parser.JqlQueryParser

import com.atlassian.jira.bc.issue.search.SearchService

import com.atlassian.jira.web.bean.PagerFilter

import com.atlassian.jira.user.util.UserManager

import com.atlassian.jira.issue.MutableIssue

import com.atlassian.jira.issue.index.IssueIndexingService;

import com.atlassian.jira.util.ImportUtils;
 

def jqlQueryParser = ComponentAccessor.getComponent(JqlQueryParser)

def userManager = ComponentAccessor.getUserManager()


def user = userManager.getUserByKey("String Username here")

String issueKey


// change to 'false' if you don't want to send a notification for that change

final boolean sendNotification = true


// have this true in order to throw an issue update event, and reindex the index

final boolean causesChangeNotification = false

 

// a list with the labels we want to add to the issue

final List<String> newLabels = ["String label name here"]


def issueManager = ComponentAccessor.issueManager

def labelManager = ComponentAccessor.getComponent(LabelManager)

// the issue key of the issue to update its labels

def query = jqlQueryParser.parseQuery("String JQL query here")

def searchService = ComponentAccessor.getComponent(SearchService.class)


def results = searchService.search(user, query, PagerFilter.getUnlimitedFilter())


results.getResults().each { documentIssue ->;

   

    def timestamp = documentIssue.getUpdated().toTimestamp()

    issueKey = documentIssue.key

    def issue = issueManager.getIssueByCurrentKey(issueKey)

    assert issue : "Could not find issue with key $issueKey"


    def loggedInUser = ComponentAccessor.jiraAuthenticationContext.loggedInUser

    def existingLabels = labelManager.getLabels(issue.id)*.label


    def labelsToSet = (existingLabels + newLabels).toSet()
  

    // Append the new labels to the list of existing labels

    labelManager.setLabels(loggedInUser, issue.id, labelsToSet, sendNotification, causesChangeNotification)
   

    MutableIssue mutableIssue = issueManager.getIssueObject(issue.id) as MutableIssue


  /*
   Optional 
   This will set the Updated Date field value back to what it was before this script ran.
  */

    mutableIssue.setUpdated(timestamp);

    mutableIssue.store()
 

    //Re-index the issue.

    boolean isIndex = ImportUtils.isIndexIssues();

    ImportUtils.setIndexIssues(true);

    IssueIndexingService IssueIndexingService = (IssueIndexingService) ComponentAccessor.getComponent(IssueIndexingService.class);

    IssueIndexingService.reIndex(mutableIssue);

 
    ImportUtils.setIndexIssues(isIndex);

}
