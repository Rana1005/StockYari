from django.contrib import admin
from .models import IndexModel,DailyPriceModel
from .resource import DailyPriceModelResource
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(DailyPriceModel)
class DailyPriceModelAdmin(ImportExportModelAdmin):
    resource_class = DailyPriceModelResource
    list_display = ('id','indexes', 'date', 'open', 'high', 'low', 'close', 'shares_traded',"turnover")

admin.site.register(IndexModel)

