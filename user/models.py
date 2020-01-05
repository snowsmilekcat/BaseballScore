from django.conf import settings
from django.db import models
from django.utils import timezone

class User(models.Model):
    POSITION_CHOICES = [
    ('1', 'ピッチャー'),
    ('2', 'キャッチャー'),
    ('3', 'ファースト'),
    ('4', 'セカンド'),
    ('5', 'サード'),
    ('6', 'ショート'),
    ('7', 'レフト'),
    ('8', 'センター'),
    ('9', 'ライト'),
    ]

    class Meta:
        ordering = ['-id']

    name = models.CharField(max_length=50)
    back_number = models.IntegerField(default=0)
    #position = models.CharField(max_length=1,choices=POSITION_CHOICES)
    #sub_position = models.CharField(max_length=1,choices=POSITION_CHOICES)
    position = models.CharField(max_length=1)
    sub_position = models.CharField(max_length=1)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):#Admin画面のタイトルにする項目の指定。無くてもよい。
        return self.name
