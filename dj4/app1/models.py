from django.db import models
class students(models.Model):
    name1=models.CharField(max_length=50)

    def __str__(self):
    	return self.name1