import graphene
from graphene_django import DjangoObjectType
from CRUD_backend.models import student, appointment, task, staff, user



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

class  user_type(DjangoObjectType):
    class Meta:
        model = user



class Query(graphene.ObjectType):

    all_students = graphene.List(student_type)
    student = graphene.Field(student_type, id=graphene.ID())

    def resolve_all_students(self, info, **kwargs):
        # Querying a list of all students
        return student.objects.all()
    def resolve_student(self, info, id):
        # Querying a single student here wazeee
        return student.objects.get(pk=id)


    all_appointments = graphene.List(appointment_type)
    appointment = graphene.Field(appointment_type, id=graphene.ID())

    def resolve_all_apppointments(self, info, **kwargs):
        # Querying a list of all appointments
        return appointment.objects.all()
    def resolve_appointment(self, info, id):
        # Querying a single appointment
        return appointment.objects.get(pk=id)


    all_tasks = graphene.List(task_type)
    task = graphene.Field(task_type, id=graphene.ID())

    def resolve_all_tasks(self, info, **kwargs):
        # rudisha all tasks assigned
        return task.objects.all()
    def resolve_task(self, info, **kwargs):
        # return a selected task
        return task.objects.get(pk=id)


    all_staffs= graphene.List(staff_type)
    staff = graphene.Field(staff_type, id=graphene.ID())

    def resolve_all_staffs(self, info, **kwargs):
        # return all staffs
        return staff.objects.all()
    def resolve_staff(self, info, id):
        # a function to return a staff
        return staff.objects.get(pk=id)


    all_users = graphene.List(user_type)
    user = graphene.Field(user_type, id=graphene.ID())

    def resolve_all_users(self, info, **kwargs):
        # a resolver fuction to return all users of the system
        return user.objects.all()
    def resolve_user(self, info, id):
        # a function to return a single selected user
        return user.objects.get(pk=id)



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

        student = student.objects.create(
            student_reg_number = student_reg_number,
            student_first_name = student_first_name,
            student_middle_name = student_middle_name,
            student_surname =student_surname,
            student_fingerprint_id = student_fingerprint_id,
            student_degree_program = student_degree_program,
            student_gender=student_gender)

        student.save()
        return CreateStudent( student = student)


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

        student = student.objects.get(pk=student_reg_number)

        student.student_first_name = student_first_name if student_first_name is not None else student.student_first_name
        student.student_middle_name = student_middle_name if student_middle_name is not None else student.student_middle_name
        student.student_surname =student_surname if student_surname is not None else student.student_surname
        student.student_degree_program = student_degree_program if student_degree_program is not None else student.student_degree_program
        student.student_gender=student_gender if student_gender is not None else student.student_gender

        student.save()
        return UpdateStudent( student = student)


class DeleteStudent(graphene.Mutation):

    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    student = graphene.Field(student_type)

    def mutate(self, info, id):

        student = student.objects.get(pk=id)
        if student is not None:
            student.delete()
        return DeleteStudent(student = student)



# -----------> STAFF-TABLE-MUTATIONS----------

class CreateStaff(graphene.Mutation):

    class  Arguments:
        staff_id= graphene.ID()
        staff_first_name= graphene.String()
        staff_middle_name= graphene.String()
        staff_surname= graphene.String()
        staff_office= graphene.String()
        staff_role= graphene.String()
        staff_gender = graphene.String()

    staff = graphene.Field(staff_type)

    def mutate(self, info, staff_id, staff_first_name,staff_middle_name,staff_surname,staff_office,staff_role,staff_gender):

        staff = staff.objects.create (
            staff_id = staff_id,
            staff_first_name = staff_first_name,
            staff_middle_name = staff_middle_name,
            staff_surname = staff_surname,
            staff_office = staff_office,
            staff_role = staff_role,
            staff_gender = staff_gender)

        staff.save()
        return CreateStaff( staff = staff)


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

        staff = staff.objects.get(pk=staff_id)

        staff.staff_first_name = staff_first_name if staff_first_name is not None else  staff.staff_first_name
        staff.staff_middle_name =staff_middle_name if staff_middle_name is not None else staff.staff_middle_name
        staff.staff_surname = staff_surname if staff_surname is not None else staff.staff_surname
        staff.staff_office = staff_office if staff_office is not None else staff.staff_office
        staff.staff_role = staff_role if staff_role is not None else staff.staff_role
        staff.staff_gender = staff_gender if staff_gender is not None else staff.staff_gender

        staff.save()
        return UpdateStaff( staff = staff)


class DeleteStaff(graphene.Mutation):

    class Arguments:
        # Tunamtafuta staff kwa id yake (the staff we want to delete)
        id = graphene.ID()

    staff = graphene.Field(staff_type)

    def mutate(self, info, id):

        staff = staff.objects.get(pk=id)
        if staff is not None:
            staff.delete()
            return DeleteStaff(staff = staff)




# -----------> APPOINTMENT-TABLE-MUTATIONS----------
# By mutations it means ni kuUpdate, kuCreate na kuDelete row kwenye
# db table (in this case ni APPOINTMENT TABLE)

class CreateAppointment(graphene.Mutation):

    class  Arguments:

        # appointment_id= graphene.ID()
        appointment_time= graphene.DateTime()
        appointment_status= graphene.String()
        appointment_description= graphene.String()
        appointment_type=graphene.String()
        appointment_category= graphene.String()
        staff_phone_number= graphene.Int()
        student_phone_number= graphene.Int()
        student_reg_number= graphene.String()
        staff_id=graphene.String()

    appointment = graphene.Field(appointment_type)

    def mutate(self, info, appointment_time, appointment_status,
                    appointment_description, appointment_type, appointment_category,
                    staff_phone_number, student_phone_number):

        staff = staff.objects.create (
        appointment_time = appointment_time,
        appointment_status = appointment_status,
        appointment_description = appointment_description,
        appointment_type = appointment_type,
        appointment_category = appointment_category,
        staff_phone_number = staff_phone_number,
        student_phone_number = student_phone_number
        )


        appointment.save()
        return CreateAppointment( appointment = appointment)


class UpdateAppointment(graphene.Mutation):

    class  Arguments:

        appointment_id= graphene.ID()
        appointment_time= graphene.DateTime()
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

        appointment = appointment.objects.get(pk=appointment_id)

        appointment.appointment_time = appointment_time if appointment_time is not None else  appointment.appointment_time
        appointment.appointment_status = appointment_status if appointment_status is not None else appointment.appointment_status
        appointment.appointment_description = appointment_description if appointment_description is not None else appointment.appointment_description
        appointment.appointment_type = appointment_type if appointment_type is not None else appointment.appointment_type
        appointment.appointment_category = appointment_category if appointment_category is not None else appointment.appointment_category
        appointment.staff_phone_number = staff_phone_number if staff_phone_number is not None else appointment.staff_phone_number
        appointment.student_phone_number = student_phone_number if student_phone_number is not None else appointment.student_phone_number

        appointment.save()
        return UpdateAppointment( appointment = appointment)


class DeleteAppointment(graphene.Mutation):

    class Arguments:

        id = graphene.ID()

    appointment = graphene.Field(appointment_type)

    def mutate(self, info, id):

        appointment = appointment.objects.get(pk=id)
        if appointment is not None:
            appointment.delete()
        return DeleteAppointment(appointment = appointment)





# -----------> TASK-TABLE-MUTATIONS----------

class CreateTask(graphene.Mutation):

    class  Arguments:

        task_issue_date= graphene.types.datetime.DateTime()
        # task_feedback_file= graphene.FileField()
        task_type=  graphene.String()
        task_description= graphene.String()
        staff_id= graphene.String()
        appointment_id= graphene.String()


    task = graphene.Field(task_type)

    def mutate(self, task_issue_date, task_type,
        task_description, staff_id, appointment_id, task_feedback_file = None):

        task = task.objects.create (

        task_issue_date= task_issue_date,
        task_feedback_file= task_feedback_file,
        task_type=  task_type,
        task_description=task_description,
        staff_id= staff_id,
        appointment_id= appointment_id)


        task.save()
        return CreateTask( task = task)


class UpdateTask(graphene.Mutation):

    class  Arguments:

        task_id= graphene.ID()
        # task_feedback_file= graphene.FileField()
        task_type=  graphene.String()
        task_description= graphene.String()
        staff_id= graphene.String()
        appointment_id= graphene.String()

    task = graphene.Field(task_type)

    def mutate(self, info, task_id, task_type = None,
        task_description= None, staff_id = None, task_feedback_file = None):

        task = task.objects.get(pk=task_id)

        task.task_type = task_type if task_type is not None else  task.task_type
        task.task_description = task_description if task_description is not None else task.task_task_description
        task.staff_id = staff_id if staff_id is not None else task.staff_id
        task.task_feedback_file = task_feedback_file if task_feedback_file is not None else task_feedback_file

        task.save()
        return UpdateTask( task = task)


class DeleteTask(graphene.Mutation):

    class Arguments:

        id = graphene.ID()

    task = graphene.Field(task_type)

    def mutate(self, info, id):

        task = task.objects.get(pk=id)
        if task is not None:
            task.delete()
        return DeleteTask(task = task)



# -----------> TASK-TABLE-MUTATIONS----------

class CreateUser(graphene.Mutation):

    class  Arguments:

        user_phone_number= graphene.Int()
        user_password=  graphene.String()


    user = graphene.Field(user_type)

    def mutate(self, user_phone_number,user_password):

        user = task.objects.create (

        user_phone_number= user_phone_number,
        user_password = user_password,
        )
        user.save()
        return CreateUser( user = user)


class UpdateUser(graphene.Mutation):

    class  Arguments:

        user_id = graphene.ID()
        user_phone_number= graphene.Int()
        user_password =  graphene.String()

    user = graphene.Field(user_type)

    def mutate(self, info, user_id, user_phone_number = None, user_password = None):

        user = user.objects.get(pk=user_id)

        user.user_phone_number = user_phone_number if user_phone_number is not None else  user.user_phone_number
        user.user_password = user_password if user_password is not None else user.user_password

        user.save()
        return UpdateUser( user = user)


class DeleteUser(graphene.Mutation):

    class Arguments:

        id = graphene.ID()

    user = graphene.Field(user_type)

    def mutate(self, info, id):

        user = user.objects.get(pk=id)
        if user is not None:
            user.delete()
        return DeleteUser(user = user)



class Mutation(graphene.ObjectType):

    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()

    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

    create_staff = CreateStaff.Field()
    update_staff = UpdateStaff.Field()
    delete_staff = DeleteStaff.Field()

    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()

    create_appointment = CreateAppointment.Field()
    update_appointment = UpdateAppointment.Field()
    delete_appointment = DeleteAppointment.Field()
