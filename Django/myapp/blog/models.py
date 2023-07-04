from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
# Post와 Comment의 관계 1:N, User와 Post의 관계 1:N 시각화하기!!
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # 지금 이 포스트가 생성이 될 때, 자동으로 지금 시간 자체를 사용하겠다.
    updated_at = models.DateTimeField(auto_now=True) # 업데이트나 수정이 될 때, 그 시간을 저장함

# Class는 2칸이상 띄워라 (관용적)
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content


class HashTag(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name