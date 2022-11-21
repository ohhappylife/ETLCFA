"""
  politifact_cralwer.py
  crawl the data from politifact.
  url : https://www.politifact.com/factchecks/list/
    requirements : Users shall have privileges to save the file into a cwd.
    input : none
    output : csv file with columns of
    ['Author', 'Published Date', 'Title', 'Text', 'Title_without_stopwords', 'Text_without_stopwords',
       'Language', 'Site_url', 'Main_img_url', 'Type', 'Label', 'hasImage']
"""
__author__ = "Shon"
__version__ = "1.0.1"
__email__ = "sshon2@alumni.jh.edu"
__status__ = "Production"

from datetime import date
from time import strptime
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

import store_to_s3
from validation_general import generateStatusCode
from config import bool_store_politifact_raw, s3_poltifiact_raw

today = date.today()

authors = []
dates = []
statements = []
sources = []
targets = []
url = []

def runit(keyword):
  """
  Crawl Nes data from Politifact
  :param None
  :return: collected news articles and its information.
  :rtype: dataframe
  """
  # Create a function to scrape the site
  def scrape_website(page_number, source):
    page_num = str(page_number)  # Convert the page number to a string

    '''source: a certain speaker only'''
    URL = 'https://www.politifact.com/factchecks/list/?page={}&speaker={}'.format(page_num, source)

    webpage = requests.get(URL)  # Make a request to the website
    soup = BeautifulSoup(webpage.text, "html.parser")  # Parse the text from the website
    # Get the tags and it's class
    statement_footer = soup.find_all('footer', attrs={'class': 'm-statement__footer'})  # Get the tag and it's class
    statement_quote = soup.find_all('div', attrs={'class': 'm-statement__quote'})  # Get the tag and it's class
    statement_meta = soup.find_all('div', attrs={'class': 'm-statement__meta'})  # Get the tag and it's class
    target = soup.find_all('div', attrs={'class': 'm-statement__meter'})  # Get the tag and it's class
    # loop through the footer class m-statement__footer to get the date and author
    for i in statement_footer:
      link1 = i.text.strip()
      name_and_date = link1.split()
      first_name = name_and_date[1]
      last_name = name_and_date[2]
      full_name = first_name + ' ' + last_name

      try:
        month = name_and_date[4].replace("•", "")
        day = name_and_date[5].replace("•", "")
        year = name_and_date[6].replace("•", "")
        month = strptime(month,'%B').tm_mon
      except ValueError:
        month = name_and_date[4].replace("•", "")
        day = name_and_date[5].replace("•", "")
        year = name_and_date[6].replace("•", "")
      date = str(str(year) + "-" + str(month) + "-" + str(day))
      dates.append(str(date))
      authors.append(full_name)
    # Loop through the div m-statement__quote to get the link
    for i in statement_quote:
      link2 = i.find_all('a')
      statements.append(link2[0].text.strip())
      base = "https://www.politifact.com/"
      search_str = re.findall(r'"([^"]*)"', str(link2))
      ourl = base + str(search_str[0])
      url.append(ourl)

    # Loop through the div m-statement__meta to get the source
    for i in statement_meta:
      link3 = i.find_all('a')  # Source
      source_text = link3[0].text.strip()
      sources.append(source_text)
    # Loop through the target or the div m-statement__meter to get the facts about the statement (True or False)
    for i in target:
      fact = i.find('div', attrs={'class': 'c-image'}).find('img').get('alt')
      targets.append(fact)

  # Loop through 'n-1' webpages to scrape the data
  n = 2
  for i in range(1, n):
    scrape_website(i, source='')

  c = generateStatusCode.dataNotCollected(1, url)

  if c == 1:
    # Create a new dataFrame
    df = pd.DataFrame(columns=['Author', 'Published Date', 'Title', 'Text',
                               'Title_without_stopwords', 'Text_without_stopwords',
                               'Language', 'Site_url', 'Main_img_url', 'Type',
                               'Label', 'hasImage'])
    df['Author'] = sources
    df['Published Date'] = list(map(lambda x: x.replace(',', ''),dates))
    df['Title'] = statements
    df['Text'] = 'Unavailable'
    df['Title_without_stopwords'] = ''
    df['Text_without_stopwords'] = ''
    df['Language'] = 'English'
    df['Site_url'] = url
    df['Main_img_url'] = ''
    df['Type'] = 'Unknown'
    df['Label'] = targets
    df['hasImage'] = False

    # Show the data set
    generateStatusCode.dataNotCollected(4, df)

    fname = "raw_politifact_" + keyword + '_' + str(today) + '.csv'
    store_to_s3.savetoBucket_csv(df, 'newsrawpolitifact', fname)
    if bool_store_politifact_raw == True:
      fname = "uncleared_politifact_" + keyword + '_' + str(today) + '.csv'
      store_to_s3.savetoBucket_csv(df, s3_poltifiact_raw, fname)

    return df
  else:
    return url