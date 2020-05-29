from django.db.models import Count

from post.models import *


def getRightInfo(request):
    # 1. 获取分类信息(按照catagory__c_name或者catagory进行分类
    r_catepost = Post.objects.values('catagory__c_name','catagory').annotate(c=Count('*')).order_by('-c')

    # 2. 近期文章
    r_repost = Post.objects.all().order_by('-created')[:3]

    # 3： 获取日期归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select DATE_FORMAT(created,'%Y%m%d') time,count('*') c from t_post GROUP BY time ORDER BY c desc,time desc")
    r_filepost = cursor.fetchall()

    return {'r_catepost': r_catepost, 'r_repost': r_repost,'r_filepost':r_filepost}