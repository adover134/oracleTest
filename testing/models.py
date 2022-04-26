from django.db import models


class User(models.Model):
    u_id = models.CharField(max_length=10, primary_key=True)
    u_name = models.TextField()

    class Meta:
        db_table = "user"


class TestClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    test_id = models.IntegerField(primary_key=True)
    u_name = models.TextField()

    class Meta:
        db_table = "testing"
