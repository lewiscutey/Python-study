import csv

def handleCsv(filePath, newFilePath):
  origin_f = open(filePath, 'rt',  encoding="utf-8")
  new_f = open(newFilePath, 'w')
  reader = csv.reader(origin_f)
  writer = csv.writer(new_f)
  for i, row in enumerate(reader):
      if i > 0:
          row.pop(0)
          writer.writerow(row)
  origin_f.close()
  new_f.close()
