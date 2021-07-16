from django.db import models

# table -> Post(id, title, body, date)


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True)

    def __str__(self):
        # "id is {id}, title is {title}, body is {body}".format(id=self.id, title=self.title, body=self.body)
        return self.title
