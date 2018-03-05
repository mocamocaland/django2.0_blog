from django.db import models
from django.utils import timezone #djangoでは、datetime.nowのかわりに, timezon.nowで現在の日付・時刻を取得する


class Day(models.Model):
    # id = models.AutoField(primary_key=True) #自動で追加されてる 重複が許されない
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

