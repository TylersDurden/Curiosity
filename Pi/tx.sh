#!/bin/bash
echo 'Enter Remote Host Password'
read password;
lftp sftp://pi:$password@192.168.1.217 -e "get $1;bye"
echo 'Transfer Complete'
#EOF