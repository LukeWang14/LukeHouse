from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from MOOC.models import *
from MOOC.admin import *
from MOOC.forms import *
from MOOC.login import *

def course_in(request, course_id):
	course = Course.objects.get(pk=course_id)
	chapters = Chapter.objects.all()

	params = request.POST if request.method == 'POST' else None
	announcementform = AnnouncementForm(params)
	if announcementform.is_valid():
		announcement = announcementform.save(commit=False)
		chapter = Chapter.objects.filter(pk = chapter_id)
		announcement.FromChapter = chapter[0]
		announcement.save()
		announcementform = AnnouncementForm()

	announcements = Announcement.objects.all()
	announcement = announcements[len(announcements) - 1]

	return render(request, 'teacher_video.html', {'course': course, 'chapters': chapters, 'announcement': announcement, 'announcementform': announcementform})


def chapter_list(request, course_id, chapter_id):
	params = request.POST if request.method == 'POST' else None


	questionform = QuestionForm(params)
	if questionform.is_valid():
		question = questionform.save(commit=False)

		username = request.user.username
		user = UserInfo.objects.filter(username__exact=username)
		question.FromStudent = user[0]

		chapter = Chapter.objects.filter(pk = chapter_id)
		question.FromChapter = chapter[0]
		question.save()
		questionform = QuestionForm()
	questions = Question.objects.all()

	answerform = AnswerForm(params)
	if answerform.is_valid():
		answer = answerform.save(commit=False)

		username = request.user.username
		user = UserInfo.objects.filter(username__exact=username)
		answer.FromTeacher = user[0]

		chapter = Chapter.objects.filter(pk = chapter_id)
		answer.FromChapter = chapter[0]

		answer.save()
		answerform = AnswerForm()
	answers = Answer.objects.all()


	params = request.POST if request.method == 'POST' else None
	chapterform = ChapterForm(params)
	if chapterform.is_valid():
		chapter = chapterform.save(commit=False)

		username = request.user.username
		user = UserInfo.objects.filter(username__exact=username)
		chapter.FromStudent = user[0]

		chapter.save()
		chapterform = ChapterForm()
	chapters = Chapter.objects.all()

	announcementform = AnnouncementForm(params)
	if announcementform.is_valid():
		announcement = announcementform.save(commit=False)
		chapter = Chapter.objects.filter(pk = chapter_id)
		announcement.FromChapter = chapter[0]
		announcement.save()
		announcementform = AnnouncementForm()

	announcements = Announcement.objects.all()
	announcement = announcements[len(announcements) - 1]


	course = Course.objects.get(pk=course_id)
	chapter = Chapter.objects.get(pk=chapter_id)

	return render(request, 'teacher_video.html', {'questions': questions, 'questionform' : questionform, 'answers': answers, 'answerform': answerform, 'course':course, 'chapters':chapters, 'chapterform': chapterform, 'chapter' : chapter, 'announcementform': announcementform, 'announcement': announcement})



def question(request, course_id, chapter_id, question_id):
	params = request.POST if request.method == 'POST' else None

	questionform = QuestionForm(params)
	if questionform.is_valid():
		question = questionform.save(commit=False)

		username = request.user.username
		user = UserInfo.objects.filter(username__exact=username)
		question.FromStudent = user[0]

		chapter = Chapter.objects.filter(pk = chapter_id)
		question.FromChapter = chapter[0]
		question.save()
		questionform = QuestionForm()
	questions = Question.objects.all()
	question = Question.objects.get(pk = question_id)

	answerform = AnswerForm(params)
	if answerform.is_valid():
		answer = answerform.save(commit=False)

		username = request.user.username
		user = UserInfo.objects.filter(username__exact=username)
		answer.FromTeacher = user[0]

		chapter = Chapter.objects.filter(pk = chapter_id)
		answer.FromChapter = chapter[0]

		answer.ToQuestion = question

		answer.save()
		answerform = AnswerForm()
	answers = Answer.objects.all()


	params = request.POST if request.method == 'POST' else None
	chapterform = ChapterForm(params)
	if chapterform.is_valid():
		chapter = chapterform.save(commit=False)

		username = request.user.username
		user = UserInfo.objects.filter(username__exact=username)
		chapter.FromStudent = user[0]

		chapter.save()
		chapterform = ChapterForm()
	chapters = Chapter.objects.all()

	announcementform = AnnouncementForm(params)
	if announcementform.is_valid():
		announcement = announcementform.save(commit=False)
		chapter = Chapter.objects.filter(pk = chapter_id)
		announcement.FromChapter = chapter[0]
		announcement.save()
		announcementform = AnnouncementForm()

	announcements = Announcement.objects.all()
	announcement = announcements[len(announcements) - 1]

	course = Course.objects.get(pk=course_id)
	chapter = Chapter.objects.get(pk=chapter_id)

	return render(request, 'teacher_question.html', {'questions': questions, 'questionform' : questionform, 'answers': answers, 'answerform': answerform, 'course':course, 'chapters':chapters, 'chapterform': chapterform, 'chapter' : chapter, 'question': question, 'announcement': announcement, 'announcementform': announcementform})