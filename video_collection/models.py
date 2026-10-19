from django.db import models
from urllib import parse
from django.core.exceptions import ValidationError

#Models help define what data is stored in the database. classes define tables, attributes define columns. Instances of a class represent rows in a table.
class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    notes = models.TextField(blank=True, null=True)
    video_id = models.CharField(max_length=40, unique=True)

    def save(self, *args, **kwargs):
        """Add additional functionality to the inherited django save function"""

        #raises error if the video's url doesn't start with the string passed to the startswith function
        if not self.url.startswith('https://www.youtube.com/watch'):
            raise ValidationError(f'Not a Youtube URL {self.url}')

        # extracts the video id from a youtube url
        url_components = parse.urlparse(self.url)
        query_string = url_components.query #v=123456
        #checks if url has a query string, else raises error
        if not query_string:
            raise ValidationError(f'Invalid YouTube URL {self.url}')
        parameters = parse.parse_qs(query_string,strict_parsing=True) #dictionary
        #checks the parameters dictionary for a key called 'v' and returns it's value, else returns none
        v_parameters_list = parameters.get('v') #return None if no key is found, e.g abc=1234

        #if v_parameters_list is falsy, raises error
        if not v_parameters_list: 
            raise ValidationError(f'Invalid YouTube URL, missing parameters {self.url}')

        #sets video objects video_id attribute equal to the returned string
        self.video_id = v_parameters_list[0] #string

        #calls django's built in save method
        super().save(*args, **kwargs)
            
    #defines what is returned if the object is printed or output as text
    def __str__(self):
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Video ID: {self.video_id},Notes: {self.notes[:200]}'
