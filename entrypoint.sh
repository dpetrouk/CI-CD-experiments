#!/bin/sh -l

time=$(date)
echo "event_info=${1}\ntime: $time" >> $GITHUB_OUTPUT