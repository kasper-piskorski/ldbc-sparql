import csv, os
from datetime import datetime as dt

def generate_seed_dict_bi(row, query_num, DATE_FORMAT):
    if query_num == 1:
      max_date = dt.fromtimestamp(int(row[0])/1000).strftime(DATE_FORMAT)
      return {"maxDate":max_date}
    elif query_num == 2:
      start_date = dt.fromtimestamp(int(row[0])/1000).strftime(DATE_FORMAT)
      end_date = dt.fromtimestamp(int(row[1])/1000).strftime(DATE_FORMAT)
      return {"startDate":start_date, "endDate":end_date, "country1Name":row[2], "country2Name":row[3]}
    elif query_num == 3:
      return {"year1":row[0], "month1":row[1]}
    elif query_num == 4:
      return {"tagClassName":row[0], "countryName":row[1]}
    elif query_num == 5:
      return {"countryName":row[0]}
    elif query_num == 6:
      return {"tagName":row[0]}
    elif query_num == 7:
      return {"tagName":row[0]}
    elif query_num == 8:
      return {"tagName":row[0]}
    elif query_num == 9:
      return {"tagClass1Name":row[0], "tagClass2Name":row[1], "threshold":row[2]}
    elif query_num == 10:
      min_date = dt.fromtimestamp(int(row[1])/1000).strftime(DATE_FORMAT)
      return {"tagName":row[0], "minDate":min_date}
    elif query_num == 11:
      return {"countryName":row[0], "blacklist":row[1].split(";")}
    elif query_num == 12:
      date = dt.fromtimestamp(int(row[0])/1000).strftime(DATE_FORMAT)
      return {"minDate":date, "likeThreshold":row[1]}
    elif query_num == 13:
      return {"countryName":row[0]}
    elif query_num == 14:
      start_date = dt.fromtimestamp(int(row[0])/1000).strftime(DATE_FORMAT)
      end_date = dt.fromtimestamp(int(row[1])/1000).strftime(DATE_FORMAT)
      return {"startDate":start_date, "endDate":end_date}
    elif query_num == 15:
      return {"countryName":row[0]}
    elif query_num == 16:
      return {"personId":row[0], "countryName":row[1], "tagClassName":row[2], "minPathDistance":row[3], "maxPathDistance":row[4]}
    elif query_num == 17:
      return {"countryName":row[0]}
    elif query_num == 18:
      min_date = dt.fromtimestamp(int(row[0])/1000).strftime(DATE_FORMAT)
      return {"minDate":min_date, "lengthThreshold":row[1], "languages":row[2].split(";")}
    elif query_num == 19:
      min_date = dt.fromtimestamp(int(row[0])/1000).strftime(DATE_FORMAT)
      return {"minDate":min_date, "tagClass1Name":row[1], "tagClass2Name":row[2]}
    elif query_num == 20:
      return {"tagClassNames":row[0].split(";")}
    elif query_num == 21:
      end_date = dt.fromtimestamp(int(row[1])/1000).strftime(DATE_FORMAT)
      return {"countryName":row[0], "endDate":end_date}
    elif query_num == 22:
      return {"country1Name":row[0], "country2Name":row[1]}
    elif query_num == 23:
      return {"countryName":row[0]}
    elif query_num == 24:
      return {"tagClassName":row[0]}
    elif query_num == 25:
      start_date = dt.fromtimestamp(int(row[2])/1000).strftime(DATE_FORMAT)
      end_date = dt.fromtimestamp(int(row[3])/1000).strftime(DATE_FORMAT)
      return {"person1Id":row[0], "person2Id":row[1], "startDate":start_date, "endDate":end_date}

def generate_seed_dict_ic(row, query_num, DATE_FORMAT):
    if query_num == 1:
      return {"personId":row[0], "firstName":row[1]}
    elif query_num == 2:
      max_date = dt.fromtimestamp(int(row[1])/1000).strftime(DATE_FORMAT)
      return {"personId":row[0], "maxDate":max_date}
    elif query_num == 3:
      start_date = dt.fromtimestamp(int(row[1])/1000).strftime(DATE_FORMAT)
      return {"personId":row[0], "startDate":start_date, "durationDays":row[2], "countryXName":row[3], "countryYName":row[4]}
    elif query_num == 4:
      start_date = dt.fromtimestamp(int(row[1])/1000).strftime(DATE_FORMAT)
      return {"personId":row[0], "startDate":start_date, "durationDays":row[2]}
    elif query_num == 5:
      min_date = dt.fromtimestamp(int(row[1])/1000).strftime(DATE_FORMAT)
      return {"personId":row[0], "minDate":min_date}
    elif query_num == 6:
      return {"personId":row[0], "tagName":row[1]}
    elif query_num == 7:
      return {"personId":row[0]}
    elif query_num == 8:
      return {"personId":row[0]}
    elif query_num == 9:
      max_date = dt.fromtimestamp(int(row[1])/1000).strftime(DATE_FORMAT)
      return {"personId":row[0], "maxDate":max_date}
    elif query_num == 10:
      month = int(row[1])
      next_month = (month + 1) if month < 12 else 1
      return {"personId":row[0], "month":str(month), "nextMonth":str(next_month)}
    elif query_num == 11:
      return {"personId":row[0], "countryName":row[1], "workFromYear":row[2]}
    elif query_num == 12:
      return {"personId":row[0], "tagClassName":row[1]}
    elif query_num == 13:
      return {"person1Id":row[0], "person2Id":row[1]}
    elif query_num == 14:
      return {"person1Id":row[0], "person2Id":row[1]}

def generate_seed_dict(row, query_type, query_num, DATE_FORMAT):
  if query_type == "ic":
      seed = generate_seed_dict_ic(row, query_num, DATE_FORMAT)
  elif query_type == "bi":
      seed = generate_seed_dict_bi(row, query_num, DATE_FORMAT)
  return seed

def get_seeds(path, num, query_type, query_num, DATE_FORMAT):
  f_name = "interactive_{}_param.txt".format(query_num) if query_type == "ic" \
      else "bi_{}_param.txt".format(query_num)

  seeds = []
  with open(os.path.join(path, f_name), "r") as f:
    reader = csv.reader(f, delimiter="|")
    next(reader) # skip header
    count = 0
    for row in reader:
      seed = generate_seed_dict(row, query_type, query_num, DATE_FORMAT)
      seeds.append(seed)
      count += 1
      if count >= num:
        break
  return seeds