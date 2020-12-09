from django.urls import path
from actors_list import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='shows_list'),
    path('show/create', views.SerialCreate.as_view(), name='create_show'),
    path('show/delete/<pk>', views.SerialDelete.as_view(), name='delete_serial'),
    path('show/update/<pk>', views.SerialUpdate.as_view(), name='update_serial'),
    path('show/details/<pk>', views.SerialDetails.as_view(), name='serial_details'),
    path('show/details/<pk>/comment', views.CommentCreate.as_view(), name='comment_create'),
    path('profile/', views.Profile.as_view(), name='profile'),





]