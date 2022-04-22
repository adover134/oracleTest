from django.db import models


class User(models.Model):
    u_id = models.CharField(max_length=10, primary_key=True)
    u_name = models.TextField()

    class Meta:
        db_table = "user"