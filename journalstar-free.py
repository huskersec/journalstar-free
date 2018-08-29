#!/usr/bin/python

import sys
import argparse
from lxml import html
import requests

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Scrape Journal Star articles.',usage='./journalstar.py -u <URL>' + "\n")

parser.add_argument("-u", "--url", action='store', dest='url', 
    help="specify url to scrape")

args = parser.parse_args()
args_url = args.url

r = requests.get(args_url)

tree = html.fromstring(r.content)

article_title = tree.xpath('//meta[@property="og:title"]/content/text()')
#article_title = article_title.translate(None, '[]')

subscriber_preview = tree.xpath('//div[@class="subscriber-preview"]/p/text()')

###<div class="subscriber-only"><p>The sophomore
subscriber_only = tree.xpath('//div[@class="subscriber-only"]/p/text()')

print_trim = tree.xpath('//span[@class="print_trim"]/text()')

print "subscriber-preview: ", subscriber_preview
print "subscriber-only: ", subscriber_only
print "print_trim: ", print_trim

f = open("article.html", "w")
f.write("<html><body>")
f.write("<title>")
f.write(repr(article_title))
f.write("</title>")
f.write("<p>")
f.write(repr(subscriber_preview))
f.write("</p>")
f.write("<p>")
f.write(repr(subscriber_only))
f.write("</p>")
f.write("<p>")
f.write(repr(print_trim))
f.write("</p>")
f.write("</body></html>")
f.close()

### auto open html file here



### References ###
#https://docs.python-guide.org/scenarios/scrape/
#https://stackoverflow.com/questions/23900348/why-does-this-xpath-fail-using-lxml-in-python
### References ###
