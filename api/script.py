from os import system
import sys
from time import sleep
from random import randint
for _ in range(int(sys.argv[1])):
    rand=randint(int(sys.argv[2]),int(sys.argv[3]))
    with open('./model.py','a') as f:
        for _ in range(rand):
            f.write(""" from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    # likes = models.ForeignKey(User,on_delete=models.CASCADE)
    poster= models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['created_at']

class Like(models.Model):
    liker = models.ForeignKey(User,on_delete=models.CASCADE)
    post  = models.ForeignKey(Post,on_delete=models.CASCADE) """)
        f.write('""" --IM_ES_N """\n')
    system('git add .')
    system('git commit -m "an commit"')
    system('git push')
    sleep(3)