from django.db import models
# import MySQLdb

# # MySQL에 연결
# conn = MySQLdb.connect(host='localhost', user='your_username', password='your_password', database='your_database')

# # 커서 생성
# cursor = conn.cursor()

# # SQL 쿼리 실행
# cursor.execute('SELECT * FROM your_table')

# # 결과 가져오기
# results = cursor.fetchall()

# # 결과 출력
# for row in results:
#     print(row)

# # 연결 종료
# conn.close()

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField()
    userid = models.CharField(verbose_name='id', max_length=15)
    password = models.CharField(verbose_name='비밀번호', max_length=15)
    nickname = models.CharField(verbose_name='닉네임', max_length=15)

class Post(models.Model):
    post_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='제목', max_length=50)
    content = models.TextField(verbose_name='내용')
    date = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    like = models.IntegerField(verbose_name='좋아요', default=0)

class Comment(models.Model):
    comment_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    content = models.TextField(verbose_name='내용')
    like = models.IntegerField(verbose_name='좋아요', default=0)