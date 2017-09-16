#!/bin/sh    
# Backup-Script /var/scripts/dump_db.sh
hostname=`hostname`

##########################################
## OpenERP Backup
## Backup databases: YOURDB
##########################################

# Stop OpenERP Server
/etc/init.d/odoo-server stop

# Dump DBs

for db in YOURDB
do
  date=`date +"%Y%m%d_%H%M%N"`
  filename="/var/pgdump/${hostname}_${db}_${date}.sql"
  # pg_dump -E UTF-8 -p 5433 -F p -b -f $filename $db
  PGPASSWORD="YOURPASSWORD" pg_dump -h localhost -U odoo -f $filename -d $db
  gzip $filename
done

# Start OpenERP Server
/etc/init.d/odoo-server start

exit 0
