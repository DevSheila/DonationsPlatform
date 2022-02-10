from django.db import models

# Create your models here.
import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.forms import EmailField

class ConsumerManager(BaseUserManager):
    def create_user(self,email, Full_name, phone_number,Organization,location,category,facebook,Twitter,Website,no_individuals,password = None):
        if not email:
            raise ValueError(" Please provide the email")
        if not Full_name:
            raise ValueError(" Please provide your full name")
        if not phone_number:
            raise ValueError(" Please provide an active")
        if not Organization:
            raise ValueError(" Please provide the Organization")
        if not location:
            raise ValueError(" Please provide your location")
        if not category:
            raise ValueError(" Please provide your category")
        if not no_individuals:
            raise ValueError(" Please provide number individuals")

        user = self.model(
            email = self.normalize_email(email),
            Full_name = Full_name,
            phone_number = phone_number,
            Organization = Organization,
            location  = location,
            category = category,
            no_individuals =no_individuals,
            facebook = facebook,
            Twitter = Twitter,
            Website = Website

        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self,email,Full_name,phone_number,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            Full_name = Full_name,
            phone_number= phone_number,
            password= password
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class Consumer(AbstractBaseUser):
    Full_name = models.CharField(verbose_name='enter full name', max_length=60,unique=False)
    email = models.EmailField(verbose_name='enter valid email',max_length=60,unique=True)
    phone_number = models.CharField(verbose_name='enter phone number',max_length=20,unique=True)
    Organization = models.CharField(max_length=60, verbose_name= 'Organization')
    CAT = (
        ('Childrens Home','Childrens Home'),
        ('Eldery shelter','Eldery shelter'),
        ('Refugee Camp','Refugee Camp'),
        ('Street Families','Street Families')
    )
    category = models.CharField(max_length=100, verbose_name= 'category', choices= CAT)
    no_individuals = models.IntegerField()
    facebook = models.CharField(max_length=300,verbose_name='facebook',null=True)
    Twitter = models.CharField(max_length=300,verbose_name='Twitter',null=True)
    Website = models.CharField(max_length=300,verbose_name='Website',null=True)
    location = models.CharField(max_length=40, verbose_name= ' Enter your current location')
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELD = ['Full_name','phone_number','Organization','category','location','no_individuals']

    objects=ConsumerManager()
    def __str__(self):
        return self.Full_name


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True