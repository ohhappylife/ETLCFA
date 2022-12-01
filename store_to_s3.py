from config import credential_aws_key, credential_aws_secret
def savetoBucket_csv(df, bn, fn):
  path = "s3://" + bn + "/" + fn
  df.to_csv(path,
            sep='|', # delimeter
            storage_options={'key': credential_aws_key,
                             'secret': credential_aws_secret})

def savetoBucket_excel(df, bn, fn):
  path = "s3://" + bn + "/" + fn
  df.to_excel(path,
            storage_options={'key': credential_aws_key,
                             'secret': credential_aws_secret})