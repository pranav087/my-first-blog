from django.shortcuts import render

from .models import Post

def post_list(request):
    return render(request, 'blog/post_list.html',{})
def home(request):

    queryset=Post.objects.all()
    dta={
        "queryset":queryset
    }
    return render(request, 'blog/home.html', {})
