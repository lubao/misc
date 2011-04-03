#!/bin/bash
echo -n SQL Password:
read -s PW
#echo $PW
mysql -uroot -p$PW -e 'CREATE DATABASE `smsd`'
mysql -uroot -p$PW smsd < smsd.sql
mysql -uroot -p$PW -e 'show databases;'
echo Done.
