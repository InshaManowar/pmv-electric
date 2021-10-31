from django.db import models
from django.db.models.base import Model
from django.db.models.fields import NullBooleanField, SlugField


STATUS_DRAFT = 0
STATUS_PUBLISH = 1

STATUS = (
    (STATUS_DRAFT, "Draft"),
    (STATUS_PUBLISH, "Publish")
)

STATUS_ONE= (
    (STATUS_DRAFT, "Draft"),
    (STATUS_PUBLISH, "Publish")
)





def upload_here(instance, filename, *kwargs):
	file_path = '{filename}'.format(filename=filename)
	return file_path


class Blog(models.Model):
    bloglist = models.IntegerField(primary_key=True, null=False, blank=False, default=0)
    title = models.CharField(max_length=250, blank=False)
    snippet = models.TextField(default='')
    content = models.TextField(default='')
    author = models.CharField(default=None, max_length=100)
    author_designation = models.TextField(default=None, max_length=100)
    publish_date=models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.IntegerField(choices=STATUS, default=0)
    image_main = models.FileField(upload_to=upload_here, blank=False, null=True)


    def __str__(self):
        return self.title + '|' + str(self.author)
    

class BlogComment(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email =models.EmailField(default='', null=False, blank=False)
    body=models.TextField()
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s = %s' % (self.blog.title, self.name)

