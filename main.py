#!/usr/bin/env python
#coding:UTF-8

##### NOTE ######
# Zeus Tracker
#################

## set constant
# Database Server URL
URL = 'https://zeustracker.abuse.ch/blocklist.php?download=baddomains'

## download file path and filename
download_path = './'
download_filename = 'zeus_malicious_list.txt'

## import module
import urllib2

## main code
response = urllib2.urlopen(URL)

file = open(download_path + download_filename,'w')

for line in response:
    if line.find('#') == 0 or len(line) == 1:
        continue
    file.write(line)

file.close()