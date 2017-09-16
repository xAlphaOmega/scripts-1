#!/bin/sh
# Housekeeping script /var/scripts/housekeeping.sh (deletes backups which are older than 30 days)
path=/var/pgdump
logfile=/var/log/$0

rm -f $logfile
for file in `find /var/pgdump/ -mtime +30 -type f -name *.sql.gz`
do
  echo "deleting: " $file >> $logfile
  rm $file
done

exit 0
