from django.db import models

#Models help define what data is stored in the database. classes define tables, attributes define columns. Instances of a class represent rows in a table.
class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    notes = models.TextField(blank=True, null=True)

    #defines what is returned if the object is printed or output as text
    def __str__(self):
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Notes: {self.notes[:200]}'
