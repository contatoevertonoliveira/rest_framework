from django.db import models

class Books(models.Model):
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  release_year = models.IntegerField()
  state = models.CharField(max_length=50)
  pages = models.IntegerField()
  publishing_company = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title
