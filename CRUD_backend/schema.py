import graphene
from graphene_django import DjangoObjectType
from CRUD_backend.models import student, appointment, task, staff, users



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

class  users_type(DjangoObjectType):
    class Meta:
        model = users



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


    all_users = graphene.List(users_type)
    user = graphene.Field(users_type, id=graphene.ID())

    def resolve_all_users(self, info, **kwargs):
        # a resolver fuction to return all users of the system
        return users.objects.all()
    def resolve_user(self, info, id):
        # a function to return a single selected user
        return users.objects.get(pk=id)



#******************* MUTATIONS *************************#



# -----------> STUDENT-MUTATIONS----------

class create_student(graphene.Mutation):

    class  Arguments:
        student_reg_number = graphene.String()
        student_first_name = graphene.String()
        student_middle_name = graphene.String()
        student_surname = graphene.String()
        student_degree_program = graphene.String()
        student_gender = graphene.String()

    student = graphene.Field(student_type)

    def mutate(self, info, student_reg_number, student_first_name , student_middle_name, student_surname, student_degree_program,student_gender):

        student = student.objects.create(
            student_reg_number = student_reg_number,
            student_first_name = student_first_name,
            student_middle_name = student_middle_name,
            student_surname =student_surname,
            student_degree_program = student_degree_program,
            student_gender=student_gender)

        student.save()
        return create_student( student = student)


class update_student(graphene.Mutation):

    class  Arguments:
        student_reg_number = graphene.String()
        student_first_name = graphene.String()
        student_middle_name = graphene.String()
        student_surname = graphene.String()
        student_degree_program = graphene.String()
        student_gender = graphene.String()

    student = graphene.get(student_type)

    def mutate(self, info, student_reg_number=None, student_first_name =None, student_middle_name=None, student_surname =None, student_degree_program =None, student_gender =None):

        student = student.objects.get(pk=student_reg_number)

        student.student_first_name = student_first_name if student_first_name is not None else student.student_first_name
        student.student_middle_name = student_middle_name if student_middle_name is not None else student.student_middle_name
        student.student_surname =student_surname if student_surname is not None else student.student_surname
        student.student_degree_program = student_degree_program if student_degree_program is not None else student.student_degree_program
        student.student_gender=student_gender if student_gender is not None else student.student_gender

        student.save()
        return update_student( student = student)


class delete_student(graphene.Mutation):

    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    student = graphene.get(student_type)

    def mutate(self, info, id):

        student = student.objects.get(pk=id)
        if student is not None:
            student.delete()
        return delete_student(student = student)