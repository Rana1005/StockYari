from django.urls import path
from stock_data_analysis.views import CsvUploadView, AllavaliableIndex, StocksInformationView

urlpatterns = [
    path('csv_upload/', CsvUploadView.as_view()),
    path('all_avaliable_index/',AllavaliableIndex.as_view()),
    path('stock_past_records/',StocksInformationView.as_view())

]