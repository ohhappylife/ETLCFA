def google():
  return ""

def catcher():
  return ''

def news():
  return ''

def NYTiems():
  return ''

def Gurdian():
  return ''

def savetoBucket(df, bn, fn):
  path = "s3://" + bn + "/" + fn
  df.to_csv(path,
            storage_options={'key': '',
                             'secret': ''})