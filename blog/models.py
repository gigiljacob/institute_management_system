from django.db import models


class Category(models.Model):
    property = models.CharField(max_length=100)
    level = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)


class BlogContents(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, models.CASCADE, related_name='category')
    sub_category = models.ForeignKey(Category, models.CASCADE, related_name='sub_category')
    sub_text = models.TextField()
    img_link = models.URLField()
    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.title
