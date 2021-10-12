from.views import edit_student, register_student, student_profile
from django.urls import path
from.views import register_student,student_list
from.views import student_profile
from django.urls import reverse



urlpatterns = [
    path("register/",register_student,name="register_student"),
    path("list/",student_list,name="student_list"),
    path("profile/<int:id>/",student_profile,name="student_profile"),
    path("edit/<int:id>/",edit_student,name="edit_student"),

    
]

