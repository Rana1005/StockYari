import os
import pandas as pd
from django.core.management.base import BaseCommand
from stock_data_analysis.models import IndexModel, DailyPriceModel
from datetime import datetime

class Command(BaseCommand):
    help = 'Bulk upload data from Excel files'

    def handle(self, *args, **kwargs):
        file_dir = os.path.join(r"C:\Users\Antino\Desktop\StockData\data")
        files = os.listdir(file_dir)
        # self.stdout.write(self.style.SUCCESS("All files are === >>> {}".format(files)))

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
                        "date": self.date_converter(str(data[0][i])),
                        "open": data[1][i],
                        "high": data[2][i],
                        "low": data[3][i],
                        "close": data[4][i],
                        "shares_traded": data[5][i],
                        "turnover": data[6][i]
                    }
                    query_list.append(DailyPriceModel(**d))

                    if len(query_list) == 2000:
                        # self.stdout.write(self.style.SUCCESS("Query list ----- >>>>> {}".format(query_list)))
                        DailyPriceModel.objects.bulk_create(query_list)
                        query_list = []
                except Exception as e:
                    self.stdout.write(self.style.ERROR("Exception found: {}".format(str(e))))

        # Insert any remaining items in the query_list
        if query_list:
            # self.stdout.write(self.style.SUCCESS("Query list ----- >>>>> {}".format(query_list)))
            DailyPriceModel.objects.bulk_create(query_list)

    def date_converter(self, dates):
        date_str = dates
        parsed_date = datetime.strptime(date_str, '%d-%b-%Y').strftime('%Y-%m-%d')
        return parsed_date
