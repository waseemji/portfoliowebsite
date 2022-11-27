from django.urls import path
from . import views

urlpatterns = [
    path("",views.BlogHomeView.as_view(), name="blog-home"),
    path("posts",views.AllPostView.as_view(),name="all-posts"),
    path("posts/<slug:slug>",views.SinglePostView.as_view(),name="detailed-post"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")
]
