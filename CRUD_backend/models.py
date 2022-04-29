from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

class student(models.Model):
    student_reg_number = models.CharField(max_length=100, primary_key= True)
    student_first_name = models.CharField(max_length=100)
    student_middle_name = models.CharField(max_length=100, null=True)
    student_surname = models.CharField(max_length=100)
    student_degree_program = models.CharField(max_length=100)
    student_fingerprint_id = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='F')

    def __str__(self):
        return self.student_reg_number


class staff (models.Model):

    staff_id= models.CharField(max_length=100, primary_key=True)
    staff_first_name= models.CharField(max_length=100)
    staff_middle_name= models.CharField(max_length=100, null =True)
    staff_surname= models.CharField(max_length=100)
    staff_office= models.CharField(max_length=100)
    staff_role = models.CharField(max_length=100)
    staff_gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='F')

    def __str__(self):
        return self.staff_surname




class appointment(models.Model):

    appointment_id= models.BigAutoField(primary_key=True)
    appointment_type=models.CharField(max_length=10,choices=(('Indiv', 'Individual'), ('Grp', 'Group')), default='Indiv')
    appointment_category= models.CharField (max_length=10, choices=(('Priv', 'Private'), ('Acad', 'Academic'), ('Other', 'Others')), default='Acad')
    appointment_description = models.CharField (max_length=200)
    appointment_time = models.CharField(max_length= 20)
    staff_phone_number= models.IntegerField()
    student_phone_number= models.IntegerField()
    appointment_status = models.CharField(max_length=15)
    student_reg_number= models.ForeignKey(student, on_delete=models.CASCADE)
    staff_id=models.ForeignKey(staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.appointment_id




class task (models.Model):
    task_id= models.BigAutoField(primary_key=True)
    task_issue_date= models.CharField(max_length = 20)
    task_feedback_file= models.CharField(max_length= 100, null=True)
    task_type= models.CharField(max_length=100)
    task_description= models.CharField(max_length=100)
    staff_id= models.ForeignKey(staff, on_delete=models.CASCADE)
    appointment_id= models.ForeignKey(appointment, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_id

class user(AbstractUser):
    
    # id = models.BigAutoField(primary_key=True, unique=True)
    # user_phone_number=models.IntegerField()
    # user_email = models.EmailField(blank = False,  max_length=255)
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    # user_verification = models.BooleanField(default= "False")
    # user_password_reset_code = models.CharField(max_length= 20, null = True)
    # user_password= models.CharField(max_length=100, null= False)
    # user_role = models.CharField(max_length= 100, default="student")
    # staff_username= models.ForeignKey(staff, on_delete=models.CASCADE, null=True)
    # student_username = models.ForeignKey(student, on_delete=models.CASCADE, null=True)


    # def __str__(self):
    #     return self.user_id
    
#  https://www.youtube.com/watch?v=pyV2_F9wlk8