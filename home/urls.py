from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("donors_list/<int:myid>/", views.donors_list, name="donors_list"),
    path("donors_details/<int:myid>/", views.donors_details, name="donors_details"),
    path("request_blood/", views.request_blood, name="request_blood"),
    path("see_all_request/", views.see_all_request, name="see_all_request"),
    path("become_donor/", views.become_donor, name="become_donor"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_status/', views.change_status, name='change_status'),
    path('request_status/<int:brid>', views.request_status, name='request_status'),
    path('delete_profile/<int:id>', views.delete_profile, name='delete_profile'),
]