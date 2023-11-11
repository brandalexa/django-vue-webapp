from django.db import models

class Event(models.Model):
    description = models.TextField(max_length=1000)
    date = models.DateTimeField("date and time of event")
    cancelled = models.BooleanField("event is cancelled", default=False)
    max_attendees = models.IntegerField()

    def __str__(self):
        return self.description
    