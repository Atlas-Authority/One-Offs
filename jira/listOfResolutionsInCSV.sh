psql -d jiradb -o '/tmp/test.csv' -c "copy (select pname as "name",sequence from resolution order by sequence) TO STDOUT with CSV HEADER"

