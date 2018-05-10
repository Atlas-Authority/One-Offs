<script>// Addresses https://jira.atlassian.com/browse/JRASERVER-27957

var contextDefender = function(){
	return confirm("Are you sure you want to delete this context?");
}

AJS.$( document ).ready(function() {
  AJS.$('[title="Delete Scheme"]').each(function(index,element){
  	element.onclick=contextDefender;
  })
});
</script>
