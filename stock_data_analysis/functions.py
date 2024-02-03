import os
import pandas as pd
from .models import IndexModel, DailyPriceModel
from datetime import datetime
from django.db.models import Min, Max

def exceluploadbulk():
    file_dir = os.path.join(r"C:\Users\Antino\Desktop\StockData\data")
    files = os.listdir(file_dir)
    print("all files are === >>>", files)

    query_list = []
    
    for file in files:
        index_or_stocks = file[0:len(file)-29]
        index_instance, created = IndexModel.objects.get_or_create(name=index_or_stocks)
        
        file_path = os.path.join(file_dir, file)
        df = pd.read_csv(file_path, header=None, delimiter=",")
        up_index = len(df.index)
        data = df.to_dict()
        
        for i in range(1, up_index):
            try:
                d = {
                    "indexes": index_instance,
                    "date": date_converter(str(data[0][i])),
                    "open": data[1][i],
                    "high": data[2][i],
                    "low": data[3][i],
                    "close": data[4][i],
                    "shares_traded": data[5][i],
                    "turnover": data[6][i]
                }
                query_list.append(DailyPriceModel(**d))
                
                if len(query_list) == 2000:
                    print("query_list ----- >>>>>", query_list)
                    DailyPriceModel.objects.bulk_create(query_list)
                    query_list = []
            except Exception as e:
                print("exception found", str(e))

    # Insert any remaining items in the query_list
    if query_list:
        print("query_list ----- >>>>>", query_list)
        DailyPriceModel.objects.bulk_create(query_list)

def date_converter(dates):
    date_str = dates
    parsed_date = datetime.strptime(date_str, '%d-%b-%Y').strftime('%Y-%m-%d')
    return parsed_date


def range_provider(queryset):
    
    result = queryset.aggregate(
        min_open=Min('open'),
        max_open=Max('open'),
        min_high=Min('high'),
        max_high=Max('high'),
        min_low = Min('low'),
        max_low = Max('low'),
        min_shares_traded = Min('shares_traded'),
        max_shares_traded = Max('shares_traded'),
        min_close = Min('close'),
        max_close = Max('close'),
        min_turnover = Min('close'),
        max_turnover = Max('close'),
    )
    ranges = {
        "open": {"lowest": result["min_open"], "highest": result["max_open"]},
        "high": {"lowest": result["min_high"], "highest": result["max_high"]},
        "low":  {"lowest": result["min_low"], "highest": result["max_low"]},
        "close": {"lowest": result["min_close"], "highest": result["max_close"]},
        "shares_traded": {"lowest": result["min_shares_traded"], "highest": result["max_shares_traded"]},
        "turnover": {"lowest": result["min_turnover"], "highest": result["max_turnover"]}
    }

    return ranges

def pagination_data(querset, page, page_size):
    total_rows = len(querset)
    total_page = total_rows // page_size
    remainder = total_rows % page_size
    if remainder != 0:
        total_page = total_page + 1
    pagination = {
        "page":page,
        "total_pages":total_page,
        "total_rows":total_rows
    }
    return pagination

def response_formet(querset_result):
    for data in querset_result:
        del data['id']
        data["indexes"] = IndexModel.objects.get(id = data["indexes"]).name

    return querset_result


    
    