from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from MOOC.models import *
from MOOC.admin import *
from MOOC.forms import *
from MOOC.login import *

def course_show(request, course_id):
	course = Course.objects.get(pk=course_id)
	username = request.user.username
	user = UserInfo.objects.get(username__exact=username)
	if user:
		courseforuser = user.CourseList.all().filter(pk = course.pk)
	else:
		onecourseforuser = UserInfo()
		courseforuser = [onecourseforuser]
	chapters = Chapter.objects.all()
	return render(request, 'courseIntro.html', {'user': user, 'course': course, 'chapters': chapters, 'courseforuser': courseforuser})

def course_in(request, course_id):
	if not request.user.is_authenticated(): 
		return HttpResponseRedirect('/login/')

	params = request.POST if request.method == 'POST' else None
	announcementform = AnnouncementForm(params)
	if announcementform.is_valid():
		announcement = announcementform.save(commit=False)
		chapter = Chapter.objects.filter(pk = chapter_id)
		announcement.FromChapter = chapter[0]
		announcement.save()
		announcementform = AnnouncementForm()


	course = Course.objects.get(pk=course_id)
	announcements = Announcement.objects.filter(FromCourse__pk = course_id)
	if len(announcements) == 0:
		blankannouncement = Announcement()
		blankannouncement.FromCourse = course
		blankannouncement.save()
		announcements = Announcement.objects.filter(FromCourse__pk = course_id)
		announcement = announcements[len(announcements) - 1]
	else:
		announcement = announcements[len(announcements) - 1]


	username = request.user.username
	user = UserInfo.objects.filter(username__exact=username)
	courseforuser = user[0].CourseList.all().filter(pk = course.pk)
	if not courseforuser:
		user[0].CourseList.add(course)
	courseforuser = user[0].CourseList.all().filter(pk = course.pk)

	params = request.POST if request.method == 'POST' else None
	chapterform = ChapterForm(params)
	if chapterform.is_valid():
		chapter = chapterform.save(commit=False)

		username = request.user.username
		user = UserInfo.objects.filter(username__exact=username)

		chapter.save()
		chapterform = ChapterForm()
	chapters = Chapter.objects.all()
	return render(request, 'school_video.html', {'course': course, 'chapters': chapters, 'announcement': announcement, 'announcementform': announcementform})


def chapter_list(request, course_id, chapter_id):
	if not request.user.is_authenticated(): 
		return HttpResponseRedirect('/login/')
	params = request.POST if request.method == 'POST' else None
	noteform = NoteForm(params)
	if noteform.is_valid():
		note = noteform.save(commit=False)

		username = request.user.username
		user = UserInfo.objects.filter(username__exact=username)
		note.FromStudent = user[0]

		chapter = Chapter.objects.filter(pk=chapter_id)
		note.FromChapter = chapter[0]
		note.save()
		noteform = NoteForm()
	notes = Note.objects.all()

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
		answer.FromStudent = user[0]

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

	course = Course.objects.get(pk=course_id)
	announcements = Announcement.objects.filter(FromCourse__pk = course_id)
	if len(announcements) == 0:
		blankannouncement = Announcement()
		blankannouncement.FromCourse = course
		blankannouncement.save()
		announcements = Announcement.objects.filter(FromCourse__pk = course_id)
		announcement = announcements[len(announcements) - 1]
	else:
		announcement = announcements[len(announcements) - 1]
	chapter = Chapter.objects.get(pk=chapter_id)

	return render(request, 'school_video.html', {'notes': notes, 'noteform' : noteform, 'questions': questions, 'questionform' : questionform, 'answers': answers, 'answerform': answerform, 'course':course, 'chapters':chapters, 'chapterform': chapterform, 'chapter' : chapter, 'announcement': announcement, 'announcementform': announcementform})


def course_delete(request, course_id):
	course = Course.objects.get(pk=course_id)
	username = request.user.username
	user = UserInfo.objects.get(username__exact=username)
	courseforuser = user.CourseList.all().filter(pk = course.pk)
	courseforuser[0].delete()

	if not request.user.is_authenticated(): 
		return HttpResponseRedirect('/login/')
	username = request.user.username
	user = UserInfo.objects.filter(username__exact=username)
	if user:
		courseforuser = user[0].CourseList.all()
	return render(request, 'homepage/homepageschool.html', {'user': user, 'courseforuser': courseforuser})

