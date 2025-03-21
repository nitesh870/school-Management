from django.urls import path
from .views import ClassListCreateView, ClassDetailView, SubjectListCreateView, SubjectDetailView
from .views import ExamListCreateView, ExamDetailView, MarksListCreateView, MarksDetailView

urlpatterns = [
    path('classes/', ClassListCreateView.as_view(), name='class-list-create'),
    path('classes/<int:pk>/', ClassDetailView.as_view(), name='class-detail'),
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),
]

urlpatterns += [
    path('exams/', ExamListCreateView.as_view(), name='exam-list-create'),
    path('exams/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    path('marks/', MarksListCreateView.as_view(), name='marks-list-create'),
    path('marks/<int:pk>/', MarksDetailView.as_view(), name='marks-detail'),
]

from .views import PeriodListCreateView, PeriodDetailView, TimeTableListCreateView, TimeTableDetailView

urlpatterns += [
    path('periods/', PeriodListCreateView.as_view(), name='period-list-create'),
    path('periods/<int:pk>/', PeriodDetailView.as_view(), name='period-detail'),
    path('timetables/', TimeTableListCreateView.as_view(), name='timetable-list-create'),
    path('timetables/<int:pk>/', TimeTableDetailView.as_view(), name='timetable-detail'),
]

from .views import AttendanceListCreateView, AttendanceDetailView

urlpatterns += [
    path('attendance/', AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('attendance/<int:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),
]

from .views import ReportCardListCreateView, ReportCardDetailView

urlpatterns += [
    path('report-cards/', ReportCardListCreateView.as_view(), name='reportcard-list-create'),
    path('report-cards/<int:pk>/', ReportCardDetailView.as_view(), name='reportcard-detail'),
]