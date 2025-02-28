from . import views
from django.urls import path


urlpatterns = [

    path('', views.index_view, name='index' ),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout' ),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name="register" ),
    path('admin_panel/', views.admin_panel_view, name='admin_panel'),
    path('person/<int:pk>', views.person, name='person'),
    path('person_delete/<int:pk>', views.person_delete, name='person_delete'),
    path('person_add/', views.person_add_view, name='person_add'),
    path('person_update/<int:pk>', views.person_update, name='person_update'),

]
