from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    schemas = Articles.objects.order_by('schema')
    return render(request, 'news/news_home.html', {'schemas': schemas})

class NewsDetailView(DetailView):
    model = Articles
    context_object_name = 'article'
    template_name = 'news/detail_view.html'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news-delete.html'
    success_url = '/news'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Форма заполнена некорректно!"

    form = ArticlesForm()
    data = {'form': form, 'error': error}
    return render(request, 'news/create.html', data)