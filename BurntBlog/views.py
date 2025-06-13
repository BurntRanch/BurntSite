from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Post

def blog_main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render({ "posts": Post.objects.all().order_by("pub_date").reverse() }))

def post(request, id):
    template = loader.get_template("post.html")
    post = None
    try:
        post = Post.objects.get(uid=id)
    except ObjectDoesNotExist:
        pass
    except ValidationError:
        pass

    return HttpResponse(template.render({ "post" : post }))
