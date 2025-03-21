from django.urls import path
from .views import EventListCreateView, EventDetailView, HolidayListCreateView, HolidayDetailView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('holidays/', HolidayListCreateView.as_view(), name='holiday-list-create'),
    path('holidays/<int:pk>/', HolidayDetailView.as_view(), name='holiday-detail'),
]
