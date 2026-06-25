from django.db import models

class StudentInfoModel(models.Model):

  DEPT_TYPES = [
    ('cse', 'CSE'),
    ('eee', 'EEE'),
    ('civil', 'CIVIL'),
  ]
  name = models.CharField(max_length=200, null=True)
  email = models.EmailField()
  image = models.ImageField(upload_to='media/stdent_img')
  department = models.CharField(choices=DEPT_TYPES, max_length=10)

  def __str__(self):
    return f'{self.name}-{self.department}'
