from django.contrib import admin

from bio.models import Contact, Profile, Resume, SocialProfile


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on', 'subject')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')


@admin.register(SocialProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('linked_in', 'insta', 'skype', 'fb', 'twitter_x')


@admin.register(Resume)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'company', 'resume_file')
