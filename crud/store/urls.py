from . import views
from django.urls import path


urlpatterns = [
    path('', views.index_view, name='index' ),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout' ),
    path('login/', views.login_view, name='login'),
    path('admin_panel/', views.admin_panel_view, name='admin_panel'),
]
