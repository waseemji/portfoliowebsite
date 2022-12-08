from django.urls import path
from . import views
urlpatterns = [
   path("",views.HomePageView.as_view(),name="home"),
   path("about-me/",views.AboutPageView.as_view(), name = "about"),
   path("my-skills",views.SkillPageview.as_view(), name = "skills"),
   path("resume",views.ResumePageView.as_view(), name = "resume"),
   path("contact",views.ContactMePage.as_view(), name = "contact")
]
