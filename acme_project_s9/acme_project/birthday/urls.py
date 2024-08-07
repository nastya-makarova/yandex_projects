from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    # path('', views.birthday, name='create'),
    # path('list/', views.birthday_list, name='list'),
    path('login_only/', views.simple_view),
    path('', views.BirthdayCreateView.as_view(), name='create'),
    path('list/', views.BirthdayListView.as_view(), name='list'),
    # path('<pk>/edit', views.birthday, name='edit'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    # path('<pk>/delete', views.birthday_delete, name='delete'),
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    path('<int:pk>/comment', views.add_comment, name='add_comment'),
]
