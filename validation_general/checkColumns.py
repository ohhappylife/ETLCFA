def checkColumnNames(df, source):
  """
  This will compare columns from collected dataframe and compare columns name with information below.
  :param dataframe df: dataframe to be cleaned, String source: source
  :return: boolean
  :rtype: boolean
  """
  if source == 1:  # Google News
    ori = ['position', 'link', 'title', 'source', 'date', 'snippet', 'thumbnail']
  elif source == 2:  # News API
    ori = ['author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content', 'status', 'totalResults',
           'id', 'name']
  elif source == 3:  # NewsCatcher
    ori = ['title', 'author', 'published_date', 'published_date_precision', 'link', 'clean_url', 'excerpt', 'summary',
           'rights', 'rank', 'topic', 'country', 'language', 'authors', 'media', 'is_opinion', 'twitter_account',
           '_score', '_id', 'status', 'total_hits', 'page', 'total_pages', 'page_size', 'user_input']
  elif source == 5:  # NYTimes
    ori = ['abstract', 'web_url', 'snippet', 'lead_paragraph', 'print_section', 'print_page', 'source', 'multimedia',
           'keywords', 'pub_date', 'document_type', 'news_desk', 'section_name', 'subsection_name', 'type_of_material',
           '_id', 'word_count', 'uri', 'headline.main', 'headline.kicker', 'headline.content_kicker',
           'headline.print_headline', 'headline.name', 'headline.seo', 'headline.sub', 'byline.original',
           'byline.person', 'byline.organization', 'subsection_name']
  elif source == 6:
    ori = ['name', 'url', 'description', 'about', 'mentions', 'provider',
           'datePublished', 'image.thumbnail.contentUrl', 'image.thumbnail.width',
           'image.thumbnail.height', 'category', 'video.name',
           'video.motionThumbnailUrl', 'video.thumbnail.width',
           'video.thumbnail.height', 'video.thumbnailUrl', 'video.embedHtml',
           'video.allowHttpsEmbed']
  else:
    ori = ["___"]

  if list(df.columns) == ori: # Columns are matched
    return False

  else: # Columns are not matched
    return True
