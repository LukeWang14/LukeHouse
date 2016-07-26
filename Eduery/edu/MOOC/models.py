from django.db import models
from django.utils import timezone

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50)
    email = models.EmailField()
    name = models.CharField(max_length=50,default="肖冬")
    school = models.CharField(max_length=50,default="清华大学")
    studentnum = models.CharField(max_length=50,default="2014013424")
    teachernum = models.CharField(max_length=50,default="2014013424")
    selfintroduction = models.CharField(max_length=400,default="这是我的个人简介")
    Type = models.CharField(max_length=50, default="student")
    StuProfession = models.CharField(max_length = 30, default="softwareengineering")
    TeaProfession = models.CharField(max_length = 30, default="softwareengineering")
    CourseList = models.ManyToManyField("Course")
    #针对学生教师和学校都可以用这个CourseList
    StuList = models.ManyToManyField("UserInfo")
    def __str__(self):
    	return self.username

class Category(models.Model):
    name = models.CharField(max_length=40, default = "")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/category/%u' % self.pk


class Course(models.Model):
	Name = models.CharField(max_length = 30, default="")
	InSchool = models.ForeignKey("UserInfo")
	Type = models.ForeignKey("Category")
	#1表示尚未开始，2表示正在进行，3表示已经结束
	ValidOrNot = models.IntegerField()
	Introduction = models.CharField(max_length =500, default = "")
	def __str__(self):
		return self.Name


class Chapter(models.Model):
	FromCourse = models.ForeignKey("Course")
	ChapterNum = models.IntegerField()
	ChapterName = models.CharField(max_length = 40, default = "")
	Introduction = models.CharField(max_length = 100, default = "")
	def __str__(self):
		return str(self.ChapterNum) + self.ChapterName



class Note(models.Model):
	FromStudent = models.ForeignKey("UserInfo")
	FromChapter = models.ForeignKey("Chapter")
	#有一个字符表示已经结束，待设定
	Title = models.CharField(max_length = 50, default = "")
	Content = models.CharField(max_length = 500, default = "")
	CreatedAt = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.Title

class Question(models.Model):
	FromStudent = models.ForeignKey("UserInfo")
	FromChapter = models.ForeignKey("Chapter")
	QuestionTitle = models.CharField(max_length = 50, default = "")
	QuestionContent = models.CharField(max_length = 500, default = "")
	CreatedAt = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.QuestionTitle


class Answer(models.Model):
	ToQuestion = models.ForeignKey("Question")
	FromTeacher = models.ForeignKey("UserInfo")
	FromChapter = models.ForeignKey("Chapter")
	AnswerContent = models.CharField(max_length = 1000, default = "")
	CreatedAt = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.ToQuestion.QuestionTitle


class Video(models.Model):
	FromChapter = models.ForeignKey("Chapter")
	VideoFile = models.FileField(upload_to = 'videos')


class Announcement(models.Model):
	FromChapter = models.ForeignKey("Chapter")
	AnnouncementContent = models.CharField(max_length = 50)
	CreatedAt = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.AnnouncementContent
