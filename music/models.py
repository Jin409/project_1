from django.db import models

TYPE_CHOICES = (
    #첫번쨰는 모델에서 받아들이는, 두번째는 실제로 models.py 작성시에 뜨는
    ('rain','비가 오는 날에'),
    ('sunny','봄이 느껴지는 날에'),
    ('christmas','크리스마스의 기분을 느끼고 싶은 날에'),
    ('midnight','조용한 새벽 공기에')
)

class Song(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    songtitle = models.CharField(max_length=30)
    songwriter = models.CharField(max_length=30)
    lyrics = models.TextField()
    writer = models.CharField(null=True,max_length=30)
    recommendation = models.CharField(null=True, max_length=200, choices = TYPE_CHOICES)
    video = models.CharField(null=True,max_length=100000)

    def __str__(self):
        return self.songtitle
    def summary(self):
        return self.lyrics[:300]
    def srtvid(self):
        return self.video[17:]
    def srtsong(self):
        return self.songtitle.lower()[0]
   
        
CHOICE=(
     ('good','추천해요!'),
    ('bad','아쉬워요!')
)
   
EMOJI = (
    ('cat','🐈'),
    ('dog','🐶'),
    ('good','👍🏻'),
    ('happy','😁'),
    ('heart','💜'),
    ('cool','😎')
)
class Comment(models.Model):
    post = models.ForeignKey(Song,null=False,on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    text = models.TextField()
    opinion = models.CharField(max_length=30, choices = CHOICE)
    icon = models.CharField(max_length=30,null=False, choices = EMOJI)
    def __str__(self):
        if self.opinion=="good":
            return "추천해요!"
        else:
            return "아쉬워요!"
