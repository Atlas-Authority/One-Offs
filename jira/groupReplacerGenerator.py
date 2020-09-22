"""
This generator is intended to work with a CSV input 
similar to the sample at the bottom of this file
The names of the groups in the file should be in 
mixed case as they are used in Jira
"""

import csv
with open('groupmap.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		# Notification Scheme
		print "update notification set notif_parameter = \'" + row[1] + "\' where notif_parameter = \'" + row[0] + "\' and notif_type = 'Group_Dropdown';"
        # Issue Security Schemes:
		print "update schemeissuesecurities set sec_parameter = \'" + row[1] + "\' where sec_parameter = \'" + row[0] + "\' and sec_type = 'group';"
		# Permission Schemes:
		print "update schemepermissions set perm_parameter = \'" + row[1] + "\' where perm_parameter =  \'" + row[0] + "\' and perm_type = 'group';"
		# Filters:
		print "update searchrequest set groupname = \'" + row[1] + "\' where groupname = \'" + row[0] + "\';"
		# Filters2:
		print "update sharepermissions set param1 = \'" + row[1] + "\' where sharetype = 'group' and param1 = \'" + row[0] + "\';"
		# Filter Subsriptions:
		print "update filtersubscription set groupname = \'" + row[1] + "\' where groupname = \'" + row[0] + "\';"
		# Comments:
		print "update jiraaction set actionlevel = \'" + row[1] + "\' where actionlevel = \'" + row[0] + "\';"
		# Worklogs
		print "update worklog set grouplevel = \'" + row[1] + "\' where grouplevel = \'" + row[0] + "\';"
		# Project Roles:
		print "update projectroleactor set roletypeparameter = \'" + row[1] + "\' where roletypeparameter = \'" + row[0] + "\' and roletype = 'atlassian-group-role-actor';"
		# Global Perms:
		print "update globalpermissionentry set group_id = \'" + row[1] + "\' where group_id = \'" + row[0] + "\';"
		# License Role Groups:
		print "update licenserolesgroup set group_id = \'" + row[1].lower() + "\' where group_id = \'" + row[0].lower() + "\';"
		# Update CFV:
		print "update customfieldvalue set stringvalue = \'" + row[1] + "\' where stringvalue = \'" + row[0] + "\' and customfield in (select id from customfield where customfieldtypekey in ('com.atlassian.jira.plugin.system.customfieldtypes:multigrouppicker', 'com.atlassian.jira.plugin.system.customfieldtypes:grouppicker'));"
		# Structure Share Permissions:
		print "update \"AO_8BAD1B_STRUCTURE\" set \"C_PERMISSONS\" = REPLACE(\"C_PERMISSONS\", \'" + row[0] + "\', \'" + row[1] + "\') where \"C_PERMISSONS\" like '%" + row[0] + "%';" 

#This is not relevant for some people
with open('groupmap.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		# Identify which filters have the group in it:
		print "select * from searchrequest where reqcontent like '%" + row[0] + "%';" 
		# Identify workflows that have the group in it:
		print "select workflowname from jiraworkflows where descriptor like '%" + row[0] + "%';" 

"""
oldgroup, newgroup
oldergroup, newergroup
"""