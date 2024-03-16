# from django.db import models
# from django.core.validators import RegexValidator
# from django.db import models
# from apps.users.models import User

# PHONE_NUMBER_VALIDATOR = RegexValidator(regex=r"^/+998/d{9}$",message="Invalid phone number")
 
 


# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

# class Position(BaseModel):
#     subject_name = models.CharField(max_length=250,
#                                    verbose_name='Subject name')

    
#     def __str__(self) -> str:
#         return self.subject_name
    
# class School(BaseModel):
#     school_name = models.CharField(max_length=250)
#     director = models.OneToOneField(User,
#                                     on_delete=models.PROTECT,
#                                     verbose_name='Director',
#                                     related_name='school_director',
#                                     )
#     adress = models.CharField(max_length=300)


#     def __str__(self) -> str:
#         return self.school_name
    



# class Pupil(BaseModel):
#     full_name = models.CharField(max_length=250,verbose_name='Full name')
#     school = models.ForeignKey('School',
#                                on_delete=models.PROTECT,
#                                related_name='schools',
#                                verbose_name='School')
#     group = models.ForeignKey('Group',
#                               on_delete=models.PROTECT,
#                               related_name='groups',
#                               verbose_name='Group')
#     birthday = models.DateField()
#     phone_number = models.CharField(max_length=13 ,
#                                     validators=[PHONE_NUMBER_VALIDATOR],
#                                     verbose_name='Phone number')
#     parent_full_name = models.CharField(max_length=500,
#                                         verbose_name='Parent full name')
#     parent_number = models.CharField(max_length=13,
#                                      validators=[PHONE_NUMBER_VALIDATOR],
#                                      verbose_name='Parent phone number')
    
    
#     def __str__(self):
#         return self.full_name
    

# class Group(BaseModel):
#     group_name = models.CharField(max_length=250,
#                                   verbose_name='Group name')
#     pupils_count = models.IntegerField(default=0)
#     teacher = models.ForeignKey("Teacher",
#                                 on_delete=models.PROTECT,
#                                 verbose_name='Teacher',
#                                 related_name='teachers')
    
#     def __str__(self) -> str:
#         return self.group_name
    
# class Teacher(BaseModel):
#     full_name = models.CharField(max_length=250,
#                                  verbose_name='Full name')
#     phone_number = models.CharField(max_length=13,
#                                     validators=[PHONE_NUMBER_VALIDATOR],
#                                     verbose_name='Phone number')
#     group = models.ForeignKey(Group, 
#                               verbose_name='Class Group',
#                               related_name='groups',
#                               on_delete=models.PROTECT)
#     school = models.ForeignKey(School, 
#                               verbose_name='School',
#                               related_name='schools',
#                               on_delete=models.PROTECT)
#     experience = models.IntegerField(default =0,
#                                      verbose_name='Experience')
#     position = models.ForeignKey(Position,
#                                  on_delete=models.PROTECT,
#                                  verbose_name='Position',
#                                  related_name='positions'
#                                  )
#     birthday = models.DateField()


#     def __str__(self) -> str:
#         return self.full_name
    

# class ClassRoom(BaseModel):
#     class_name = models.CharField(max_length=250)
#     school = models.ForeignKey(School,
#                                on_delete=models.PROTECT,
#                                related_name='schools',
#                                verbose_name='School')
#     capacity = models.PositiveIntegerField(default = 0)
#     group = models.ForeignKey(Group,
#                               on_delete=models.PROTECT,
#                               related_name='groups',
#                               verbose_name='Group')
    
#     def __str__(self) -> str:
#         return self.class_name
    
