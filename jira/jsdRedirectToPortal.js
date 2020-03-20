<script>
	window.onload = function() {
		let errorQueue = document.getElementsByClassName("projects-error-page-heading")[0];
		let errorIssue = document.getElementsByClassName("error-image-canNotBeViewed")[0];
		let jsdProjects = ["ITSD", "ITSDNA"]; // Adjust to your JSD project list
		let contextPath = "/jira"; // Adjust to your context path
		if (window.location.pathname.includes("/queues")){
			if (errorQueue){
				window.location.pathname = contextPath + "/servicedesk/customer/user/requests"
			}
		} else if (errorIssue){
			jsdProjects.forEach(function(value){
				if (window.location.pathname.includes("/" + value + "-")){
					const regex = /[A-Z]+[A-Z0-9_]*-[0-9]+/g;
					// May need to be adjusted based on https://confluence.atlassian.com/adminjiraserver/changing-the-project-key-format-938847081.html
					let issueKey = window.location.pathname.match(regex);
					window.location.pathname = contextPath + "/servicedesk/customer/portal/1/" + issueKey	
				}
			});
		}
	}
</script>