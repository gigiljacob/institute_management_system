from django.db import models


class Contact(models.Model):
    name = models.CharField(verbose_name='Your name', max_length=100)
    email = models.EmailField(verbose_name='Your email')
    subject = models.CharField(verbose_name='Subject', max_length=100)
    message = models.TextField(verbose_name='message')
    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.name


class SocialProfile(models.Model):
    linked_in = models.URLField()
    insta = models.URLField()
    skype = models.URLField()
    fb = models.URLField()
    twitter_x = models.URLField()
    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return str(self.created_on)


class Resume(models.Model):
    file_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    resume_file = models.FileField(upload_to='media/resumes/')
    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return str(self.file_name)


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=13)
    social_profile = models.ForeignKey(SocialProfile, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return str(self.email)
