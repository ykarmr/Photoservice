from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=150)
    comment = models.TextField(blank=True)
    #pip install Pillpw をしないとImageFieldは使えない
    image = models.ImageField(upload_to = 'photos')
    #第一引数 Userモデルと紐付け
    #on_delete 紐付けされたインスタンスが削除された時の挙動
    #models.CASCADE 全て削除

    category = models.ForeignKey(Category,on_delete=models.PROTECT)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
