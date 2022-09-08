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
  else:
    name = "err"
    code = 399

  bool = validation_general.checkColumns.checkColumnNames(df, name)
  if bool == True:
    logger.critical(str(code) + " Columns mismatched " + name)
    return [name, code]
  else:
    pass

def dataNotCollected(source):
  size = validation_general.checkSize.checkrow(source)
  if size != 0:
    logger.debug("Size OK : " + source)
    pass
  else:
    logger.critical("err 200 : Data is not collected : " + source)
    return "err 200 : Data is not collected : " + source
