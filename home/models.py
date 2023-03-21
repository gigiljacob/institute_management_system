from django.db import models

class Contact(models.Model):
    """Details of the contacts would be stored into this model."""
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    message = models.TextField()

    def __str__(self) -> str:
        return str(self.name)
