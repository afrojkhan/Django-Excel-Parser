from django.urls import path
from fileapi.views import Student,AdditionalInfo

urlpatterns = [
    path('student/',Student.as_view(),name='student'),
    path('additional/',AdditionalInfo.as_view(),name='additional_Info'),
]
