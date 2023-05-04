from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionsViewSet)
router.register(r'answers', views.AnswersViewSet)
router.register(r'scorecard', views.ScoreCardViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/post_question_answer/', views.post_new_question_answer, name='post_question_answer'),
]