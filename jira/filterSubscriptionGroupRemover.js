<script>
	// This code hides groups from the Edit Subscription UI
	AJS.toInit(function(){

		if (window.location.pathname.includes("EditSubscription") && !AJS.$("#system-admin-menu")){

			const groupsToRemove = ["jira-users",
			"jira-software-users",
			"jira-administrators",
			"jira-servicedesk-users",
			"jira-system-administrator",
			"jira-service-accounts",
			"jsd-customers"];

			for (i in groupsToRemove){
			AJS.$("select[name='groupName'] option[value=" + groupsToRemove[i] + "]").remove()
			}
		}

	});
</script>