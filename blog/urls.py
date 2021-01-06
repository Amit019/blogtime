from django.urls import path
from .views import IndexView,tagged,CategoryView,post_detail,search,blog_list

urlpatterns = [
   
    path('', IndexView.as_view(),name='index'),
    path('search/',search, name="search"),
    path('blog/',blog_list, name='blog_list'),
    path('<slug:slug>/',post_detail, name='article'),
    path('tag/<slug:tag_slug>',tagged,name='index_by_tag'),
    path('category/<int:pk>', CategoryView.as_view(), name="index_by_cate"),

]
