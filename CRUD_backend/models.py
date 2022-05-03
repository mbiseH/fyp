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

    appointment_id = models.BigAutoField(primary_key=True)
    appointment_type = models.CharField(max_length=20)
    appointment_category = models.CharField (max_length=10)
    appointment_description = models.CharField (max_length=200)
    appointment_time = models.TimeField()
    appointment_date = models.DateField()
    staff_phone_number= models.IntegerField()
    student_phone_number= models.IntegerField()
    appointment_status = models.CharField(max_length=15, default="Pending")
    student_reg_number= models.ForeignKey(student, on_delete=models.CASCADE)
    staff_id=models.ForeignKey(staff, on_delete=models.CASCADE)

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





# from graphene_file_upload.scalars import Upload
# from django.core.files.storage import FileSystemStorage


# class UploadMutation(graphene.Mutation):
#     class Arguments:
#         file = Upload(required=True)

#     success = graphene.Boolean()
#     full_file_name = graphene.String()
#     file_name = graphene.String()

#     def mutate(self, info, file, **kwargs):
#         new_folder = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

#         try:
#             os.mkdir(os.path.join(str(settings.MEDIA_ROOT)+'/documents/', new_folder))
#             fs = FileSystemStorage(location=str(settings.MEDIA_ROOT)+'/documents/'+new_folder)
#         except:
#             fs = FileSystemStorage(location=str(settings.MEDIA_ROOT)+'/documents/'+new_folder)

#         new_file_name,ext=os.path.splitext(file.name)
#         modified_name = '{}_{}'.format(uuid.uuid4().hex[:24], "_"+new_file_name+""+ext)

#         new_attachment=fs.save(modified_name, file)
#         uploaded_file_url = fs.url('/documents/'+new_folder+"/"+new_attachment)
        
#         save_path = os.path.join(str(settings.MEDIA_ROOT)+'/documents/'+new_folder,str(modified_name))
#         saved_file_name, file_extension=os.path.splitext(save_path)

#         full_file_name=str(uploaded_file_url)
#         file_name=file.name

#         return UploadMutation(success=True,full_file_name=full_file_name,file_name=file_name)