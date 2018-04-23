import json
import urllib2
# get data
link = "https://raw.githubusercontent.com/wesm/pydata-book/master/ch02/usagov_bitly_data2012-03-16-1331923249.txt"
data = urllib2.urlopen(link)
records = [json.loads(line) for line in data]
print records[0]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
