/*
 Fills the sprint field on issue create, when the Issue Type matches what we want.
 Last tested on Jira 7.12.3
*/

import com.atlassian.greenhopper.service.sprint.Sprint
import com.atlassian.greenhopper.service.sprint.SprintManager
import com.onresolve.scriptrunner.runner.customisers.PluginModuleCompilationCustomiser
import com.onresolve.scriptrunner.runner.customisers.WithPlugin
import com.atlassian.jira.issue.MutableIssue


import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.event.type.EventDispatchOption

def customFieldManager = ComponentAccessor.getCustomFieldManager()
def issueManager = ComponentAccessor.getIssueManager()
def user = ComponentAccessor.getJiraAuthenticationContext().getLoggedInUser()
def cf = customFieldManager.getCustomFieldObjectByName("Sprint")

// Board id
final Long id = 592

def issue = event.issue as MutableIssue
def cfVal = cf.getValue(issue)

@WithPlugin("com.pyxis.greenhopper.jira")
def sprintServiceOutcome = PluginModuleCompilationCustomiser.getGreenHopperBean(SprintManager).getAllSprints()


if (issue.getIssueType().getName() == 'Issue Type Name')
    if (sprintServiceOutcome.valid) {
        
        // Get the current active sprint for the board Id specified above.
        def Sprint_name = sprintServiceOutcome.getValue()?.findAll { it.rapidViewId == id }?.findAll { it.state == Sprint.State.ACTIVE }?.each { return it.name.toString() }
        
        // Set the Sprint field
        issue.setCustomFieldValue(cf, Sprint_name)
        
        // Update the issue and do not send a notification about it
        issueManager.updateIssue(user, issue, EventDispatchOption.DO_NOT_DISPATCH, false) }

    else {
        log.info "Invalid sprint service outcome, ${sprintServiceOutcome.errors}"
    }
else
    log.info 'The issue type does not match. No action taken on issue'

