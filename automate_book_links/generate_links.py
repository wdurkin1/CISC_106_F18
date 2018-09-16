#!/usr/bin/python3
# coding: utf-8

"""

Note: Some duplicates. 
Example: VAUGHAN, DIANA IREY is #20 (last person second page) and #21 (first person 3rd page)
-- Only difference is committee: 
---- https://www.pavoterservices.pa.gov/ElectionInfo/CommitteeInfo.aspx?ID=10260
---- https://www.pavoterservices.pa.gov/ElectionInfo/CommitteeInfo.aspx?ID=14584


"""

#import sys

import requests

import re

from time import sleep

from bs4 import BeautifulSoup



url_base = 'https://automatetheboringstuff.com'

# Read locally when debugging
f = open('home.html', 'r')
html = f.read()
f.close()

# Read from web
#r = requests.get(url_base)
#html = r.text

soup = BeautifulSoup(html, 'html.parser')

soup_chapter_links = soup.find_all('a', href=re.compile('/chapter'))

link_md = ''

for soup_link in soup_chapter_links:

    link_text = soup_link.text
    link_href = soup_link.get('href')
    print(link_text, link_href)

    chapter_link = url_base+link_href

    link_md += "# [{}]({})\n".format(link_text, chapter_link)

    # Read locally when debugging
    f = open('chapter0.html', 'r')
    html = f.read()
    f.close()

    # Read from web
    #r = requests.get()
    #html = r.text

    # Don't need original
    soup = BeautifulSoup(html, 'html.parser')

    soup_section_titles = soup.find_all('h1', {"class": "title2"})

    for soup_section_title in soup_section_titles:

        section_link_text = soup_section_title.text
        section_link_id = soup_section_title.find('a').get('id')
        print(section_link_text, section_link_id)

        link_md += "* [{}]({})\n".format(section_link_text, chapter_link+'#'+section_link_id)

    break

    link_md += "\n"


# Write file
f = open('links.md', 'w')
f.write(link_md)
f.close()

