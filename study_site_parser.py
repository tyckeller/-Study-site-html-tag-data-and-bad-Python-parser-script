import requests
import re
from bs4 import BeautifulSoup

with open("study_site_text.txt") as yj:
    yj_soup = BeautifulSoup(yj)

tag_titles_counts = {}

for tag in yj_soup.find_all('li'):
    tag_title = tag.find('a')
    tag_count = tag.find('span')
    new_tag_count = re.sub('[ ()]', '', tag_count.string)
    if type(tag_title.string) != None:
        tag_titles_counts[tag_title.string] = int(new_tag_count)

def dict_50_len():
    empty_dict = {}
    for i in range(50):
        empty_dict[i] = 0
    return empty_dict
 
def top_fifty(dictionary):
    fifty_dict = dict_50_len()
    for key, value in dictionary.items():
        for fifty_key, fifty_value in fifty_dict.items():
            if value > fifty_value:
                fifty_dict.pop(fifty_key)
                fifty_dict[key] = value
    return fifty_dict

for key, value in top_fifty(tag_titles_counts).items():
    print("{}: {}".format(key, value))
        
