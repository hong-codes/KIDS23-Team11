from asyncio import constants
from django.shortcuts import render
import requests
import csv
from rest_framework import viewsets
from .models import Question, Answer, ScoreCard
from .serializers import QuestionSerializer, AnswerSerializer, ScoreCardSerializer

# Create your views here.

def home(request):
	# load GPCR data from GPCRdb Rest api query
	questions = Question.objects.all()
	# if (questions.count() == 0):
	# 	load_questions()

	# load TGGA variant data from csv file
	answers = Answer.objects.all()
	# if (answers.count() == 0):
	# 	load_answers()

	return render(request, 'home.html', {'questions': questions, 'answers': answers})

class QuestionsViewSet(viewsets.ModelViewSet):
	"""
    API endpoint that shows protein families.
    """
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

class AnswersViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that shows protein families.
	"""
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

class ScoreCardViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that shows protein families.
	"""
	queryset = ScoreCard.objects.all()
	serializer_class = ScoreCardSerializer