# Generated by Django 3.0.5 on 2022-04-30 12:42

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('appointment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('appointment_type', models.CharField(max_length=20)),
                ('appointment_category', models.CharField(max_length=10)),
                ('appointment_description', models.CharField(max_length=200)),
                ('appointment_time', models.TimeField()),
                ('appointment_date', models.DateField()),
                ('staff_phone_number', models.IntegerField()),
                ('student_phone_number', models.IntegerField()),
                ('appointment_status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('staff_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('staff_first_name', models.CharField(max_length=100)),
                ('staff_middle_name', models.CharField(max_length=100, null=True)),
                ('staff_surname', models.CharField(max_length=100)),
                ('staff_office', models.CharField(max_length=100)),
                ('staff_role', models.CharField(max_length=100)),
                ('staff_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('student_reg_number', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('student_first_name', models.CharField(max_length=100)),
                ('student_middle_name', models.CharField(max_length=100, null=True)),
                ('student_surname', models.CharField(max_length=100)),
                ('student_degree_program', models.CharField(max_length=100)),
                ('student_fingerprint_id', models.CharField(max_length=100)),
                ('student_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('task_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('task_issue_date', models.DateField()),
                ('task_deadline_date', models.DateField()),
                ('task_feedback_file', models.CharField(max_length=100, null=True)),
                ('task_type', models.CharField(max_length=100)),
                ('task_description', models.CharField(max_length=100)),
                ('appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD_backend.appointment')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD_backend.staff')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD_backend.staff'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='student_reg_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD_backend.student'),
        ),
    ]
