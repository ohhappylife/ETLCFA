# ETLCFA

## Usage
1. Collects news article / title based on keywords from different news media.
2. Clean the text data by removing stopwords, creating N-Gram from the text.
3. Users can set keyword for the articles for search (except politifact).
4. Users can leverage S3 to store and retrieve data.

## Source
This will collect news from following sources:
  - Google News
    - https://news.google.com/
  - News API
    - https://newsapi.org/
  - NewsCatcher News API
    - https://newscatcherapi.com/
  - Politifact
    - https://www.politifact.com/
  - NYTimes
    - https://www.nytimes.com/
  - Bing News API
    - https://www.bing.com/news

## How to use
- Please install required library (refer Requirements.txt)
- Please fill API keys and AWS S3 information into the temp.py file
- Please configure main.py before used (please refer to the comment on python file).; 
- Run the main.py with through the command line.
  - e.g., python main.py {keyword} {newsCatcher if 1} {googleNews if 1} {Politifact if 1} {News API if 1} {NYTimes if 1} {Bing if 1}
- Result (collected data, N-gram result) will be stored on S3 Bucket.

## Issues (To-be fixed)
- The pipeline is not a fault-tolerant
- The pipeline does not have function to validate the data (Partially Fixed as of Sept 8 2022).
- The pipeline does not store logs (Partially Fixed  as of Sept 8 2022 : ONLY critical issues and errors are stored into log files).
- As it utilizes default list of stopwords from NLTK, not all stopwords might be removed during the process.
- Stores login credentials into codes can increase chance of data breach.

## Limitations
- Some sources provide limited information
  - Politifact does not have articles.

## Requirements
- Users need to have valid API keys of the sources.
- Users need to have AWS Account, and set S3 storage and s3 bucket for storing dataset.
- Users need to have writing privilege on CWD to store log data.

## Important
- <i> dataset_example </i> folder or a following google drive link that have example dataset (keyword = <i> 'tesla' </i>).
  : <a href = https://tinyurl.com/42f95xvb> Google Drive </a>
  / <a href = https://github.com/ohhappylife/ETLCFA/tree/master/dataset_example> Github Folder </a>
- As of September 05, 2022, development is in progress; pipeline is NOT fault-tolerant and might be unstable.
- Logs are currently stored into cwd, not S3 to minimize the cost.
- Analyze Article.ipynb file contains information about each source.
- column_information.csv file contains information about column for each source.