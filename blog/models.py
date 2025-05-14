from django.db import models

# Create your models here.



class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('estimating', 'Estimating'),
        # Add more categories as needed
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog-images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    time_to_read = models.CharField(max_length=20)  # e.g., "4 min read"
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title