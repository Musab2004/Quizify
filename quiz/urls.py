from django.urls import path
from . import views

urlpatterns = [
    path('quiz-page', views.view_pdf, name='view_pdf'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('take-quiz/', views.your_view, name='take_quiz'),
    path('about-us/', views.about_us, name='about_us'),
    path('', views.homepage, name='homepage'),
]