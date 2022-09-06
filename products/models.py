from django.db import models
from datetime import datetime

class Products(models.Model):
    category=[
        ('phone','phone'),
        ('computer','computer'),
        ('screens','screens'),
    ]
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    content=models.TextField()
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    active=models.BooleanField(default=True)
    category=models.CharField(max_length=50,null=True,blank=True,choices=category)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='product'
        ordering =['-price']
        #ترتيب المنتجات 
        # - تعني الترتيب من الاعلي سعر 

class Test(models.Model):
    date=models.DateField()
    time=models.TimeField(null=True)
    created=models.DateTimeField(default=datetime.now)