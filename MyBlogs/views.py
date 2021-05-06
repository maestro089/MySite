from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import UpdateView, DeleteView

from .forms import CreateForm
from .models import Blog


def index(request):
    latest_blog_list = Blog.objects.order_by('-pub_date')[:10]
    template = loader.get_template('MyBlogs/Index.html')
    context = {
        'latest_blog_list': latest_blog_list,
    }
    return render(request, 'MyBlogs/index.html', context)

def detail(request, Blog_id):
    try:
        blog = Blog.objects.get(pk=Blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request, 'MyBlogs/detail.html', {'blog': blog})


def create(request):
    error =''
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('MyBlogs:success_saved'))
        else:
            error = 'Wrong form filling'

    form = CreateForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'MyBlogs/create.html', data)


def success_saved(request):
    return render(request, 'MyBlogs/success_saved.html')


class Update(UpdateView):
    model = Blog
    pk_url_kwarg = "Blog_id"
    template_name = 'MyBlogs/update.html'
    form_class = CreateForm


class Delete(DeleteView):
    model = Blog
    pk_url_kwarg = "Blog_id"
    success_url = '/MyBlogs/'
    template_name = 'MyBlogs/delete.html'
