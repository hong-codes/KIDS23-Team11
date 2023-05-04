from django.db import models

question_types = (
	('general', 'general'),
	('biomedical', 'biomedical'),
	('-', '-')
)

model_types = (
	('chatGPT', 'chatGPT'),
	('AI21', 'AI21'),
	('OpenAssistant', 'OpenAssistant'),
	('BioGPT', 'BioGPT'),
	('-', '-')
)

rating_types = (
	(1, 'positive'),
	(0, 'neutral'),
	(-1, 'negative'),
)

class Question(models.Model):
	question_text = models.TextField(default='-')
	question_type =  models.CharField(choices=question_types, max_length=40, default='-')

class Answer(models.Model):
	answer_text = models.TextField(default='-')
	model_type =  models.CharField(choices=model_types, max_length=40, default='-')
	rating = models.IntegerField(choices=rating_types, default=0)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

class ScoreCard(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	chatGPT = models.IntegerField(null=True)
	AI21 = models.IntegerField(null=True)
	OpenAssistant = models.IntegerField(null=True)
	BioGPT = models.IntegerField(null=True)