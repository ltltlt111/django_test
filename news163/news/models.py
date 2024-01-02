from django.db import models

# Create your models here.
class NewsType(models.Model):
    news_type = models.CharField(max_length=20)

class News(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.CharField(max_length=255)
    publish_time = models.CharField(max_length=255)
    tie_num = models.IntegerField()
    doc_url = models.CharField(max_length=255)
    keywords = models.CharField(max_length=20)
    news_type = models.ForeignKey(NewsType, on_delete=models.CASCADE)

class NewsContent(models.Model):
    content = models.TextField()
    news = models.OneToOneField(News, on_delete=models.CASCADE)

