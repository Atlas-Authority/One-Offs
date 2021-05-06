/*
Title: Add Assignee to Watcher List
Author - Mike Schultz - mike@atlasauthority.com
Date Created: July 11, 2019
Date Last Updated: N/A
Description: Add Issue Assignee to the Issue's Watchers list upon issue assignment.
*/

// Trigger event is IssueAssigned
import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.issue.Issue
import com.atlassian.jira.user.ApplicationUser
import com.atlassian.jira.issue.watchers.WatcherManager

Issue issue = event.getIssue()
ApplicationUser assignee = issue.assignee
def watcherManager = ComponentAccessor.getWatcherManager()
def userManager = ComponentAccessor.getUserManager()

watcherManager.startWatching(assignee, issue)
