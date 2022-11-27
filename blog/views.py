from django.shortcuts import render
from .models import BlogPost
from .forms import CommentForm

from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


class BlogHomeView(ListView):
    template_name = "blog/blog-home.html"
    model = BlogPost
    ordering = ["-date"]
    context_object_name = "posts"

    # def get_queryset(self): ??

class AllPostView(ListView):
    template_name = "blog/all-posts.html"
    model = BlogPost
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):

    def saved_to_read_later(self,request,post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            saved_to_read_later = True
        else:
            saved_to_read_later = False
        return saved_to_read_later

    def get(self,request,slug):
        post = BlogPost.objects.get(slug=slug)

        context = {
            "post":post,
            "tags":post.tag.all(),
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("id"),
            "saved_to_read_later":self.saved_to_read_later(request,post.id)
        }

        return render(request,"blog/detailed-post.html",context)

    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = BlogPost.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("detailed-post",args=[slug]))

        context = {
            "post":post,
            "tags":post.tag.all(),
            "comment_form":comment_form,
            "comments":post.comments.all().order_by("-id"),
            "saved_to_read_later":self.saved_to_read_later(request,post.id)
        }

        return render(request,"blog/detailed-post.html",context)

class ReadLaterView(View):
    def get(self,request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = BlogPost.objects.filter(id__in = stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request,"blog/read-later.html",context)

    def post(self,request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        
        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/blog")