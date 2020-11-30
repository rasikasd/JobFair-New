from django.urls import path
from . import views
from .views import (
    JobsListView, 
    JobsDetailView, 
    JobsCreateView,
    JobsUpdateView,
    JobsDeleteView
)
from .models import Jobs

urlpatterns = [
    path('', JobsListView.as_view(), name='employer-home'),
    path('jobs/<int:pk>/', JobsDetailView.as_view(), name='jobs-detail'),
    path('jobs/<int:pk>/update', JobsUpdateView.as_view(), name='jobs-update'),
    path('jobs/<int:pk>/delete', JobsDeleteView.as_view(), name='jobs-delete'),
    path('jobs/new/', JobsCreateView.as_view(), name='jobs-create'),
    path('about/', views.about, name='employer-about'),
]
