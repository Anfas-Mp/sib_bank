from django.db import models

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    link=models.CharField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='district'
        verbose_name_plural='districts'

    def __str__(self):
        return '{}'.format(self.name)

class Branch(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=250,unique=True)
    area=models.CharField(max_length=250,unique=True)

    class Meta:
        ordering=('area',)
        verbose_name='branch'
        verbose_name_plural='branches'

    def __str__(self):
        return '{}'.format(self.area)

class Person(models.Model):
    GENDER_CHOICES = [

        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    name=models.CharField(max_length=250,unique=True)
    dob=models.DateField(null=True,blank=True)
    age=models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=200, null=True)
    phoneno = models.CharField(max_length=250,unique=True)
    email=models.CharField(max_length=250,unique=True)
    address = models.TextField()
    district=models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    area=models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)
