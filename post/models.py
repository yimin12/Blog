from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    c_name = models.CharField(max_length=30,unique=True,verbose_name=u'类别名称')
    class Meta:
        db_table = 't_catagory'
        verbose_name_plural= u'类别'
    def __str__(self):
        return u'Catatory:%s'%self.c_name

class Tag(models.Model):
    t_name = models.CharField(max_length=30,unique=True,verbose_name=u'标签签名')
    class Meta:
        db_table = 't_tag'
        verbose_name_plural = u'标签'
    def __str__(self):
        return u'Tag:%s'%self.t_name

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True,blank=True)
    created = models.DateTimeField(auto_created=True) # 自动创建时间
    catagory = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_post'
        verbose_name_plural = u'帖子'
    def __str__(self):
        return u'Post:%s'%self.title