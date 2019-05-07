from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect
# from .forms import BlogPostForm ##將輸入textarea的東西透過BlogPost建立成一個obj所需的輸入
from .forms import BlogPostModelForm

# Create your views here.
from .models import BlogPost





def blog_post_list_view(request):
    # list out objs
    # could be search
    qs = BlogPost.objects.published() # queryset -> list of python object
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct() #不會出現重複的
    template_name = 'blog/list.html'
    context = {"object_list":qs}
    return render(request, template_name, context)




#@login_required() 在無登入的情況下，直接error 404
@staff_member_required() #會跳到要你登入的頁面
def blog_post_create_view(request):
    #create object
    #? use a form
    #request user -> return someting

    form = BlogPostModelForm(request.POST or None,request.FILES or None)
    if form.is_valid():

        ##透過(commit=False)的方式，我們可以修改要輸入進去的值
        obj = form.save(commit=False)
        obj.user = request.user      # obj.title = form.cleaned_data.get("title") + '0' #把字典內的東西挑出來 在後面加上0
        obj.save()
        ##----------------------------------------------


        ##透過自定義BlogPostForm建立的----------------
        # print(form.cleaned_data)                           ## form.cleaned_data => 在文字區域輸入進來的東西
        # obj = BlogPost.objects.create(**form.cleaned_data) ## 利用BlogPost建立一個內容為form.cleaned_data的東西，**是字典的意思
        # form = BlogPostForm() ###將輸入textarea的東西透過BlogPost建立成一個obj
        ##------------------------------------------

        ##透過（繼承）modelform建立的----------------
        # form.save()
        form = BlogPostModelForm()
        ##----------------------------------------


    template_name = 'form.html'
    context = {"form":form}
    return render(request, template_name, context)

def blog_post_detail_view(request,slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required()
def blog_post_update_view(request,slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None,instance=obj)
    if form.is_valid(): #如果使用者有輸入的話，讓它覆蓋舊的檔案
        form.save()

    template_name = 'form.html'
    context = {'title':f"Update {obj.title}",'form':form}
    return render(request, template_name, context)


@staff_member_required()
def blog_post_delete_view(requests,slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'

    if requests.method == "POST":
        obj.delete()
        return redirect("/blog")

    context = {"object": obj}
    return render(requests, template_name, context)