# Generated by Django 4.1.3 on 2022-11-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='User Email_Id')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('iduser', models.AutoField(primary_key=True, serialize=False, verbose_name='idUser')),
                ('user_name', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='User name')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='address')),
                ('state', models.CharField(max_length=45, verbose_name='State')),
                ('city', models.CharField(max_length=45, verbose_name='City')),
                ('password', models.CharField(max_length=45, verbose_name='Password')),
                ('pincode', models.IntegerField(verbose_name='Pincode')),
                ('phone_number', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Phone Number')),
                ('profile_image', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Profile Image')),
                ('user_bio', models.TextField(blank=True, null=True, verbose_name='User bio')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
