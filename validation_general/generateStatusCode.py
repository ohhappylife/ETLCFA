import validation_general
from logger import logger

def columnsChanged(source, df):
  if source == 1:
    name = "Google"
    code = 301
  elif source == 2:
    name = "NewsAPI"
    code = 302
  elif source == 3:
    name = "NewsCatcher"
    code = 303
  elif source == 4:
    name = "Politifact"
    code = 304
  elif source == 5:
    name = "NYTimes"
    code = 305
  else:
    name = "err"
    code = 399

  bool = validation_general.checkColumns.checkColumnNames(df, source)
  if bool == True:
    logger.critical(str(code) + ": Columns mismatched " + name)
    return [name, code]
  else:
    logger.debug("Columns Unchanged : " + name)
    pass

def dataNotCollected(source, df):
  if source == 1:
    name = "Google"
    code = 401
  elif source == 2:
    name = "NewsAPI"
    code = 402
  elif source == 3:
    name = "NewsCatcher"
    code = 403
  elif source == 4:
    name = "Politifact"
    code = 404
  elif source == 5:
    name = "NYTimes"
    code = 405
  else:
    name = "err"
    code = 499

  size = validation_general.checkSize.checkrow(df)
  if size != 0:
    logger.debug("Size OK : " + source)
    pass
  else:
    logger.critical(str(code) + ": Data is not collected : " + source)
    return (str(code) + ": Data is not collected : " + source)
