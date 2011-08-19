#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mizan
#
# Created:     19/08/2011
# Copyright:   (c) mizan 2011
# Licence:     <open source licenced under gnu/gpl>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import urllib
#code only looks at one page of followers instead of continuing to all of a user's followers
#decided to only use a small sample

site = "http://mobile.twitter.com"
friends = set()
response = urllib.urlopen(site)
html = response.read()
soup = BeautifulSoup(html)


mainTrend = soup.find('div',{'class' : 'main-trend'})

links= mainTrend.findAll('a',{'href':True})

for link in links:
    linkLabel=link.renderContents().lower()
    url=str(link['href'])
    print "--------------------", url,"----------------------------------------------------"

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tweets = soup.findAll('span',{'class' : 'status'})
    for tweet in tweets:
        for content in tweet.contents:
            print str(content)







print ("happy coding")

