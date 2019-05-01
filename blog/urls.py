from  django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blogs/', views.blogs, name="blogs"),
    path('about/', views.about, name="about"),
    path('deatil/<int:id>', views.detail, name='detail_view')
]