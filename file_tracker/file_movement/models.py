from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.

class file_movement(models.Model):
    Date = models.DateTimeField(auto_now=False)
    File_number = models.IntegerField(default=1234)
    Project_title = models.CharField(max_length=200)
    Proponent = models.CharField(max_length=50)
    Project_location = models.CharField(max_length=100)
    # Document_upload = models.FileField(upload_to='media', max_length=150,
    #   validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])])

    Action = models.CharField(max_length=100)

    def __str__(self):
        return self.Project_title

"""class staff(models.Model):
    staff_name = models.CharField(max_length=500)
    staff_designation = models.CharField(max_length=200)
    staff_email = models.CharField(max_length=300)
    staff_division = models.CharField(max_length=200) """