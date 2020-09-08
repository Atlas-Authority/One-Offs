"""
Built for python3

This generator is intended to work with the 
output of the following SQL (postgres) at the bottom of this file 
"""

import csv
with open('userkey.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print "update jiraissue set assignee = (select user_key from app_user where lower_user_name = \'" + row[3].lower()  + "\') where assignee = \'" + row[1] + "\' ;"
        print "update jiraissue set reporter = (select user_key from app_user where lower_user_name = \'" + row[3].lower()  + "\') where reporter = \'" + row[1] + "\' ;"
        print "update changegroup set author = (select user_key from app_user where lower_user_name = \'" + row[3].lower()  + "\') where author = \'" + row[1] + "\' ;"
        print "update changeitem set oldvalue = (select user_key from app_user where lower_user_name = \'" + row[3].lower()  + "\') where oldvalue = \'" + row[1] + "\' ;"
        print "update changeitem set newvalue = (select user_key from app_user where lower_user_name = \'" + row[3].lower()  + "\') where newvalue = \'" + row[1] + "\' ;"
        print "update customfieldvalue set stringvalue = (select user_key from app_user where lower_user_name = \'" + row[3].lower()  + "\') where stringvalue = \'" + row[1] + "\' ;"
        print "update jiraaction set author = (select user_key from app_user where lower_user_name = \'" + row[3].lower()  + "\') where author = \'" + row[1] + "\' ;"
        print "update jiraaction set updateauthor = (select user_key from app_user where lower_user_name = \'" + row[3].lower()  + "\') where updateauthor = \'" + row[1] + "\' ;"


"""
After running this, you need to manually add another 
column with the destination user name

select *
	from app_user 
	where lower_user_name not in (
		select lower_user_name 
		from cwd_user)
	and 
	  user_key in (
		select assignee
	  	from jiraissue
		union
		select reporter
	  	from jiraissue
		union
		select author 
		from changegroup
		union
		select oldvalue
		from changeitem
		union
		select newvalue
		from changeitem
		union 
		select stringvalue
		from customfieldvalue
		union 
		select author
		from jiraaction
		union 
		select updateauthor
		from jiraaction)
"""
