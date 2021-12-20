from django.conf import settings
from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	path('feed/<str:pk>/', views.feed, name='feed'),
	path('profile/', views.profile, name='profile'),
	path('profile/<str:username>/', views.profile, name='profile'),
	path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
	path('post/', views.post, name='post'),
	path('follow/<str:username>/', views.follow, name='follow'),
	path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
	path('post/<int:pk>/comment/', views.commentpost, name='commentpost'),
	path('', views.home, name='home'),

	
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)