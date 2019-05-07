from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .form  import ContactForm
from blog.models import BlogPost




def homepage(request):
    my_title = "welcome to my first django"

    qs = BlogPost.objects.all()[:5]
    context = {"title":my_title,'blog_post':qs}

    return  render(request,"home.html",context)

def about(request):
    return  render(request,"about.html",{'title':'about us'})

def contact(request):
    # print(request.POST) ##可以看見submit後的東西

    ##類似print(request.post)只是這裡是透過寫在form.py達成
    form  = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm() #讓輸入完submit後可以清空文字方塊不要留下值
    context = {
        'title': 'contact us',
        'form': form
    }
    return  render(request,"form.html",context)

def example_page(request):
    exmaple_title = "example title..."
    context = {"title":exmaple_title}
    template_name = "title.txt"
    template_here = "helloword.html"
    template_object = get_template(template_name)
    render_item = template_object.render(context)
    return  render(request,"helloword.html",{'title':render_item})
    #HttpResponse(render_item)