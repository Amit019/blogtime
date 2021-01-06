from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category,Comment
from django.utils import timezone
import datetime
from taggit.models import Tag
from django.db.models import Q,Count
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.


# <!------------ Search View ---------------!>
def search(request):
    q=request.GET.get('q')
    queryset =Post.published.filter(
        Q(title__icontains=q) |
        Q(content__icontains=q)
        
    ).distinct() 
   
    
    parms={
        'queryset':queryset,
        'title':f'Serach for {q}',
        'pop_post': Post.published.order_by('-read')[:5],
        'category_count':Category.objects.all().annotate(posts_count=Count('post')),
        'tags': Tag.objects.all(),
    
        }
    return render(request,'search.html', parms)


# <!------------End Search View ---------------!>
  
# <!------------ blog list View ---------------!>

def blog_list(request):
    posts=Post.published.all().order_by('-publish')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    parms={}
    parms['posts']=posts
    parms['page']=page
    parms['category_count']=Category.objects.all().annotate(posts_count=Count('post'))
    parms['tags']= Tag.objects.all()
    return render(request,'blog_list.html', parms)

# <!------------ end bloglist View ---------------!>


# <!------------ Index(home) View ---------------!>
class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-publish']

    def get_context_data(self, *args, **kwargs):
        posts=Post.published.all()
        week_ago = datetime.date.today() - datetime.timedelta(days=7)
        cate_menu = Category.objects.all()
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['cate_menu'] = cate_menu
        context['health'] = Post.published.filter(category=cate_menu[0])
        context['techs'] = Post.published.filter(category=cate_menu[1])
        context['django'] = Post.published.filter(category=cate_menu[2])
        context['trends'] = Post.published.filter(
            publish__gte=week_ago).order_by('-read')
        context['pop_post'] = Post.published.order_by('-read')[:5]
        context['category_count'] = Category.objects.all().annotate(posts_count=Count('post'))
        context['tags'] = Tag.objects.all()
        context['posts'] = posts
       

        return context

# <!------------ end Index View ---------------!>


# <!------------ Post_Detail View ---------------!>
def post_detail(request,slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    post.read=post.read+1
    post.save()
    post_tags_ids=Post.tags.values_list('id',flat=True)  
    similar_posts=Post.published.filter(tags__in=post_tags_ids.exclude(id=post.id))   
    similar_posts=similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]  
    comments=Comment.objects.filter(post=post,reply=None).order_by('-pk')
    if request.method == "POST":
        content=request.POST.get('content')
        name=request.POST.get('name')
        email=request.POST.get('email')
        reply_id =request.POST.get('comment_id')
        comment_qs=None
        if reply_id:
            comment_qs=Comment.objects.get(id=reply_id)
        comment=Comment.objects.create(post=post,name=name,email=email,content=content,reply=comment_qs)
        comment.save()
        return redirect(reverse("article", kwargs={
            'slug': post.slug
             }))
    else:
      pass
  
    context={}
    context['category_count'] = Category.objects.all().annotate(posts_count=Count('post'))
    context['tags'] = Tag.objects.all()
    context['comments'] = comments
    context['post'] = post
    context['similar_posts'] = similar_posts 
    context['pop_post'] = Post.objects.order_by('-read')[:6]
       

    return render(request,
                  'article_details.html',context)
  

# <!------------ end Post_deatil View ---------------!>

# <!------------ tagged View ---------------!>
def tagged(request, tag_slug=None):
    tag = None
    posts = Post.published.all()
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
  
 
    parmas = {'tag': tag,
              'posts': posts, 
              'category_count':Category.objects.all().annotate(posts_count=Count('post')),
              'tags': Tag.objects.all(),
              }
    return render(request, 'search.html', parmas)

# <!------------ end taggedView ---------------!>

# <!------------ category View ---------------!>
class CategoryView(ListView):
    model = Post
    template_name = 'search.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])

        return Post.published.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['category_count']=Category.objects.all().annotate(posts_count=Count('post'))
        context['tags']= Tag.objects.all()
        return context

# <!------------ end  Category View ---------------!>


def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)


