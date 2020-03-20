<script>
AJS.toInit(function(){
	var defaultCommentField = document.getElementById("addcomment");
	var clonedFCommentField = defaultCommentField.cloneNode(true);
	var mainColumn = document.getElementsByClassName("aui-item issue-main-column")[0];
	var dndMetadata = document.getElementById("dnd-metadata");
	mainColumn.insertBefore(clonedFCommentField, dndMetadata); 
});
</script>