from django.db import models

# Create your models here.
class TestTable(models.Model):
    id = models.AutoField()
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'test_table'
