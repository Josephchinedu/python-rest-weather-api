from django.db import models

DESCRIPTIONS =(
    (0, "Sunny"),
    (1, "Rain"),
    (2, "Cloudy"),
    (3, "Snow")
)
# Create your models here.
class Description(models.Model):
    """ 
    Model to describe the weather
    """

    weather_description = models.IntegerField(choices=DESCRIPTIONS)
    temperature = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return (self.created_on)
    
