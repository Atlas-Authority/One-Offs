/*
Title: Add Assignee to Watcher List
Author - Mike Schultz - mschultz@zenefits.com
Date Created: July 11, 2019
Date Last Updated: N/A
Description: Add Issue Assignee to the Issue's Watchers list upon issue assignment.
*/


import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.event.issue.AbstractIssueEventListener
import com.atlassian.jira.event.issue.IssueEvent
import com.atlassian.jira.issue.Issue
import org.apache.log4j.Logger
import com.atlassian.jira.ComponentManager
import static org.apache.log4j.Level.DEBUG
import com.atlassian.jira.issue.Issue
import com.atlassian.jira.user.ApplicationUser
import com.atlassian.jira.issue.watchers.WatcherManager

def watcherManager = ComponentAccessor.getWatcherManager()
def userManager = ComponentAccessor.getUserManager()
Issue issue = event.getIssue()
log.setLevel(DEBUG)
log.debug "Event: ${event.getEventTypeId()} fired for ${issue} and caught by TaskVersionListener"
def assignee = issue.assigneeId
ApplicationUser assigneeWatcher = issue.assignee
log.debug "assigneeWatcher: " + assigneeWatcher
watcherManager.startWatching(assigneeWatcher, issue)
