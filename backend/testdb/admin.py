from django.contrib import admin
from .models import Question, Answer, ScoreCard

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'question_type']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'model_type', 'rating', 'question']

class ScoreCardAdmin(admin.ModelAdmin):
    list_display = ['question', 'chatGPT', 'AI21', 'OpenAssistant', 'BioGPT']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(ScoreCard, ScoreCardAdmin)
