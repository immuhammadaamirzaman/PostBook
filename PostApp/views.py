from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView


def home(request): 
    return render(request,'PostApp/home.html',{'posts':Post.objects.all()})

class PostListView(ListView):
    model=Post
    context_object_name='posts' #this is object that will iteratre by default in listview it uses object var to iterate
    ordering=['-date_posted']
    template_name='PostApp/home.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self,form):#override form_valid 
        form.instance.author=self.request.user #setting the author as the current logged in 
        return super().form_valid(form) #running this method over parent class


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def test_func(self):#this func will check if the user is valid to perform an action
        post=self.get_object() #get the post on which action needs to be 
        if self.request.user==post.author:#checking if the author of post if same
            return True
        return False

class PostDetailView(DetailView):
    model=Post


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False