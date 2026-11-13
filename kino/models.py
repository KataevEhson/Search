from django.db import models



class Ganr(models.Model):
    name = models.CharField()



class Film(models.Model):
    name = models.CharField()
    caption = models.CharField()
    photo = models.ImageField(upload_to='images/')
    ganr_id = models.ForeignKey(Ganr, on_delete=models.CASCADE)

class Comment(models.Model):
    author = models.CharField()
    text = models.CharField()
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
