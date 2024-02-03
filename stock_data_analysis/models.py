from django.db import models

# below I have created this two model just for illustration that we can create one - many relation
# between IndexModel DailyPriceModel
class IndexModel(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class DailyPriceModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    indexes = models.ForeignKey(IndexModel, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    shares_traded = models.FloatField()
    turnover = models.FloatField()

# below model is able to handle data upload 
    
