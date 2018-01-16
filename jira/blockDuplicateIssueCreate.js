<!-- <script> 
//disables Create button once clicked to avoid duplicates 
AJS.toInit(function(){ 
	if (window.location.pathname == "/secure/CreateIssue.jspa"){ 
		AJS.$("#issue-create-submit").click(function(){ setTimeout(function(){ 
			AJS.$("#issue-create-submit").attr("disabled","disabled") }, 1); 
		}); 
	}; 
}); </script>


