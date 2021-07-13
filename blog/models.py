from django.db import models

# table -> Post(id, title, body, date)
class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  date = models.DateField(auto_now_add=True)
