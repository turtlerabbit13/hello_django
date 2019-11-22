from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = "home.html"
	
	def get_context_data(self):
		data ={
				"message_title": "Yahoo",
				"message_content": "Django is great!"
			  }
		return data

class About (TemplateView):
	template_name = "about.html"
	
	
