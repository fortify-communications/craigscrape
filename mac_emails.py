#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urlparse import urljoin
import dataset
from pysqlite2 import dbapi2 as sqlite
import os
from thready import threaded
from hashlib import sha1


# connect to our database
con = sqlite.connect('mac.db')
conemails = sqlite.connect('mac_emails.db')

cur = con.cursor()
sql = "select source_url,body from posts where strftime(posted_at) > datetime('now', '-1 day')";
cur.execute(sql)
for row in cur:
  url = row[0]
  body = row[1]
  cur2 = conemails.cursor()
  # if url does not exist in emails
  sql2 = "select source_url from emailed where source_url = '" + url + "'";
  cur2.execute(sql2);
  source_url = "";
  for rowe in cur2:
    source_url = rowe[0]

  print 'source url: "' + source_url + "'";

  if source_url == "":
    sql3 = "insert into emailed values ('"+url+"')";
    cur3 = conemails.cursor()
    cur3.execute(sql3)
    print sql3;
    conemails.commit()
  # send email

    print 'send email'
    os.system('echo "'+body+' '+url+'" | mail -s "phonepurchase iphone" andrei@odeski.ca')
  # insert the source url
