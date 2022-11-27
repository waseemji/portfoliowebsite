from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = "homepage/home.html"

class AboutPageView(TemplateView):
    template_name = "homepage/about.html"

class SkillPageview(TemplateView):
    template_name = "homepage/my-skills.html"

class ResumePageView(TemplateView):
    template_name = "homepage/resume.html"

class ContactMePage(TemplateView):
    template_name = "homepage/contact.html"