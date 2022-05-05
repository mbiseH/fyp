import graphene
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload
from django.core.files.storage import FileSystemStorage
from CRUD_backend.models import student, appointment, task, staff, complain



class student_type(DjangoObjectType):
    class Meta:
        model = student

class appointment_type(DjangoObjectType):
    class Meta:
        model = appointment

class task_type(DjangoObjectType):
    class Meta:
        model = task

class staff_type(DjangoObjectType):
    class Meta:
        model = staff

class complain_type (DjangoObjectType):
    class Meta:
        model = complain
   


# class  user_type(DjangoObjectType):
#     class Meta:
#         model = user


class Query(graphene.ObjectType):

    all_students = graphene.List(student_type)
    student = graphene.Field(student_type, student_reg_number = graphene.ID())

    def resolve_all_students(self, info, **kwargs):
        # Querying a list of all students
        return student.objects.all()

    def resolve_student(self, info, student_reg_number):
        # Querying a single student here wazeee
        return student.objects.get(pk=student_reg_number)


    all_complains = graphene.List(complain_type)
    complain = graphene.Field(complain_type, complain_id = graphene.ID())
    complain_to_staff = graphene.List(complain_type, staff_id = graphene.String())
    
    def resolve_all_complains(self, info, **kwargs):
        #turudishie Complains Zote
        return complain.objects.all()
    
    def resolve_complain(self, info, complain_id):
        #tupe complain moja tu
        return complain.objects.get(pk=complain_id)
    
    def  resolve_staff_complains(self, info, staff_id):
        #rudisha complain za mwalimu fulani tu
        return complain.objects.filter(staff_id = staff_id)
   
 
    zote_appointments = graphene.List(appointment_type, staff_id=graphene.String())
    appointment = graphene.Field(appointment_type, appointment_id=graphene.ID())
    all_appointments = graphene.List(appointment_type)
    student_appointment = graphene.List(appointment_type, student_reg_number=graphene.String())
    staff_appointment = graphene.List(appointment_type, staff_id=graphene.String())
    count_new_appointments = graphene.Int()
  
    def resolve_zote_appointments(self, info):
        #return appointment Done By a A single Staff member{User}
        return appointment.objects.all()

    def resolve_appointment(self, info, appointment_id):
        # Querying a single appointment
        return appointment.objects.get(pk=appointment_id)

    def resolve_student_appointment(self, info, student_reg_number):
        #Appointment zote za mwanafunzi mmoja {User}
        return appointment.objects.filter(student_reg_number=student_reg_number)

    def resolve_staff_appointment(self, info, staff_id):
        #return appointment Done By a A single Staff member{User}
        return appointment.objects.filter(staff_id=staff_id)
    
    def resolve_all_appointments (self, info):
        return appointment.objects.all()
    
    def resolve_count_new_appointments(self, info):
        return appointment.objects.filter(is_New= True).count()


    all_tasks = graphene.List(task_type)
    task = graphene.Field(task_type, task_id=graphene.ID())

    def resolve_all_tasks(self, info, **kwargs):
        # rudisha all tasks assigned
        return task.objects.all()
        
    def resolve_task(self, info, task_id):
        # return a selected task
        return task.objects.get(pk=task_id)


    all_staffs= graphene.List(staff_type)
    staff = graphene.Field(staff_type, staff_id=graphene.ID())

    def resolve_all_staffs(self, info, **kwargs):
        # return all staffs
        return staff.objects.all()
    def resolve_staff(self, info, staff_id):
        # a function to return a staff
        return staff.objects.get(pk=staff_id)


    # all_users = graphene.List(user_type)
    # user = graphene.Field(user_type, user_id=graphene.ID())

    # def resolve_all_users(self, info, **kwargs):
    #     # a resolver fuction to return all users of the system
    #     return user.objects.all()
    # def resolve_user(self, info, user_id):
    #     # a function to return a single selected user
    #     return user.objects.get(pk=user_id)



#******************* MUTATIONS *************************#



# -----------> STUDENT-TABLE-MUTATIONS----------

class CreateStudent(graphene.Mutation):

    class  Arguments:
        student_reg_number = graphene.ID()
        student_first_name = graphene.String()
        student_middle_name = graphene.String()
        student_surname = graphene.String()
        student_fingerprint_id = graphene.String()
        student_degree_program = graphene.String()
        student_gender = graphene.String()


    student = graphene.Field(student_type)

    def mutate(self, info, student_reg_number, student_fingerprint_id,
               student_first_name , student_middle_name, student_surname,
               student_degree_program,student_gender):

        createdStudent = student.objects.create(
        student_reg_number = student_reg_number,
        student_first_name = student_first_name,
        student_middle_name = student_middle_name,
        student_surname =student_surname,
        student_fingerprint_id = student_fingerprint_id,
        student_degree_program = student_degree_program,
        student_gender=student_gender)

        return CreateStudent( student = createdStudent)


class UpdateStudent(graphene.Mutation):

    class  Arguments:
        student_reg_number = graphene.ID()
        student_first_name = graphene.String()
        student_middle_name = graphene.String()
        student_surname = graphene.String()
        student_degree_program = graphene.String()
        student_gender = graphene.String()

    student = graphene.Field(student_type)

    def mutate(self, info, student_reg_number, student_first_name =None, student_middle_name=None, student_surname =None, student_degree_program =None, student_gender =None):

        updatedStudent = student.objects.get(pk=student_reg_number)

        updatedStudent.student_first_name = student_first_name if student_first_name is not None else updatedStudent.student_first_name
        updatedStudent.student_middle_name = student_middle_name if student_middle_name is not None else updatedStudent.student_middle_name
        updatedStudent.student_surname =student_surname if student_surname is not None else updatedStudent.student_surname
        updatedStudent.student_degree_program = student_degree_program if student_degree_program is not None else updatedStudent.student_degree_program
        updatedStudent.student_gender=student_gender if student_gender is not None else updatedStudent.student_gender
        UpdateStudent.save()
        return UpdateStudent( student = updatedStudent)


class DeleteStudent(graphene.Mutation):

    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    student = graphene.Field(student_type)

    def mutate(self, info, id):

        deletedStudent = student.objects.get(pk=id)
        if student is not None:
            deletedStudent.delete()
        return DeleteStudent(student = deletedStudent)



# -----------> STAFF-TABLE-MUTATIONS----------

class CreateStaff(graphene.Mutation):

    class  Arguments:
        staff_id= graphene.ID(required = True)
        staff_first_name= graphene.String()
        staff_middle_name= graphene.String()
        staff_surname= graphene.String()
        staff_office= graphene.String()
        staff_role = graphene.String()
        staff_gender = graphene.String()


    staff = graphene.Field(staff_type)

    def mutate(self, info, staff_id, staff_first_name, staff_role, staff_middle_name,staff_surname,staff_office,staff_gender):

        createdStaff = staff.objects.create (
            staff_id = staff_id,
            staff_first_name = staff_first_name,
            staff_middle_name = staff_middle_name,
            staff_surname = staff_surname,
            staff_office = staff_office,
            staff_role = staff_role,
            staff_gender = staff_gender)


        return CreateStaff( staff = createdStaff)


class UpdateStaff(graphene.Mutation):

    class  Arguments:
        staff_id= graphene.ID()
        staff_first_name= graphene.String()
        staff_middle_name= graphene.String()
        staff_surname= graphene.String()
        staff_office= graphene.String()
        staff_role= graphene.String()
        staff_gender = graphene.String()

    staff = graphene.Field(staff_type)

    def mutate(self, info, staff_id, staff_first_name = None,staff_middle_name= None, staff_surname= None,staff_office = None,staff_role = None,staff_gender = None):

        updatedStaff = staff.objects.get(pk=staff_id)

        updatedStaff.staff_first_name = staff_first_name if staff_first_name is not None else  updatedStaff.staff_first_name
        updatedStaff.staff_middle_name =staff_middle_name if staff_middle_name is not None else updatedStaff.staff_middle_name
        updatedStaff.staff_surname = staff_surname if staff_surname is not None else updatedStaff.staff_surname
        updatedStaff.staff_office = staff_office if staff_office is not None else updatedStaff.staff_office
        updatedStaff.staff_role = staff_role if staff_role is not None else updatedStaff.staff_role
        updatedStaff.staff_gender = staff_gender if staff_gender is not None else updatedStaff.staff_gender
        UpdateStaff.save()
        return UpdateStaff( staff = updatedStaff)


class DeleteStaff(graphene.Mutation):

    class Arguments:
        # Tunamtafuta staff kwa id yake (the staff we want to delete)
        id = graphene.ID()

    staff = graphene.Field(staff_type)

    def mutate(self, info, id):

        deletedStaff = staff.objects.get(pk=id)
        if staff is not None:
            deletedStaff.delete()
            return DeleteStaff(staff = deletedStaff)




# -----------> APPOINTMENT-TABLE-MUTATIONS----------
# By mutations it means ni kuUpdate, kuCreate na kuDelete row kwenye
# db table (in this case ni APPOINTMENT TABLE)

class CreateAppointment(graphene.Mutation):

    class  Arguments:

        appointment_description= graphene.String()
        appointment_type=graphene.String()
        appointment_category= graphene.String()
        staff_phone_number= graphene.Int()
        appointment_time = graphene.String()
        appointment_date = graphene.String()
        student_phone_number= graphene.Int()
        student_reg_number= graphene.String()
        appointment_status=graphene.String()
        staff_id=graphene.String()

    appointment = graphene.Field(appointment_type)

    def mutate(self, info, appointment_time, appointment_date, student_reg_number,
                     appointment_type, appointment_category,
                    staff_phone_number,staff_id, appointment_status,
                    appointment_description, student_phone_number):
        
        studentobj = student.objects.get(pk=student_reg_number)
        staffobj = staff.objects.get(pk=staff_id)

        createdAppointment = appointment.objects.create (
        appointment_time = appointment_time,
        appointment_status = appointment_status,
        appointment_description = appointment_description,
        appointment_type = appointment_type,
        staff_id= staffobj,
        appointment_date = appointment_date,
        student_reg_number=studentobj,
        appointment_category = appointment_category,
        staff_phone_number = staff_phone_number,
        student_phone_number = student_phone_number
        )


        return CreateAppointment( appointment = createdAppointment)


class UpdateAppointment(graphene.Mutation):

    class  Arguments:

        appointment_id= graphene.ID()
        appointment_time= graphene.String()
        appointment_status= graphene.String()
        appointment_description= graphene.String()
        appointment_type=graphene.String()
        appointment_category= graphene.String()
        staff_phone_number= graphene.Int()
        student_phone_number= graphene.Int()
        student_reg_number= graphene.String()
        staff_id=graphene.String()

    appointment = graphene.Field(appointment_type)

    def mutate(self, info,appointment_id, appointment_time = None, appointment_status= None,appointment_description = None, appointment_type = None, appointment_category = None,               staff_phone_number = None, student_phone_number = None):

        updatedAppointment = appointment.objects.get(pk=appointment_id)

        updatedAppointment.appointment_time = appointment_time if appointment_time is not None else  updatedAppointment.appointment_time
        updatedAppointment.appointment_status = appointment_status if appointment_status is not None else updatedAppointment.appointment_status
        updatedAppointment.appointment_description = appointment_description if appointment_description is not None else updatedAppointment.appointment_description
        updatedAppointment.appointment_type = appointment_type if appointment_type is not None else updatedAppointment.appointment_type
        updatedAppointment.appointment_category = appointment_category if appointment_category is not None else updatedAppointment.appointment_category
        updatedAppointment.staff_phone_number = staff_phone_number if staff_phone_number is not None else updatedAppointment.staff_phone_number
        updatedAppointment.student_phone_number = student_phone_number if student_phone_number is not None else updatedAppointment.student_phone_number
        updatedAppointment.save()
        return UpdateAppointment( appointment = updatedAppointment )


class DeleteAppointment(graphene.Mutation):

    class Arguments:

        id = graphene.ID()

    appointment = graphene.Field(appointment_type)

    def mutate(self, info, id):

        deletedAppointment = appointment.objects.get(pk=id)
        if appointment is not None:
            deletedAppointment.delete()
        return DeleteAppointment(appointment = deletedAppointment)



# -----------> COMPLAIN-TABLE-MUTATIONS----------

class CreateComplain(graphene.Mutation):
    
    class  Arguments:
        complain_description = graphene.String()
        complain_to_staff = graphene.String()
        complain_from_appointment = graphene.String()
        
    complain = graphene.Field(complain_type)

    def mutate(self, info, complain_description, complain_to_staff, complain_from_appointment):

        staff_obj= staff.objects.get(pk=complain_to_staff)
        appointment_obj= appointment.objects.get(pk=complain_from_appointment)

        createdComplain= complain.objects.create (
            complain_description = complain_description,
            complain_to_staff = staff_obj,
            complain_from_appointment = appointment_obj )

        return CreateComplain( complain = createdComplain)


class UpdateComplain(graphene.Mutation):

    class  Arguments:
        complain_id = graphene.ID()
        complain_description= graphene.String()
        complain_to_staff = graphene.String()
        complain_from_appointment = graphene.String()
        
    complain = graphene.Field(complain_type)

    def mutate(self, info, complain_id, complain_description = None , complain_to_staff = None, complain_from_appointment= None):

        updatedComplain = complain.objects.get(pk=complain_id)
        appointment_obj = appointment.objects.get(pk=complain_from_appointment)
        staff_object = staff.objects.get(pk = complain_to_staff)

        updatedComplain.complain_description = complain_description if complain_description is not None else  updatedComplain.complain_description
        updatedComplain.staff_object = staff_object if staff_object is not None else updatedComplain.complain_to_staff
        updatedComplain.staff_id = appointment_obj if appointment_obj is not None else updatedComplain.complain_from_appointment
        UpdateComplain.save()
        return UpdateComplain( complain = updatedComplain)


class DeleteComplain(graphene.Mutation):

    class Arguments:

        complain_id = graphene.ID()

    complain = graphene.Field(complain_type)

    def mutate(self, info, complain_id):

        deletedComplain= complain.objects.get(pk=complain_id)
        if task is not None:
            deletedComplain.delete()
        return DeleteComplain(complain = deletedComplain)





# -----------> TASK-TABLE-MUTATIONS----------

class CreateTask(graphene.Mutation):

    class  Arguments:
        
        task_deadline_date = graphene.Date()
        task_feedback_file= graphene.String()
        task_type=  graphene.String()
        task_description= graphene.String()
        appointment_id=graphene.String()
        staff_id=graphene.String()


    task = graphene.Field(task_type)

    def mutate(self, info, task_deadline_date ,appointment_id, staff_id, task_type, task_description, task_feedback_file = None):

        staff_obj= staff.objects.get(pk=staff_id)
        appointment_obj= appointment.objects.get(pk=appointment_id)

        createdTask= task.objects.create (
        appointment_id= appointment_obj,
        task_issue_date= appointment_obj.appointment_date ,
        task_feedback_file= task_feedback_file,
        task_type= task_type,
        staff_id= staff_obj,
        task_description=task_description,
        task_deadline_date = task_deadline_date )

        return CreateTask( task = createdTask)

class UpdateTask(graphene.Mutation):
    
    class  Arguments:

        task_id= graphene.ID()
        task_feedback_file= graphene.String()
        task_deadline_date = graphene.Date()
        task_type=  graphene.String()
        task_description= graphene.String()
        staff_id= graphene.String()
        appointment_id= graphene.String()

    task = graphene.Field(task_type)

    def mutate(self, info, task_id, appointment_id = None , task_type = None  ,
        task_description= None, staff_id = None, task_feedback_file = None, ):

        updatedTask = task.objects.get(pk=task_id)
        appointment_obj = appointment.objects.get(pk=appointment_id)

        updatedTask.task_type = task_type if task_type is not None else  updatedTask.task_type
        updatedTask.task_description = task_description if task_description is not None else updatedTask.task_task_description
        updatedTask.staff_id = staff_id if staff_id is not None else updatedTask.staff_id
        updatedTask.appointment_id = appointment_obj if appointment_id is not None else updatedTask.appointment_id
        updatedTask.task_feedback_file = task_feedback_file if task_feedback_file is not None else updatedTask.task_feedback_file
        updatedTask.save()
        return UpdateTask( task = updatedTask)


class DeleteTask(graphene.Mutation):

    class Arguments:

        id = graphene.ID()

    task = graphene.Field(task_type)

    def mutate(self, info, id):

        deletedTask = task.objects.get(pk=id)
        if task is not None:
            deletedTask.delete()
        return DeleteTask(task = deletedTask)



# class UploadMutation(graphene.Mutation):
#     class Arguments:
#         file = Upload(required=True)
#         success = graphene.Boolean()
#         full_file_name = graphene.String()
#         file_name = graphene.String()

  
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


# -----------> user-TABLE-MUTATIONS----------
     
# class CreateUser(graphene.Mutation):

#     class  Arguments:

#         user_phone_number= graphene.Int()
#         user_password=  graphene.String()
#         user_role = graphene.String( required = True)
#         user_email = graphene.String(required = True)


#     user = graphene.Field(user_type)

#     def mutate(self,  info, user_phone_number,user_password,user_role, user_email ):

#         createdUser = user.objects.create (
#         user_phone_number= user_phone_number,
#         user_password = user_password,
#         user_role = user_role,
#         user_email = user_email
#         )

#         return CreateUser( user = createdUser)


# class UpdateUser(graphene.Mutation):

#     class  Arguments:

#         user_id = graphene.ID()
#         user_phone_number= graphene.Int()
#         user_password =  graphene.String()
#         user_role = graphene.String ()
#         user_email = graphene.String()

#     user = graphene.Field(user_type)

#     def mutate(self, info, user_id, user_email =None, user_role = None,user_phone_number = None, user_password = None, ):

#         updatedUser = user.objects.get(pk=user_id)

#         updatedUser.user_phone_number = user_phone_number if user_phone_number is not None else  updatedUser.user_phone_number
#         updatedUser.user_password = user_password if user_password is not None else updatedUser.user_password
#         updatedUser.user_role = user_role if user_role is not None else updatedUser.user_role 
#         updatedUser.user_email = user_email if user_email is not None else updatedUser.user_email
        
#         return UpdateUser( user = updatedUser)


# class DeleteUser(graphene.Mutation):

#     class Arguments:

#         id = graphene.ID()

#     user = graphene.Field(user_type)

#     def mutate(self, info, id):

#         deletedUser = user.objects.get(pk=id)
#         if user is not None:
#             deletedUser.delete()
#         return DeleteUser(user = deletedUser)



class Mutation(graphene.ObjectType):

    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()

    # create_user = CreateUser.Field()
    # update_user = UpdateUser.Field()
    # delete_user = DeleteUser.Field()

    create_staff = CreateStaff.Field()
    update_staff = UpdateStaff.Field()
    delete_staff = DeleteStaff.Field()

    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()
    
    create_complain = CreateComplain.Field()
    update_complain = UpdateComplain.Field()
    delete_Complain = DeleteComplain.Field()
  
    create_appointment = CreateAppointment.Field()
    update_appointment = UpdateAppointment.Field()
    delete_appointment = DeleteAppointment.Field()
