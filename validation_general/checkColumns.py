def checkColumnNames(df, source):
  if source == 1:  # Google News
    ori = ['position', 'link', 'title', 'source', 'date', 'snippet', 'thumbnail']
  elif source == 2:  # News API
    ori = ['author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content', 'status', 'totalResults',
           'id', 'name']
  elif source == 3:  # NewsCatcher
    ori = ['title', 'author', 'published_date', 'published_date_precision', 'link', 'clean_url', 'excerpt', 'summary',
           'rights', 'rank', 'topic', 'country', 'language', 'authors', 'media', 'is_opinion', 'twitter_account',
           '_score', '_id', 'status', 'total_hits', 'page', 'total_pages', 'page_size', 'user_input']
  else:
    ori = ["w"]

  if list(df.columns) == ori:
    return False
  else:
    return True
