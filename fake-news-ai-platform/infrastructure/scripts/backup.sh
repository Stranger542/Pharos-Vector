#!/bin/bash

timestamp=$(date +%F-%H-%M-%S)
pg_dump -U postgres -h localhost -F c -b -v -f "backup-$timestamp.dump" fakenewsdb
echo "Backup saved to backup-$timestamp.dump"
