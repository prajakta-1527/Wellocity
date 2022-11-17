from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
import django
# Create your models here.
django.contrib.auth.base_user 
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import NoiceUser
class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, password,first_name, **other_fields):
        email=self.normalize_email(email)
        if not email:
            raise ValueError(_('You must provide an email address'))

        user = self.model(
            email=email,user_name=user_name,first_name=first_name,**other_fields
           
        )

        user.set_password(password)
        # user.save(using=self._db)
        user.save()
        return user
    
    def create_superuser(self, email, first_name, password,**other_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff' ) is not True:
             raise ValueError(_('superuser must be assigned to is_staff=true'))
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,**other_fields
        )
        user.is_admin = True
        # user.save(using=self._db)
        return user

import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
# from cloudinary.models import CloudinaryFileField
# class User1(models.Model):
#     iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
#     user_name = models.CharField(max_length=250)
#     user_email_id = models.CharField(db_column='User Email_Id', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     address = models.CharField(max_length=250, blank=True, null=True)
#     state = models.CharField(db_column='State', max_length=45)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=45)  # Field name made lowercase.
#     pincode = models.IntegerField(db_column='Pincode')  # Field name made lowercase.
#     phone_number = models.IntegerField(db_column='Phone Number', blank=True, null=True)  
#     profile_image = models.FileField(db_column='Profile Image',upload_to='blog-post-images',blank=True, null=True)# Field name made lowercase. Field renamed to remove unsuitable characters.
#     # profile_image = models.CharField(db_column='Profile Image', max_length=2048, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     user_bio = models.TextField(db_column='User bio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     first_name = models.CharField(max_length=45)
#     last_name = models.CharField(max_length=45, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user1'

# class User2(models.Model):
#     iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
#     user_name = models.CharField(max_length=250)
#     user_email_id = models.CharField(db_column='User Email_Id', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     address = models.CharField(max_length=250, blank=True, null=True)
#     state = models.CharField(db_column='State', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     pincode = models.IntegerField(db_column='Pincode', blank=True, null=True)  # Field name made lowercase.
#     phone_number = models.IntegerField(db_column='Phone Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     profile_image = models.FileField(db_column='Profile Image',upload_to='blog-post-images',blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     user_bio = models.TextField(db_column='User bio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     first_name = models.CharField(max_length=45, blank=True, null=True)
#     last_name = models.CharField(max_length=45, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user2'


class User3(models.Model):
    iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    auth_id = models.IntegerField()
    user_name = models.CharField(max_length=250)
    user_email_id = models.CharField(db_column='User Email_Id', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pincode = models.IntegerField(db_column='Pincode', blank=True, null=True)  # Field name made lowercase.
    phone_number = models.IntegerField(db_column='Phone Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # profile_image = CloudinaryField('imgs',db_column='Profile Image')
    profile_image=models.ImageField(upload_to='images/',db_column='Profile Image', blank=True, null=True)
    # profile_image = models.FileField(db_column='Profile Image',upload_to='blog-post-images',blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_bio = models.TextField(db_column='User bio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user3'

class User(AbstractBaseUser,PermissionsMixin):
    first_name= models.CharField(blank=True, max_length=150 )
    last_name= models.CharField(blank=True, max_length=150)
    email= models.EmailField(_('User Email_Id'),unique=True, max_length=254)
    is_staff=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')
    is_active= models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    # date_joined= models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')
    iduser= models.AutoField(_('idUser'), primary_key=True, serialize=False)
    # iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    #validators=[django.contrib.auth.validators.UnicodeUsernameValidator()]
    user_name = models.CharField(_('User name'), error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # user_email_id = models.CharField(db_column='User Email_Id', max_length=50, blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address = models.CharField(_('address'),max_length=250, blank=True, null=True)
    state = models.CharField(_('State'), max_length=45,blank=True,null=True)  # Field name made lowercase.
    city = models.CharField(_('City'), max_length=45,blank=True,null=True)  # Field name made lowercase.
    # password = models.CharField(_('Password'), max_length=145,null=False)  # Field name made lowercase.
    pincode = models.IntegerField(_('Pincode'),blank=True,null=True)  # Field name made lowercase.
    phone_number = models.IntegerField(_('Phone Number'), blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profile_image = models.CharField(_('Profile Image'), max_length=2048, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_bio = models.TextField(_('User bio'), blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name']
    objects=CustomAccountManager()

    def __str__(self):
        return self.user_name



# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey('NoiceUser', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class NoiceUser(models.Model):
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(unique=True, max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     iduser = models.AutoField(primary_key=True)
#     user_name = models.CharField(unique=True, max_length=150)
#     address = models.CharField(max_length=250, blank=True, null=True)
#     state = models.CharField(max_length=45, blank=True, null=True)
#     city = models.CharField(max_length=45, blank=True, null=True)
#     password = models.CharField(max_length=128)
#     pincode = models.IntegerField(blank=True, null=True)
#     phone_number = models.IntegerField(blank=True, null=True)
#     profile_image = models.CharField(max_length=2048, blank=True, null=True)
#     user_bio = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'noice_user'


# class NoiceUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(NoiceUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'noice_user_groups'
#         unique_together = (('user', 'group'),)


# class NoiceUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(NoiceUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'noice_user_user_permissions'
#         unique_together = (('user', 'permission'),)

# from django.contrib.auth.models import NoiceUser

#deleted user
# from django.conf import settings
# class OrderDetails(models.Model):
#     idorder = models.AutoField(db_column='idOrder', primary_key=True)  # Field name made lowercase.
#     date_of_order = models.DateTimeField(db_column='Date of order')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
#     user_username = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='User_username', to_field='user_name')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'order details'

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AskADoctor(models.Model):
    idask_a_doctor = models.AutoField(db_column='idAsk a Doctor', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    question = models.CharField(db_column='Question', max_length=200, blank=True, null=True)  # Field name made lowercase.
    answer = models.TextField(db_column='Answer', blank=True, null=True)  # Field name made lowercase.
    domain = models.CharField(db_column='Domain', max_length=45)  # Field name made lowercase.
    doctor_iddoctor = models.ForeignKey('Doctor', models.DO_NOTHING, db_column='Doctor_idDoctor')  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ask a doctor'

    def __str__(self):
        return(self.idask_a_doctor)


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


class Category(models.Model):
    idcategory = models.AutoField(db_column='idCategory', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'

    def __str__(self):
        return(self.category)
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey('NoiceUser', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


class Doctor(models.Model):
    iddoctor = models.AutoField(db_column='idDoctor', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    specialisation = models.CharField(db_column='Specialisation', max_length=45)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email ID', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_no_field = models.IntegerField(db_column='Phone No.')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    state = models.CharField(db_column='State', max_length=45)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45)  # Field name made lowercase.
    pincode = models.IntegerField(db_column='Pincode')  # Field name made lowercase.
    experience_yrs_field = models.IntegerField(db_column='Experience(yrs)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    photo = models.CharField(db_column='Photo', max_length=2048, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctor'
    def __str__(self):
        return(self.name)

class Faq(models.Model):
    idfaq = models.AutoField(db_column='idFAQ', primary_key=True)  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=200)  # Field name made lowercase.
    answer = models.TextField(db_column='Answer')  # Field name made lowercase.
    subcategory_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faq'
    


class HealthArticles(models.Model):
    idhealth_articles = models.AutoField(db_column='idHealth Articles', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    heading = models.CharField(db_column='Heading', max_length=100)  # Field name made lowercase.
    photo = models.CharField(db_column='Photo', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    subcategory_id = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'health articles'

class Inventory(models.Model):
    idinventory = models.AutoField(db_column='idInventory', primary_key=True)  # Field name made lowercase.
    expiry_date = models.DateTimeField(db_column='Expiry Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    quantity_sold_this_month = models.IntegerField(db_column='Quantity Sold this Month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sub_category_id_sub_category = models.ForeignKey('SubCategory', models.DO_NOTHING, db_column='Sub Category_id_Sub Category')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'inventory'
    

class Manufacturer(models.Model):
    idmanufacturer = models.AutoField(db_column='idManufacturer', primary_key=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company Name', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.
    phone_number = models.IntegerField(db_column='Phone number', unique=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manufacturing_headquarters = models.CharField(db_column='Manufacturing Headquarters', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'manufacturer'
    def __str__(self):
        return(self.company_name)

# class NoiceUser(models.Model):
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(unique=True, max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     iduser = models.AutoField(primary_key=True)
#     user_name = models.CharField(unique=True, max_length=150)
#     address = models.CharField(max_length=250, blank=True, null=True)
#     state = models.CharField(max_length=45, blank=True, null=True)
#     city = models.CharField(max_length=45, blank=True, null=True)
#     password = models.CharField(max_length=128)
#     pincode = models.IntegerField(blank=True, null=True)
#     phone_number = models.IntegerField(blank=True, null=True)
#     profile_image = models.CharField(max_length=2048, blank=True, null=True)
#     user_bio = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'noice_user'


# class NoiceUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(NoiceUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'noice_user_groups'
#         unique_together = (('user', 'group'),)


# class NoiceUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(NoiceUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'noice_user_user_permissions'
#         unique_together = (('user', 'permission'),)


class OrderDetails(models.Model):
    idorder = models.AutoField(db_column='idOrder', primary_key=True)  # Field name made lowercase.
    date_of_order = models.DateTimeField(db_column='Date of order')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    date_of_delivery = models.DateTimeField(db_column='Date of Delivery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order details'
    

class OrderItems(models.Model):
    idorder_details = models.AutoField(db_column='idOrder details', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quantity = models.IntegerField()
    order_details_idorder = models.ForeignKey(OrderDetails, models.DO_NOTHING, db_column='Order Details_idOrder')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    price = models.IntegerField()
    product_id = models.IntegerField(db_column='Product_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order items'
    

class Payment(models.Model):
    idpayment_details = models.AutoField(db_column='idPayment Details', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=45)  # Field name made lowercase.
    type_of_payment = models.CharField(db_column='Type of payment', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_of_payment = models.DateTimeField(db_column='Time of Payment', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_details_idorder = models.ForeignKey(OrderDetails, models.DO_NOTHING, db_column='Order Details_idOrder', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'payment'
    

class Product(models.Model):
    idproduct = models.AutoField(db_column='idProduct', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    number_of_purchases = models.IntegerField(db_column='Number of purchases', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    desciption = models.TextField(db_column='Desciption', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    discounted_price = models.IntegerField(db_column='Discounted price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.
    manufacturer_idmanufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='Manufacturer_idManufacturer', blank=True, null=True)  # Field name made lowercase.
    sub_category_id_sub_category = models.ForeignKey('SubCategory', models.DO_NOTHING, db_column='Sub Category_id_Sub Category', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'product'
    def __str__(self):
        return(self.product_name)

class Rating(models.Model):
    idrating = models.AutoField(db_column='idRating', primary_key=True)  # Field name made lowercase.
    rating = models.IntegerField()
    product_id = models.IntegerField(db_column='Product_id')  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rating'
    

class Reviews(models.Model):
    idreviews = models.AutoField(db_column='idReviews', primary_key=True)  # Field name made lowercase.
    reviews = models.TextField(db_column='Reviews')  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id')  # Field name made lowercase.
    product_id = models.IntegerField(db_column='Product_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reviews'
   

class ShoppingCart(models.Model):
    id_cart = models.AutoField(db_column='id cart', primary_key=True)  # Field renamed to remove unsuitable characters.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shopping cart'
    

class ShoppingCartItems(models.Model):
    idshopping_cart_items = models.AutoField(db_column='idShopping Cart items', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    shopping_cart_id_cart = models.ForeignKey(ShoppingCart, models.DO_NOTHING, db_column='Shopping cart_id cart')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    product_id = models.IntegerField(db_column='Product_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shopping cart items'


    
class SubCategory(models.Model):
    sub_category = models.CharField(db_column='Sub Category', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_sub_category = models.AutoField(db_column='id_Sub Category', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    category_idcategory = models.ForeignKey(Category, models.DO_NOTHING, db_column='Category_idCategory')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub category'
    def __str__(self):
        return(self.sub_category)

class Wishlist(models.Model):
    idwishlist = models.AutoField(db_column='idWishlist', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wishlist'
    

class WishlistItems(models.Model):
    idwishlist_items = models.AutoField(db_column='idWishlist items', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wishlist_idwishlist = models.ForeignKey(Wishlist, models.DO_NOTHING, db_column='Wishlist_idWishlist')  # Field name made lowercase.
    product_id = models.IntegerField(db_column='Product_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wishlist items'
   