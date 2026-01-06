from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('submit/<int:course_id>/', views.submit, name='submit'), # Changed to match view
    path('result/<int:submission_id>/', views.show_exam_result, name='show_exam_result'), # Fixed per rubric
]
