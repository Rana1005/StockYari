from import_export import resources 
from .models import DailyPriceModel
class DailyPriceModelResource(resources.ModelResource):
    class Meta:
        model = DailyPriceModel
        fields = ('date', 'open', 'high', 'low', 'close', 'shares_traded',"turnover")

    def after_import_instance(self, instance, new, **kwargs):
        # update file name
        file_name = kwargs.get('file_name', 'unknown')
        print("file name is ---->>>>",file_name)
        instance.source = file_name
        


    