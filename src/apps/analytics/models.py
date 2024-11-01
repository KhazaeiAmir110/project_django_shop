from django.contrib.admin.models import LogEntry


# class FootPrint(models.Model):
#     pass

class ActionHistory(LogEntry):
    class Meta:
        proxy = True
