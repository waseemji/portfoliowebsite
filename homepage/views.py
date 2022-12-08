from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm
# Create your views here.

class HomePageView(TemplateView):
    template_name = "homepage/home.html"

class AboutPageView(TemplateView):
    template_name = "homepage/about.html"

class SkillPageview(TemplateView):
    template_name = "homepage/my-skills.html"

class ResumePageView(TemplateView):
    template_name = "homepage/resume.html"

class ContactMePage(FormView):
    form_class = ContactForm
    template_name = "homepage/contact.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)