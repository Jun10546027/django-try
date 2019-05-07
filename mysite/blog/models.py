from django.conf import settings
from django.db import models
from django.db.models import Q #搜尋關鍵字時，可以用來設定被搜尋到的範圍
from django.utils import timezone


User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        #BlogPost.objects.all()
        ##publist_date__lte 是兩個＿＿
        return self.filter(publish_date__lte=now)
    #設定搜尋的關鍵字的範圍／，這裡是title
    # def search(self,query):
    #     return self.filter(title__iexact = query)
    def search(self,query):
        ##可以被搜尋的範圍，類似定義搜尋的關鍵字
        lookup = (Q(title__icontents= query) |
                  Q(content__icontents = query)|
                  Q(slug__icontents=query) |
                  Q(user__first_name__icontents = query)|
                  Q(user__last_name__icontents=query)|
                  Q(user__username__icontents=query)
                  )
        return self.filter(lookup)

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)
    def published(self):
        return self.get_queryset().published()
    def search(self,query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='image/',blank=True,null=True)
    title = models.CharField(max_length=120) #一定要打max_length，不然會報錯
    content = models.TextField(null=True,blank=True)
    slug = models.SlugField(unique = True) # hello world -> hello-world

    publish_date = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        #  - => 高到低      沒有=>低到高
        #ex. ordering = ['id']
        ordering = ['-publish_date','-update','-timestamp']


    def get_absolute_url(self):
        return f'/blog/{self.slug}'
    def get_edit_url(self):
        return f'/blog/{self.slug}/edit'
    def get_delete_url(self):
        return f'/blog/{self.slug}/delete'