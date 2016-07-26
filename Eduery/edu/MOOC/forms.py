from django import forms 
from .models import *

class NoteForm(forms.ModelForm): 
	class Meta: 
		model = Note
		fields = ('Title', 'Content')


class QuestionForm(forms.ModelForm): 
	class Meta: 
		model = Question
		fields = ('QuestionTitle', 'QuestionContent')


class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('AnswerContent',)


class ChapterForm(forms.ModelForm):
	class Meta:
		model = Chapter
		fields = ('ChapterNum', 'ChapterName')

class AnnouncementForm(forms.ModelForm):
	class Meta:
		model = Announcement
		fields = ('AnnouncementContent', )