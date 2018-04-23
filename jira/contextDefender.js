<script>// Addresses https://jira.atlassian.com/browse/JRASERVER-27957

var contextDefender = function(){
	return confirm("Are you sure you want to delete this context?");
}

$( document ).ready(function() {
  $('[title="Delete Scheme"]').each(function(index,element){
  	element.onclick=contextDefender;
  })
});
</script>
