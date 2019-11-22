from django.urls import path
from hello_django_app.views import About

urlpatterns = [
	path('about/', About.as_view(), name="about_page"),
]
# from django.urls import path

# from hello_django_app.views import AboutPageView
# urlpatterns = [

#     path('about/', AboutPageView.as_view()),
# ]