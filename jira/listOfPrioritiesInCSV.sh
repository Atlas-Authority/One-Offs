psql -d jiradb -o '/tmp/test.csv' -c "copy (select pname as name, description, sequence from priority order by sequence) TO STDOUT with CSV HEADER"

