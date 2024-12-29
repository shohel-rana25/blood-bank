from django.db import models

# Create your models here.

CHOICES=[
   
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-')
]

class Bloodlist(models.Model):
    Name = models.CharField(max_length=30)
    Last_Donate = models.DateField(null=True, blank=True)  # This should allow NULL values
    Phone = models.PositiveIntegerField()
    Location = models.CharField(max_length=40)
    Email = models.EmailField(max_length=30)
    Blood_Group = models.CharField(max_length=20, choices=CHOICES)
    Image = models.ImageField(upload_to='donor_images/', null=True, blank=True)

    def __str__(self):
        return self.Name
