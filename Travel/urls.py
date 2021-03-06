from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name="login"),
    path('blogindex.html', views.blogindex, name='blogindex'),
    path('blog.html', views.blog, name='blog'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about')
]
