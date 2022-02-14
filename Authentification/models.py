import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.forms import EmailField

class AllUsersManager(BaseUserManager):
    def create_user(self,email, Full_name, phone_number,Organization,sign_up_as,location,password = None):
        if not email:
            raise ValueError(" Please provide the email")
        if not Full_name:
            raise ValueError(" Please provide your full name")
        if not phone_number:
            raise ValueError(" Please provide an active")
        if not location:
            raise ValueError(" Please provide your location")

        user = self.model(
            email = self.normalize_email(email),
            Full_name = Full_name,
            phone_number = phone_number,
            Organization = Organization,
            location = location,
            sign_up_as = sign_up_as
            

        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self,email,Full_name, phone_number,Organization,sign_up_as,location,password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            Full_name = Full_name,
            phone_number = phone_number,
            Organization = Organization,
            location = location,
            sign_up_as = sign_up_as,
            password = password
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class AllUsers(AbstractBaseUser,PermissionsMixin):
    Full_name = models.CharField(verbose_name='enter full name', max_length=60,unique=False)
    email = models.EmailField(verbose_name='enter valid email',max_length=60,unique=True)
    phone_number = models.CharField(verbose_name='enter phone number',max_length=20,unique=True)
    gn =(
        ('Donor','Donor'),
        ('Donee','Donee')
    )
    sign_up_as = models.CharField(max_length=20, choices=gn)
    ORG = (
        ('Individual','Individual'),
        ('Organization','Organization'),
        ("               ","               ")
    )
    Organization = models.CharField(max_length=60, verbose_name= 'Organization', choices= ORG)
    donee_name = models.CharField(max_length=50,verbose_name= 'Enter name of you donee organization',blank=True)
    CAT = (
        ("Childrens Home","Childrens Home"),
        ("Eldrey Shelter","Eldrey Shelter"),
        ("Street Families","Street Families"),
        ("               ","               ")
        )
    donee_category = models.CharField(max_length=50,choices=CAT,verbose_name= 'Donee category',null=True)
    facebook = models.CharField(max_length=300,verbose_name='Facebook',blank=True)
    no_individuals = models.IntegerField(blank=True, null=True)
    twitter = models.CharField(max_length=300,verbose_name='Twitter',blank=True)
    website = models.CharField(max_length=300,verbose_name='Website',blank=True)
    location = models.CharField(max_length=40, verbose_name= ' Enter your current location')
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['Full_name','phone_number','Organization','location','sign_up_as']

    objects=AllUsersManager()
    def __str__(self):
        return self.Full_name


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
        