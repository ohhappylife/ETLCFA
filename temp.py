def google():
  return "" # Google API key

def catcher():
  return '' # News Catcher API Key

def news():
  return '' # News API key

def NYTimes():
  return '' # NYTimes API key

def Bing():
  return '' # Bing API Key

def savetoBucket(df, bn, fn): # bn = bucket name, fn = file name
  path = "s3://" + bn + "/" + fn
  df.to_csv(path,
            storage_options={'key': '', # AWS Account Key
                             'secret': ''}) # AWS secret