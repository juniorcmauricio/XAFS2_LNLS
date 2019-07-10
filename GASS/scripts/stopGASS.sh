#!/bin/bash

echo Stopping GASS...
ps -ef | grep gass | grep -v grep | awk {'print $2'} | xargs kill -s 2
echo "Last GASS aborted with SIGINT (CTRL+C). Output data file will be saved."
sleep 0.1
echo Killing remaining gass...!
ps -ef | grep gass | grep -v grep | awk {'print $2'} | xargs kill 
echo GASS process stopped!
