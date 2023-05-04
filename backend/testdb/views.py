from asyncio import constants
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import Question, Answer, ScoreCard
from .serializers import QuestionSerializer, AnswerSerializer, ScoreCardSerializer

# Create your views here.

def home(request):
    # load GPCR data from GPCRdb Rest api query
    questions = Question.objects.all()
    # if (questions.count() == 0):
    #     load_questions()

    # load TGGA variant data from csv file
    answers = Answer.objects.all()
    # if (answers.count() == 0):
    #     load_answers()

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

@api_view(['POST'])
def post_new_question_answer(request):
    if request.method == 'POST':
        json_request = JSONParser().parse(request)
        question_text = json_request['text']
        question_type = json_request['type']
        question = Question.objects.get_or_create(question_text=question_text, question_type=question_type)
        chatGPT_score = None
        AI21_score = None
        OpenAssistant_score = None
        BioGPT_score = None
        answers = json_request['answers']
        for answer in answers:
            answer_text = answer['text']
            model_type = answer['type']
            score = None
            if (answer['score'] == 'positive'):
                score = 1
            elif (answer['score'] == 'neutral'):
                score = 0
            elif (answer['score'] == 'negative'):
                score = -1
            if(model_type == 'ChatGPT'):
                chatGPT_score = score
            elif(model_type == 'AI21'):
                AI21_score = score
            elif(model_type == 'OpenAssistant'):
                OpenAssistant_score = score
            elif(model_type == 'BioGPT'):
                BioGPT_score = score
            Answer.objects.get_or_create(answer_text=answer_text, model_type=model_type, rating=score, question=question[0])
        ScoreCard.objects.get_or_create(question=question[0], chatGPT=chatGPT_score, AI21=AI21_score, OpenAssistant=OpenAssistant_score, BioGPT=BioGPT_score)

    return Response({'saved':True}, content_type="application/json")