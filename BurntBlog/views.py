from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Post, Image

def blog_main(_):
    template = loader.get_template("blog_index.html")
    return HttpResponse(template.render({ "posts": Post.objects.all().order_by("pub_date").reverse() }))

def post(_, id):
    template = loader.get_template("post.html")
    post = None
    try:
        post = Post.objects.get(uid=id)
    except ObjectDoesNotExist:
        pass
    except ValidationError:
        pass

    return HttpResponse(template.render({ "post" : post }))

def image(_, id):
    img = None

    try:
        img = Image.objects.get(uid=id)
    except ObjectDoesNotExist:
        pass
    except ValidationError:
        pass

    if img is None:
        return HttpResponseNotFound()

    image_data = None
    with open(img.content.path, 'rb') as f:
        image_data = f.read()

    response = HttpResponse(image_data, content_type=f"image/{img.content.path[img.content.path.rindex('.')+1:]}")
    response.headers['Cache-Control'] = "max-age=604800"
    return response
