from django.db import models

class TeacherModel(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  email = models.EmailField()

  #TeacherModel object (1) for changing the object name
  def __str__(self):
    return f'{self.name}-{self.email}'
  
