from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

#----discription model
class Discription(models.Model):
    name=models.CharField(max_length=100,verbose_name='توضیح')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'توضیح'
        verbose_name_plural = 'توضیحات'


#--------size model
class Size(models.Model):
    range=models.IntegerField(null=True,blank=True,verbose_name='اندازه')
    # slug=models.SlugField(default='',null=False,db_index=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.range)
    #     super().save(*args, **kwargs)
    def __int__(self):
        return self.range

    class Meta:
        verbose_name = 'اندازه'
        verbose_name_plural = 'اندازه ها'

#--------kind model
class Kind(models.Model):
    name=models.CharField(max_length=50,verbose_name='جنس رویه')
    slug=models.SlugField(default='',null=False,db_index=True,verbose_name='اسلاگ در url')
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'جنس رویه'
        verbose_name_plural = 'جنس های رویه'


class Shoe(models.Model):
    brand = models.CharField(max_length=30, verbose_name='برند')
    property=models.CharField(max_length=30,verbose_name='ویژگی')
    color=models.CharField(max_length=30,verbose_name='رنگ')
    production_date=models.DateField()
    kind=models.ForeignKey(Kind,on_delete=models.CASCADE,null=True,blank=True,verbose_name='جنس رویه')
    # price=models.DecimalField(max_digits=8,decimal_places=2,verbose_name='قیمت')
    price=models.IntegerField(null=True,blank=True,verbose_name='قیمت')
    discription=models.OneToOneField(Discription,on_delete=models.CASCADE,null=True,blank=True,verbose_name='توضیح')
    size=models.ManyToManyField(Size,verbose_name='اندازه')
    # speces=models.FileField(upload_to='files/shoes')
    photo=models.ImageField(upload_to='files/shoes',verbose_name='عکس')
    gender=models.CharField(max_length=10,verbose_name='جنسیت')
    slug=models.SlugField(default='',null=False,db_index=True,verbose_name='اسلاگ در url')




    def save(self,*args,**kwargs):
        self.slug=slugify(self.property+'_'+self.brand+'-'+self.color+'_'+self.gender)
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.property}-----{self.kind}----{self.discription}----{self.slug}'

    class Meta:
        verbose_name = 'کفش'
        verbose_name_plural = 'کفش ها'