1. Open up psql
	1. Connect to the jira db
	2. Run: ```\o out.txt```
	3. Update list of SLA Fields you want to recalculate in query.sql
	4. Run the query.sql contents
2. Delete the first and last 2 lines of the output
	1. Then run: ```sed "s/^[ \t]*//" -i out.txt```
3. Update the fixsla.py script for your:
	1. base url        
	2. auth information you need
	3. input filename

There is a bug currently where the last n<10 tickets won't be fixed, but will be printed as the last output of the script. Put them all into a new file and re-run it.