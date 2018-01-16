psql -d jiradb -o '/tmp/test.csv' -c "copy (select cfname as \"Field Name\", right(customfieldtypekey, -50) as \"Field Type\" from customfield where customfieldtypekey like 'com.atlassian.jira.plugin.system%' order by customfieldtypekey, cfname) TO STDOUT with CSV HEADER"

