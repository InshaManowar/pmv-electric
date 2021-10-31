from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .models import Blog, STATUS_PUBLISH
from django.core.paginator import Paginator
from django.views import generic
# from newsletter.forms import SubscibersForm, MailMessageForm
from django.contrib import messages


class BlogList(generic.ListView):
    paginate_by = '6'
    queryset = Blog.objects.filter(status=STATUS_PUBLISH).order_by('-publish_date')
    template_name = 'blog/blog.html'
    context_object_name='posts'
    
class BlogDetails(generic.DetailView):
    model = Blog
    template_name= 'blog/detail.html'
    
def detail_view(request,slug):
    section = get_object_or_404(Blog, slug=slug)
    post = Blog.objects.filter(status=STATUS_PUBLISH).order_by('-publish_date')[0:5]
  
 
    return render(request, 'blog/detail.html', { 'section':section, 'post':post,})
