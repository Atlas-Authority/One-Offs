// Helps prevent duplicate tickets from being created due to bad UX on the create screen where the create button stays clickable after form submission
// Slightly different from blockDuplicateCreate.js because it's on a different path

AJS.$(document).ajaxError(
	function(event, jqxhr, settings, thrownError) { 
		if (settings.url == "/secure/QuickCreateIssue.jspa?decorator=none" && settings.type == "POST" && thrownError=="timeout"){
			AJS.$(".jira-dialog-heading").after('<div id="aui-message-bar"></div>'); 
			AJS.messages.error({ title: 'Timeout!', body: '<p>It looks like the ticket submission has timed out. Please check to see if the ticket was created before submitting this again.</p>' }); 
		}; 
	});