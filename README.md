# ETLCFA

## Usage
1. Collects news article / title based on keywords from different news media.
2. Clean the text data by removing stopwords, creating N-Gram from the text.
3. Users can set keyword for the articles for search (except politifact).
4. Users can leverage S3 to store and retrieve data.

## Output
1. Uni-gram, Bi-gram, Tri-gram for each article and title will be created (by sources),
2. Raw data will be created.
3. Concatenated/individual cleaned data will be stored
   - example: https://drive.google.com/file/d/1jmP28mt2O34NWnW6TB6AJ_Gv7g9dje1d/view?usp=sharing

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
- - Run main.py {keyword} to start the process
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

## Important
- As of September 05, 2022, development is in progress; pipeline is NOT fault-tolerant and might be unstable.
- Logs are currently stored into cwd, not S3 to minimize the cost.
- Analyze Article.ipynb file contains information about each source.
- column_information.csv file contains information about column for each source.