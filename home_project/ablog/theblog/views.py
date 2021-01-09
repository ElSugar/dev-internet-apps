from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
  model = Post
  template_name = 'home.html'
  ordering = ['-date']

  def get_context_data(self, *args, **kwargs):
    cat_menu = Category.objects.all()
    context = super(HomeView, self).get_context_data(*args, **kwargs)
    context['cat_menu'] = cat_menu
    return context

class ArticleDetailView(DetailView):
  model = Post
  template_name = 'article_details.html'

class AddPostView(CreateView):
  model = Post
  form_class = PostForm
  template_name = 'create_post.html'

class UpdatePostView(UpdateView):
  model = Post
  form_class = EditForm
  template_name = 'update_post.html'

class DeletePostView(DeleteView):
  model = Post
  template_name = 'delete_post.html'
  success_url = reverse_lazy('home')

def CategoryListView(request):
  cat_menu_list = Category.objects.all()
  return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
  category_posts = Post.objects.filter(category=cats.replace('-', ' '))
  return render(request, 'categories.html', {'cats':cats.replace(' ', '-'), 'category_posts':category_posts})

class AddCategoryView(CreateView):
  model = Category
  template_name = 'add_category.html'
  fields = '__all__'