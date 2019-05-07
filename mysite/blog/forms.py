from django import forms

from .models import BlogPost

##類似BlogPost(blog/models)
class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


##透過modelform來抓取user所輸入的值
class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost #位址：blog/models裡的 BlogPost
        fields = ['title','image','slug','content','publish_date']

    ##設立提醒訊息（invaild）-----------------------------
                    # arguments keyword arguments
    def clean_title(self,*args,**kwargs):

        #透過BlogPostModelForm中撈出使用者輸入的資料（cleaned_data）
        #並用get找到有關title東西
        title = self.cleaned_data.get('title')

        instance = self.instance #找出原本的資料
        print(instance) #檢視看看傳入資料有哪些

        #設定一個qs來存取使用者輸入的title
        #如果已存在就顯示錯誤訊息
        #如果沒有存在就存入           title_iexact=>大小寫都看成相同 ex: qws Qws 都會顯示已被使用
        qs = BlogPost.objects.filter(title=title)

        #新創建的instance會是None，所以這裡透過這個方法判別他是不是新建的（create）
        #如果不是新建的，將qs設成和原先的不同，避免出現名稱相同的錯誤
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)

        #slug 中的unique
        if qs.exists():
            raise forms.ValidationError("這個標題已經被使用")

        return title
    #----------------------------------------------------

##-------------------------------

