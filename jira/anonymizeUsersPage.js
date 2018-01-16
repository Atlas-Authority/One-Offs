// No idea why I wrote this, but likely to submit something to the support team.

$("td[data-cell-type='username']").each(
	function (i, userRow) { 
		$(userRow).html('<div><span class="username">admin</span><br><a href="mailto:admin@admin.com"><span class="email">admin@admin.com</span></a></div>'); 
	})