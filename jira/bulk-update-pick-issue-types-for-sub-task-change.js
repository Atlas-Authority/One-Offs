// Changes the issue type of all items on a bulk move page on Jira Cloud when all items in the bulk move are sub-task issue types.
for (row of document.getElementsByClassName("issue-type-selector-container")){
	switch(row.getElementsByClassName("from-issue-type")[0].innerText){
		//Original Issue Type
		case 'Technical Task':
			row.getElementsByClassName("drop-menu")[0].click()
			for (issueType of document.getElementsByClassName("ajs-layer box-shadow active")[0].getElementsByClassName("aui-list-item")) {
				// New Issue Type
				if (issueType.children[0].innerText === 'Generis Sub-task') {
					issueType.click()
				}
			}
	}
}