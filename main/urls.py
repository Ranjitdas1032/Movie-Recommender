from django.urls import path,include
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('signup/',views.signup, name= 'signup'),
    path('login_cus/',views.login_cus , name = 'login_cus'),
    path('logout_cus/',views.logout_cus,name = 'logout_cus'),
    path('',views.home,name='home'),
    path('add_movie/',views.add_movie,name='add_movie'),
    path('movie_detail/<int:pk>',views.movie_detail,name="movie_detail"),
    path('movie_chart_data/<int:pk>',views.movie_chart_data,name="movie_chart_data"),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

