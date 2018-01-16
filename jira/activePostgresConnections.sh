# See how many active pgsql connections there are

psql -t -A -F";" -c 'select * from pg_stat_activity order by datname;'