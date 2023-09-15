from django.db import models


class Contact(models.Model):
    name = models.CharField(verbose_name='Your name', max_length=100)
    email = models.EmailField(verbose_name='Your email')
    subject = models.CharField(verbose_name='Subject', max_length=100)
    message = models.TextField(verbose_name='message')
    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.name
