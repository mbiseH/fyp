from django.db import models


class student(models.Model):
    student_reg_number = models.CharField(max_length=100, primary_key= True)
    student_first_name = models.CharField(max_length=100)
    student_middle_name = models.CharField(max_length=100)
    student_surname = models.CharField(max_length=100)
    student_degree_program = models.CharField(max_length=100)
    student_fingerprint_id = 
    student_gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='F')

    def __str__(self):
        return self.student_reg_number




class staff (models.Model):
    
    staff_id= models.CharField(max_length=100,primary_key=True)
    staff_first_name= models.CharField(max_length=100)
    staff_middle_name= models.CharField(max_length=100)
    staff_surname= models.CharField(max_length=100)
    staff_office= models.CharField(max_length=100)
    staff_role= models.CharField(max_length=50)
    staff_gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), default='F')

    def __str__(self):
        return self.staff_surname




class appointment(models.Model):
    appointment_id= models.BigAutoField(primary_key=True)
    appointment_time= models.DateTimeField()
    appointment_status= models.CharField(max_length=10)
    appointment_description= models.CharField(max_length=100)
    appointment_type=models.CharField(max_length=10,choices=(('Indiv', 'Individual'), ('Grp', 'Group')), default='Indiv')
    appointment_category= models.CharField (max_length=10, choices=(('Priv', 'Private'), ('Acad', 'Academic'), ('Other', 'Others')), default='Acad')
    staff_phone_number= models.IntegerField()
    student_phone_number= models.IntegerField()
    student_reg_number= models.ForeignKey(student, on_delete=models.CASCADE)
    staff_id=models.ForeignKey(staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.appointment_id




class task (models.Model):
    task_id= models.BigAutoField(primary_key=True)
    task_issue_date= models.DateTimeField()
    task_feedback_file= models.FileField(null=True)
    task_type= models.CharField(max_length=100)
    task_description= models.CharField(max_length=100)
    staff_id= models.ForeignKey(staff, on_delete=models.CASCADE)
    appointment_id= models.ForeignKey(appointment, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_id





class user(models.Model):
    user_id= models.BigAutoField(primary_key=True)
    user_phone_number=models.IntegerField()
    user_password= models.CharField(max_length=100)
    staff_username= models.ForeignKey(staff, on_delete=models.CASCADE)
    student_username = models.ForeignKey(student, on_delete=models.CASCADE)


    def __str__(self):
        return self.user_id