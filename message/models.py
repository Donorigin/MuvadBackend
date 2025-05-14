from django.db import models

# Create your models here.


class Message(models.Model):
    SERVICE_CHOICES = [
        ('Estimating', 'Estimating'),
        ('ITBs',"ITBs"),
        ('Lead Resercher','Lead Researcher'),
        ('Full Package','Full Package'),
    ]

    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    project_details = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name} ({self.email})"


