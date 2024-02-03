from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .functions import exceluploadbulk, range_provider, pagination_data, response_formet
from .models import IndexModel,DailyPriceModel
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from .serializers import DailyPriceModelSerializer


class DailyPricePagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

class CsvUploadView(APIView):
    def get(self,request):
        exceluploadbulk()
        return Response({
            "status" : 200
        })

class AllavaliableIndex(APIView):
    def get(self, request):
        all_indeces = IndexModel.objects.all().values_list('name', flat=True)
        return Response({
            "data": all_indeces
        })
    
class StocksInformationView(APIView):
    pagination_class = DailyPricePagination
    def get(self, request):
        request_data = request.data
        daily_price_obj = DailyPriceModel.objects.all()
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        page = request.GET.get("page")
        if start_date and end_date:
            if start_date == end_date:
                daily_price_obj = daily_price_obj.filter(date = start_date)
            else:
                daily_price_obj = daily_price_obj.filter(Q(date__gte = start_date) & Q(date__lte = end_date))
        if request_data.get("open<="):
            daily_price_obj = daily_price_obj.filter(open__lte = request_data.get("open<="))

        if request_data.get("open>="):
            daily_price_obj = daily_price_obj.filter(open__gte = request_data.get("open>="))
        
        if request_data.get("high<="):
            daily_price_obj = daily_price_obj.filter(high__lte = request_data.get("high<="))

        if request_data.get("high>="):
            daily_price_obj = daily_price_obj.filter(high__gte = request_data.get("high>="))

        if request_data.get("low<="):
            daily_price_obj = daily_price_obj.filter(low__lte = request_data.get("low<="))

        if request_data.get("low>="):
            daily_price_obj = daily_price_obj.filter(low__gte = request_data.get("low>="))

        if request_data.get("close<="):
            daily_price_obj = daily_price_obj.filter(close__lte = request_data.get("close<="))

        if request_data.get("close>="):
            daily_price_obj = daily_price_obj.filter(close__gte = request_data.get("close>="))

        if request_data.get("shares_traded<="):
            daily_price_obj = daily_price_obj.filter(shares_traded__lte = request_data.get("shares_traded<="))

        if request_data.get("shares_traded>="):
            daily_price_obj = daily_price_obj.filter(shares_traded__gte = request_data.get("shares_traded>="))

        if request_data.get("turnover<="):
            daily_price_obj = daily_price_obj.filter(turnover__lte = request_data.get("turnover<="))

        if request_data.get("turnover>="):
            daily_price_obj = daily_price_obj.filter(turnover__gte = request_data.get("turnover>="))

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(daily_price_obj, request)
        ranges = range_provider(daily_price_obj)
        paginations = pagination_data(daily_price_obj,page,25)
        serializer = DailyPriceModelSerializer(result_page, many=True)
        data = response_formet(serializer.data)
        
        return Response({
            "start-date":start_date,
            "end_date":end_date,
            "pagination":paginations,
            "data":data,
            "ranges":ranges
        })


