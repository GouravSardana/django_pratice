from django.db import models

class Slider(models.Model):
	title=models.ImageField(blank=True, null=True,  upload_to='media/%y/%m/%D/')


class Features(models.Model):
	title=models.CharField(max_length=200)
	content=models.TextField(max_length=200)
	icons=models.CharField(max_length=20)


class Banner(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField(max_length=100)
	button=models.CharField(max_length=10)
class FirstFeature(models.Model):
	title=models.CharField(max_length=200)
	content=models.TextField(max_length=500)