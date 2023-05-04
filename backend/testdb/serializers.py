from .models import Question, Answer, ScoreCard
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text', 'question_type']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer_text', 'model_type', 'rating', 'question']

class ScoreCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScoreCard
        fields = ['question', 'chatGPT', 'AI21', 'OpenAssistant', 'BioGPT']