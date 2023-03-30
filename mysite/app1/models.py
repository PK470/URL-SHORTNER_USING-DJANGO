from django.db import models
from datetime import datetime  

# Create your models here.
class Url(models.Model):
    fullurl = models.CharField(unique=True, max_length = 400)
    Shorturl = models.CharField(unique=True, max_length = 20)
    def __sizeof__(self):
        return self.fullurl
    @classmethod
    def create(self,full_url):
        now = datetime.now()
       
        dt_obj = datetime.strptime( str(now), '%Y-%m-%d %H:%M:%S.%f')  
        epoch = dt_obj.timestamp() * 1000  
        try:
            obj = self.objects.create(fullurl = full_url,Shorturl = str(int(epoch)))
        except:
            obj = self.objects.get(fullurl = full_url)
            
        return obj