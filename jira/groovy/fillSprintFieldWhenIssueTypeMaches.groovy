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

final Long id = 592
def issue = event.issue as MutableIssue
def cfVal = cf.getValue(issue)

@WithPlugin("com.pyxis.greenhopper.jira")
def sprintServiceOutcome = PluginModuleCompilationCustomiser.getGreenHopperBean(SprintManager).getAllSprints()


if (user.name.toString() != 'cho') {
    if (!cfVal) {
        if (issue.getIssueType().getName() == 'Admin Task')
            if (sprintServiceOutcome.valid) {
                def Sprint_name = sprintServiceOutcome.getValue()?.findAll { it.rapidViewId == id }?.findAll { it.state == Sprint.State.ACTIVE }?.each { return it.name.toString() }
                issue.setCustomFieldValue(cf, Sprint_name)
                issueManager.updateIssue(user, issue, EventDispatchOption.DO_NOT_DISPATCH, false) }
                //sprintServiceOutcome.getValue().findAll { it.state != Sprint.State.ACTIVE }?.each { updateSprintState(it, Sprint.State.ACTIVE) }
            else {
                log.info "Invalid sprint service outcome, ${sprintServiceOutcome.errors}"
            }
        else
            log.info 'No action taken on issue'
    } else
        null
} else
    null
