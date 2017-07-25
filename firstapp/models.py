from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    Title = models.CharField(max_length = 30)
    Location = models.CharField(max_length = 30)
    Trainer = models.CharField(max_length = 30)
    
    def _str_(self):
        return self.Title