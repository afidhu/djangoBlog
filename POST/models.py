from django.db import models
from ACCOUNT.models import Users, Profile


# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(Users, on_delete=models.CASCADE)
    title=models.CharField(max_length=100, null=True, blank=True)
    image=models.ImageField(max_length=100, upload_to='photo/', null=True, blank=True)
    video=models.FileField(max_length=100, upload_to='video/')
    content=models.TextField(blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
    
    
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField()
    
    def __str__(self) -> str:
        return f'{self.post} => {self.content}'
    
    
class Follow(models.Model):
    follower=models.ForeignKey(Users,on_delete=models.DO_NOTHING, related_name='follower+')
    followee=models.ForeignKey(Users,on_delete=models.DO_NOTHING, related_name='followee+')
    
    def __str__(self):
        return f'{self.follower} => {self.followee}'
    