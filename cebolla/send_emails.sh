#!usr/bin/env bash

file=$(cat ../data/email_list.txt)

for line in $file
do
    python mail.py "$line"
done