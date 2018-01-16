let list; 
$( "strong[data-issue-type-field='name']" ).each(
	function( index, issueType ) { 
		list = list + ', ' + issueType.innerText }); 

console.log(list)
