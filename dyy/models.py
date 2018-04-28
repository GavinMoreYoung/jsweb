from django.db import models
from tinymce.models import HTMLField
class DyClass(models.Model):
    classname = models.CharField('类别名称',max_length=10)
    def __str__(self):
        return  self.classname

class Dy(models.Model):
    dytp = models.ImageField('电影图片',upload_to='pic/%Y/%m/%d')
    dybt = models.CharField('电影标题',max_length=10)
    dyclass = models.ForeignKey('DyClass',on_delete=models.CASCADE,verbose_name='电影类别')
    dydz = models.CharField('电影地址',max_length=200)
    def __str__(self):
        return self.dybt

class Wz(models.Model):
    wzbt = models.CharField('文章标题',max_length=20)
    wznr = HTMLField()
    def __str__(self):
        return self.wzbt