from django.shortcuts import render
from django import forms
from MOOC.models import *
from MOOC.admin import *
from MOOC.forms import *

def note_list(request):
	params = request.POST if request.method == 'POST' else None
	noteform = NoteForm(params)
	if noteform.is_valid():
		note = noteform.save(commit=False)

		username = request.user.username
		user = UserInfo.objects.filter(username__exact=username)
		note.FromStudent = user[0]

		chapter = Chapter.objects.filter(ChapterName__exact="introduction")
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

		chapter = Chapter.objects.filter(ChapterName__exact="introduction")
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

		chapter = Chapter.objects.filter(ChapterName__exact="introduction")
		answer.FromChapter = chapter[0]
		answer.save()
		answerform = AnswerForm()
	answers = Answer.objects.all()

	return render(request, 'video.html', {'notes': notes, 'noteform' : noteform, 'questions': questions, 'questionform' : questionform, 'answers': answers, 'answerform': answerform})



