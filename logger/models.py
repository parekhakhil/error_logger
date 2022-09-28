from django.db import models

# Create your models here.


class Error(models.Model):
    status_code = models.IntegerField()
    request = models.URLField(max_length=255, null=True, blank=True)
    method = models.CharField(max_length=10, null=True, blank=True)
    error = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} -- {1}".format(str(self.status_code), self.method)

