from django.db import models

class User (models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=32, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    regiester_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    useremail = models.EmailField(max_length=128, verbose_name='이메일')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_info'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'