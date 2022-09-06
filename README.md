# ETLCFA

## Usage
Collects news about a topic from different news media, and clean the text data by removing stopwords, creating N-Gram from the text.
Users can set keyword for the articles for search (except politifact).

## Source
This will collect news from following sources:
  - Google News
  - News API
  - NewsCatcher News API
  - Politifact

## How to use
- Please install rquired library (refer Requirements.txt)
- Please fill API keys and AWS S3 information into the temp.py file
- Run the main.py with through the command line.
  - e.g., python main.py {keyword} {newsCatcher if 1} {googleNews if 1} {Politifact if 1} {News API if 1}
- Result (collected data, N-gram result) will be stored on S3 Bucket.

## Issues (To-be fixed)
- Systems is not a fault-tolerant.
- As it utilizes default list of stopwords from NLTK, not all stopwords might be removed during the process.

## Important
- <i> dataset_example </i> forder has contains example dataset (keyword = <i> 'tesla' </i>).
- As of September 05, 2022, development is in progress; pipeline is NOT fault-tolerant and might be unstable.
