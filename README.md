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

## How to use
- Please install required library (refer Requirements.txt)
- Please fill API keys and AWS S3 information into the temp.py file
- Please configure main.py before used (please refer to the comment on python file).; 
- Run the main.py with through the command line.
  - e.g., python main.py {keyword} {newsCatcher if 1} {googleNews if 1} {Politifact if 1} {News API if 1} (NYTimes if 1)
- Result (collected data, N-gram result) will be stored on S3 Bucket.

## Issues (To-be fixed)
- The pipeline is not a fault-tolerant
- The pipeline does not have function to validate the data.
- The pipeline does not store logs.
- As it utilizes default list of stopwords from NLTK, not all stopwords might be removed during the process.
- Stores login credentials into codes can increase chance of data breach.

## Limitations
- Some sources provide limited information
  - Politifact does not have articles.
  
## Important
- <i> dataset_example </i> forder or a following google drive link that have example dataset (keyword = <i> 'tesla' </i>).
  : <a href = https://tinyurl.com/42f95xvb> Google Drive </a>
  / <a href = https://github.com/ohhappylife/ETLCFA/tree/master/dataset_example> Github Folder </a>
- As of September 05, 2022, development is in progress; pipeline is NOT fault-tolerant and might be unstable.
