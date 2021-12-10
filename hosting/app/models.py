from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

# Create your models here.
#  class registering(models.Model):
#     email = models.CharField(max_length=100)
#     year=models.IntegerField(max_length =4, default = 2024, null = True)
#     branch=models.CharField(max_length=3, default='CSE')
#     username=models.CharField(max_length=500)
#     password=models.CharField(max_length=20)
#     confirm_your_password=models.CharField(max_length=20, default=' ')


class UserManager(BaseUserManager):
    def create_user(self, email, branch, username, year, password = None, is_active=True, is_staff = False, is_admin= False): #make things which are mandatory
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users require passowrd")
        user_obj = self.model(
            email = self.normalise_email(email)
        )
        user_obj.set_password(password) #to change password
        user_obj.staff= is_staff
        user_obj.admin=is_admin
        user_obj.active = is_active

        user_obj.year= year
        user_obj.username= username
        user_obj.branch= branch
        # user_obj = UserManager()
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password= None):
        user = self.create_user(
            email, 
            password=password, 
            is_staff=True,      
            is_admin=True

            )
        return user

    def create_superuser(self, email, branch, username, year, password= None):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users require passowrd")
        user_obj = self.model(
            email = self.normalise_email(email)
        )
        user_obj.set_password(password) #to change password
        user_obj.year= year
        user_obj.username= username
        user_obj.branch= branch
        # user_obj = UserManager()
        user_obj.save(using=self._db)
        return user_obj


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, default=None, unique=True) 
    year=models.IntegerField(max_length =4, default = 2024, null = False)
    branch=models.CharField(max_length=3, default = 'CSE', null=False)
    username=models.CharField(max_length=500, null = False)
    # printf("vedant")
    is_active = models.BooleanField(default = True) #can login
    is_staff = models.BooleanField(default = False) #non superuser
    is_admin = models.BooleanField(default = False) #superuser

    user_obj = UserManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELD =['year', 'branch', 'username']

    def __str__(self):
        return self.username 
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class AppCourse(models.Model):
    ccode = models.CharField(primary_key=True, max_length=10)
    dept = models.ForeignKey('AppDepartment', models.DO_NOTHING, db_column='dept', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'app_course'


class AppDepartment(models.Model):
    dept = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = True
        db_table = 'app_department'


class linklesson(models.Model):
    time_phase = models.CharField(max_length=20)
    period_no = models.IntegerField(default=1)


class lesson(models.Model):
    year=models.IntegerField(max_length =4, default = 2024, null = True)
    branch=models.CharField(max_length=3, default = 'CSE')
    period_day = models.CharField(max_length=10)
    subject_id = models.CharField(max_length=15, null = True)
    gmeet_link = models.CharField(max_length=1000, null = True)
    period_no = models.ForeignKey(linklesson, on_delete=models.SET_NULL, null=True)
    teacher_name=models.CharField(max_length = 50, null = True)




    
    # @property
    # def is_staff(self):
    #     return self.is_staff

    

    # @property
    # def is_admin(self):
    #     return self.is_admin


    # @property
    # def is_active(self):
    #     return self.is_active


class AppPYQ(models.Model):
    id=models.IntegerField(primary_key=True)
    q_year=models.IntegerField(blank=True,null=True)
    link=models.CharField(max_length=3000)
    ccode=models.ForeignKey(AppCourse,on_delete=models.DO_NOTHING)
    qtype=models.CharField(max_length=10)


class author(models.Model):
    aname=models.CharField(max_length=300)
    class Meta:
        ordering=['aname']
    
genre_choices=[
    ('NF','Non-Fiction'),
    ('F','Fiction'),
    ('Th','Thriller'),
    ('AA','Acrion and Adventure'),
    ('C','Comic'),
    ('BG','Biographies and Autobiographies'),
    ('CLB','College Level Books'),
]   


class Books(models.Model):
    
    name=models.CharField(max_length=100)
    author=models.ManyToManyField(author)
    genre=models.CharField(max_length=100,choices=genre_choices,default='CLB')    
    available=models.BooleanField(default=True)
    img=models.ImageField(upload_to='pics',null=True)


class Lends(models.Model):
    bid=models.ForeignKey(Books, on_delete=models.DO_NOTHING)
    lender=models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Borrower(models.Model):
    bid=models.ForeignKey(Books,on_delete=models.DO_NOTHING)
    borrower=models.ForeignKey(User,on_delete=models.DO_NOTHING)


class post(models.Model):
    user_id =  models.ForeignKey(User, models.DO_NOTHING)
    post_text = models.CharField(max_length=500)
    post_date = models.DateTimeField((u"Conversation Date"), auto_now_add=True, blank=True)
    post_img=models.ImageField(upload_to='pics',null=True)
    # post_video = models.FileField(upload_to='videos/' , null=True)
    likes=models.IntegerField(max_length=1000, default=0, null = True)
    dislikes=models.IntegerField(max_length=1000, default=0, null = True)



class todo (models.Model):
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    reminder_date = models.DateTimeField(auto_now_add=False, auto_now = False, null = False, default= None)
    todo_text = models.CharField(max_length=1000)

class notification(models.Model):
    receiver=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    sender=models.CharField(max_length=100)
    book=models.ForeignKey(Books,on_delete=models.DO_NOTHING, unique=True)
    response=models.BooleanField(default=False)


# class Comment(models.Model):
#     ''' Main comment model'''
#     user =  models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
#     comment = models.CharField(max_length=1000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def get_total_likes(self):
#         return self.likes.users.count()

#     def get_total_dis_likes(self):
#         return self.dis_likes.users.count()

#     def __str__(self):
#         return str(self.comment)[:30]


# class Like(models.Model):
#     ''' like  comment '''

#     comment = models.OneToOneField(Comment, related_name="likes", on_delete=models.CASCADE)
#     users = models.ManyToManyField(User, related_name='requirement_comment_likes')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.comment.comment)[:30]

# class DisLike(models.Model):
#     ''' Dislike  comment '''

#     comment = models.OneToOneField(Comment, related_name="dis_likes", on_delete=models.CASCADE)
#     users = models.ManyToManyField(User, related_name='requirement_comment_dis_likes')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.comment.comment)[:30]