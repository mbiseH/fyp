import os
from datetime import datetime, timedelta
from twilio.rest import Client
from asyncio.windows_events import NULL
from twilio.rest import Client
from django.db import models
from django.contrib.auth.models import AbstractUser

class student(models.Model):
    student_reg_number = models.CharField(max_length=100, primary_key= True)
    student_first_name = models.CharField(max_length=100)
    student_middle_name = models.CharField(max_length=100, null=True)
    student_surname = models.CharField(max_length=100)
    student_phone_number= models.CharField(max_length = 20 , null = False)
    student_degree_program = models.CharField(max_length=100)
    student_fingerprint_id = models.CharField(max_length=100)
    student_associated_group_name = models.CharField(max_length=100, default=NULL)
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
    staff_phone_number= models.CharField(max_length = 20, null = False )
    staff_gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='F')

    def __str__(self):
        return self.staff_surname




class appointment(models.Model):

    appointment_id = models.BigAutoField(primary_key=True)
    appointment_time = models.TimeField()
    appointment_date = models.DateField()
    is_New = models.BooleanField(default=True)
    appointment_type = models.CharField(max_length=20)
    appointment_category = models.CharField (max_length=10)
    appointment_description = models.CharField (max_length=200)
    appointment_reschedule_frequency = models.IntegerField(default =0)
    appointment_verification_status = models.BooleanField(default=False)
    student_phone_number = models.CharField (max_length=200)
    staff_phone_number = models.CharField (max_length=200)
    appointment_status = models.CharField(max_length=25, default="Pending")
    staff_first_name  = models.CharField (max_length=200)
    staff_surname = models.CharField (max_length=200)
    student_first_name = models.CharField (max_length=200)
    student_surname = models.CharField (max_length=200)
    student_reg_number= models.ForeignKey(student, on_delete=models.CASCADE)
    staff_id=models.ForeignKey(staff, on_delete=models.CASCADE)
    
    def reminder_method(self):
        if self.appointment_status == "Approved":
            current_date_time_object = datetime.strptime(datetime.now(), "%Y-%m-%d")
            date_time_object_from_db = datetime.strptime(self.appointment_date, "%Y-%m-%d")
            
            time_object_from_db = datetime.time(self.appointment_time)
            current_time_object = datetime.time(datetime.now())
            
            if (((date_time_object_from_db) - (current_date_time_object) ==  timedelta(days=0) )  & (( time_object_from_db) - (current_time_object) ==  timedelta(minutes=15))):
                
                account_sid = "AC27ee4b69fc4c2f932ba1897d4dd3a184"
                auth_token = "14a93eff44045bc413bec7112278bcd9"
                client = Client(account_sid, auth_token)
                
                # message to staff
                msg_to_staff = "Hello staff {} {}, an appointment with {} {} scheduled on {} at {}, is due to begin in 15 minutes. Please visit the appointment system for more details. Thank you!".format(self.staff_first_name, self.staff_surname, self.student_first_name, self.student_surname, self.appointment_date,self.appointment_time)
                client.api.account.messages.create(
                    from_="+19704782047",
                    to=self.staff_phone_number, 
                    body=msg_to_staff)
                
                # message to student
                msg_to_student = "Hello student {} {}, an appointment with {} {} scheduled on {} at {},  is due to begin in 15 minutes. Kindly visit the appointment system for more details. Thank you!".format(self.student_first_name, self.student_surname,self.staff_first_name, self.staff_surname, self.appointment_date,self.appointment_time)
                client.api.account.messages.create(
                    from_="+19704782047",
                    to=self.student_phone_number,
                    body=msg_to_student )
            

    def __str__(self):
        return self.appointment_id



class complain(models.Model):

    complain_id = models.BigAutoField(primary_key=True)
    complain_status = models.CharField(max_length=20, default= "Pending")
    complain_is_new = models.BooleanField(default=True)
    complain_description = models.CharField(max_length= 255)
    complain_creation_date = models.DateTimeField(auto_now_add=True)
    complain_to_staff = models.ForeignKey(staff, on_delete=models.CASCADE)
    complain_from_appointment = models.ForeignKey(appointment, on_delete=models.CASCADE)
    
    def __str__(self):
            return self.complain_id



class task (models.Model):
    task_id= models.BigAutoField(primary_key=True)
    task_issue_date= models.DateField()
    task_deadline_date= models.DateField()
    task_feedback_file= models.CharField(max_length= 100, null=True)
    task_type= models.CharField(max_length=100)
    task_description= models.CharField(max_length=100)
    staff_id= models.ForeignKey(staff, on_delete=models.CASCADE)
    appointment_id = models.ForeignKey(appointment, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task_id


class user(AbstractUser):
    # user_id = models.CharField(max_length= 100, unique=True)
    # user_password_reset_code = models.CharField(max_length= 20, blank = True)
    # user_role = models.CharField(max_length= 100, default="student", blank=False)
    # staff_username= models.ForeignKey(staff, on_delete=models.CASCADE, null=True)
    # student_username = models.ForeignKey(student, on_delete=models.CASCADE, null=True)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    
    def __str__(self):
        return self.user_id
    
    # token 14a93eff44045bc413bec7112278bcd9
    # SID AC27ee4b69fc4c2f932ba1897d4dd3a184
    # +19704782047
    # phone number +255692087745


