from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('<tag>/', views.index, name='category_tag'),
    path('post/<int:pk>', views.add_comment_post, name='add_comment_to_post')
]