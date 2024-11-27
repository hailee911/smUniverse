from django.db import models

class Member(models.Model):
  id = models.CharField(max_length=50, primary_key=True)
  pw = models.CharField(max_length=50, null=False)
  name = models.CharField(max_length=50)
  age = models.CharField(max_length=10)
  role = models.CharField(max_length=50)
  mdate = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f"{self.id},{self.name},{self.mdate}"
