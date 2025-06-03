from django.db import models
from uuid import uuid4

class Post(models.Model):
    uid = models.UUIDField("Post UUID", primary_key=True, default=uuid4, unique=True, editable=False)
    title = models.CharField("Post Title")
    content = models.TextField("Post Content")
    pub_date = models.DateTimeField("Date", auto_now=True)
