from django.contrib import admin
from apps.common.models import *

admin.site.register(Position)
admin.site.register(School)
admin.site.register(Pupil)
admin.site.register(Group)
admin.site.register(ClassRoom)
# from .models import *


# @admin.register(Position)
# class PositionAdmin(admin.ModelAdmin):
#     list_display = ('subject_name',)    
#     list_filter = ('subject_name',)
#     search_fields = ('subject_name',)
    


# @admin.register(School)
# class SchoolAdmin(admin.ModelAdmin):
#     list_display = ('school_name', 'director','adress')
#     list_filter = ('school_name','adress' )
#     search_fields = ('school_name','adress')

# @admin.register(Pupil)
# class PupilAdmin(admin.ModelAdmin):
#     list_display = ('full_name','school', 'group', 'birthday', 'phone_number', 'parent_full_name', 'parent_number')
#     list_filter = ('full_name','school','group')
#     search_fields = ('full_name','school','group')



# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('group_name', 'pupils_count', 'teacher')
#     list_filter = ('group_name', 'teacher')
#     search_fields = ('group_name', 'teacher')


# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'phone_number','group','school', 'experience', 'position', 'birthday')
#     list_filter = ('full_name', 'group','school')
#     search_fields = ('full_name', 'group','school')



# @admin.register(ClassRoom)
# class ClassRoomAdmin(admin.ModelAdmin):
#     list_display = ('class_name','school', 'capacity', 'group')
#     list_filter = ('class_name','school')
#     search_fields = ('class_name','school')
# >>>>>>> ef3146b92e854e7464a7390649fab513b4947217
