# ETLCFA
This will collect news from different sources (mainly APIs) based on keyword, and stored cleaned articles into the S3 Bucket.

## Output
- Cleaned data, which include following will be stored:
  - Source
  - Published Date
  - Title
  - Articles
  - Title_without_stopwords	
  - Text_without_stopwords	
  - Language	
  - Site_url	
  - Main_img_url
  - Image (whether news contains image)	
  - API Source	
  - summarized_text	
  - Keyword of Title
  - Keyword of Text
- Raw data, uncleaned data, N-Gram data can be stored based on configuration.

## Source
This will collect news from following sources:
  - Google News - It utilized SerpAPI for crawling news data from Google.
    - https://news.google.com/
      - Request API key from https://serpapi.com/news-results
  - News API
    - https://newsapi.org/
      - Request API key from https://newsapi.org/register
  - NewsCatcher News API
    - https://newscatcherapi.com/
      - Request API key from https://newscatcherapi.com/news-api
  - Politifact
    - https://www.politifact.com/
      - API key is not needed.
  - NYTimes
    - https://www.nytimes.com/
      - Request API key from https://developer.nytimes.com/signup
  - Bing News
    - https://www.bing.com/news
      - Request API key from MS Azure (https://portal.azure.com/#create/microsoft.bingsearch).

## How to use
- Please install required library (refer Requirements.txt).
- Set the config_example.py file, and change the file name into config.py.
- Run main.py to start the process
- Result (collected data, N-gram result, summarized text) will be stored on S3 Bucket.

## Issues (To-be fixed)
- As it utilizes default list of stopwords from NLTK, not all stopwords might be removed during the process.

## Limitations
- Some sources provide limited information
  - Politifact does not have articles.

## Requirements
- Users need to have valid API keys of the sources.
- Users need to have AWS Account, and set S3 storage and s3 bucket for storing dataset.
- Users need to have writing privilege on CWD to store log data.
- Users need to install dependency (Requirement.txt)

## Important
- Logs are currently stored into cwd, not S3 to minimize the cost.
- Analyze Article.ipynb file contains information about each source (outdated as November 15th, will update soon).
- column_information.csv file contains information about column for each source.