from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home" ),
    # path('login/', views.login_view, name="login" ),
    path('logout/', views.logout_view, name="logout" ),
    path('index.html/', views.index_view, name='index'),
]

# urlpatterns = [
#     path('', views.home, name="index" ),
#     # path('login/', views.login_view, name="login" ),
#     path('logout/', views.logout_view, name="logout" ),
#     path('home/', views.index_view, name='home'),
# ]
