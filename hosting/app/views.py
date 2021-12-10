from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from app.models import User, post, lesson,todo
# from app.models import  post
from app.models import *
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .forms import RegisterForm

student=None
vcode=None

getemail = None
# from django.contrib.auth import logout


def base(request):
    return render(request, 'base.html')


# def signin(request):
#     print("aryan")
#     print("hi bro
#     if request.method == 'POST':
#         print("in if statement 111")
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print("done 2")
#         temp = register_user.objects.filter(email=email)
#         if password == temp[0].password:
#             user = temp[0]
#         else:
#             user = None

#         print(email, password)
#         # user = authenticate(email=email , password = password)
#         print("lol")
#         if user is not None:
#             print("again here")
#             # login(request, user)

#             username = user.username
#             return render(request, "home.html", {'username': username})

#         else:
#             print("oh no no")

#             messages.error(request, "Incorrect Credentials :( Try Again !")

#     return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated:
        
        if request.method=="POST":
            id_td=str(request.POST.get('id')).strip()
            todo.objects.get(id=int(id_td)).delete()

        if request.user.year == 2024 and request.user.branch =='CSE': #for cse 2024
            timetable_cse_1 = lesson.objects.filter(year=2024, branch = 'CSE', period_no_id=1)
            timetable_cse_2 = lesson.objects.filter(year=2024, branch = 'CSE', period_no_id=2)
            timetable_cse_3 = lesson.objects.filter(year=2024, branch = 'CSE', period_no_id=3)
            timetable_cse_4 = lesson.objects.filter(year=2024, branch = 'CSE', period_no_id=4)
            timetable_cse_5 = lesson.objects.filter(year=2024, branch = 'CSE', period_no_id=5)
            timetable_cse_6 = lesson.objects.filter(year=2024, branch = 'CSE', period_no_id=6)
            timetable_cse_7 = lesson.objects.filter(year=2024, branch = 'CSE', period_no_id=7)
            timetable_cse_8 = lesson.objects.filter(year=2024, branch = 'CSE', period_no_id=8)
            timetable_cse_9 = lesson.objects.filter(year=2024, branch = 'CSE', period_no_id=9)

            #for todo: 
            todo_cse = todo.objects.filter(user_id = request.user.id)
            
            return render(request, 'home.html', {'todo_cse': todo_cse, 'data_cse_1': timetable_cse_1, 'data_cse_2':timetable_cse_2, 'data_cse_3':timetable_cse_3, 'data_cse_4':timetable_cse_4, 'data_cse_5':timetable_cse_5, 'data_cse_6':timetable_cse_6, 'data_cse_7':timetable_cse_7, 'data_cse_8':timetable_cse_8, 'data_cse_9':timetable_cse_9})

        else:
            return render(request,'home.html')
    else:
        return redirect('/')



# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # print("vedu")
#             return redirect ('login')
        
#         else:
#             # print("in else 1")
#             form =RegisterForm(request.POST)
#             return render(request, 'register.html', {"form":form})
    
#     else:
#         # print("bade walal")
#         form = RegisterForm()
#         return render(request, 'register.html', {"form":form})

def sendmail(mail):
    import smtplib,random
    from email.message import EmailMessage
    mail=str(student.cleaned_data['email'])
    code=str(random.randint(10000,99999))
    global vcode
    vcode=code
    content="Your verification code is: "+code

    msg = EmailMessage()
    msg.set_content(content)

    msg['Subject'] = 'Blackboard-User Verification '
    msg['From'] = "blackboardaryanaarya@gmail.com"
    msg['To'] = mail
     # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("blackboardaryanaarya@gmail.com", "aaryadurba")
    server.send_message(msg)
    server.quit()
     

def verification(request):
    if request.method=='GET':
        global student
        mail=str(student.cleaned_data['email'])
        print(mail,request)
        sendmail(mail)
    
    if request.method == 'POST':
        c=request.POST.get('code')
        print(c,vcode)
        if str(c).strip()==vcode:
            # global student
            student.save()
            return redirect ('login')
    return render(request, 'verification.html')





 
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        global student 
        student=form
        if form.is_valid():
            return redirect('verification')
        
        else:
            form =RegisterForm(request.POST)
            return render(request, 'register.html', {"form":form})
    
    else:
        form = RegisterForm()
        return render(request, 'register.html', {"form":form})


def search_book(request):
    genre_choices={
    'NF':'Non-Fiction',
    'F':'Fiction',
    'Th':'Thriller',
    'AA':'Acrion and Adventure',
    'C':'Comic',
    'BG':'Biographies and Autobiographies',
    'CLB':'College Level Books'
    }   
   
    if request.method=="POST":
        print("here")
        searched=request.POST['searched']
        gen=request.POST.get('genre',None)
        searched=searched.strip()
        if gen:
            datas = Books.objects.filter(name__icontains=searched,available=True,genre=gen)
        else:
            datas = Books.objects.filter(name__icontains=searched,available=True)
        if datas:
            for data in datas:
                print(data.author.all())
                print(data.id)
                data.name=str(data.name).strip()                
                data.genre=str(data.genre).strip()
                data.genre=genre_choices[data.genre]
            return render(request, 'search_book.html',{"bk":datas})

    return render(request, 'search_book.html')


def book_url_response(request,my_id,*args,**kwargs):
    if request.user.is_authenticated:

        bdts=Books.objects.get(id=my_id)
        bdts.available=False
        gen=bdts.genre
        bdts.save(update_fields=['available'])
        borrow=Borrower(bid=bdts,borrower=request.user)
        similar_books=Books.objects.filter(genre=gen,available=True)[:3]
        borrow.save()
        print(similar_books)
        return render(request,"detail.html",{'book':bdts, 'sim_b':similar_books})


def addbook(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            a_name=request.POST.get('aname1')
            a_name2=request.POST.get('aname2',None)
            bname=request.POST.get('book_name')
            book_genre=request.POST.get('genre')
            img_link=request.POST.get('picture')
            writer=author(aname=a_name)
            writer.save()
            print(request.POST)
            book=Books(name=bname, genre=book_genre, img=img_link)
            book.save()
            book.author.add(writer)
            lender=Lends(bid=book,lender=request.user)
            lender.save()
            if a_name2:
                writer2=author(aname=a_name2)
                writer2.save()
                book.author.add(writer2)
            return render(request,'book_add_success.html',{'name':bname})
        else:
            return render(request,'addbook.html')
        # aform=GetAuthor()
        
        # form=BookForm()
        # if request.method=='POST':
        #     try:
        #         auth_name=request.POST["aname"]
        #         aform=GetAuthor(request.POST)
        #     if aform.is_valid():
        #         aform.save
            # form=BookForm(request.POST)
            # if form.is_valid() :
            #     form.save()
            #     return 
           
    else:
        return redirect('/')





def sstest(request):
    if request.user.is_authenticated:
        return render(request, 'successful_entry.html')
    else:
        return redirect('/')

# def loginuser(request):
#     print("i am here")
#     form = AuthenticationForm(request.POST)
#     print(form)
#     if request.method == 'POST':
#         print("suar")
#         loginsuccess = authenticate(request, username = request.POST.get(''), password = request.POST.get(''))
#         if loginsuccess is None:
#             print("sabse bada wala")
#             return render(request, 'login.html', {'form':form,'error':'Username or Password are incorrect'})
#         else:
#             print("good job")
#             login(request, loginsuccess)
#             return redirect('home.html')

#     else:
#         return render(request, 'login.html', {'form':form})

def book_success(request):
    if request.user.is_authenticated():
        return render(request,'book_add_success.html')
    else:
        return redirect('/')


def pyq(request):
    # print("jio")
    if request.user.is_authenticated:
        print('user is authenticated')
        if request.method=="POST":
            # print('in post')
            searched=request.POST['searched']
            searched=searched.strip()
            datas = AppPYQ.objects.filter(ccode__ccode__icontains=searched)
            # ccodes=list()
            # link=list()
            # years
            # values=[]
            for data in datas:
                
                
                data.link=str(data.link).strip()
                data.q_year=str(data.q_year).strip()
                data.qtype=str(data.qtype).strip()
                data.qtype="End Semester" if data.qtype=="ES" else "Mid Semester"
            return render(request, 'pyq.html',{"qp":datas})
        
        return render(request, 'pyq.html')

    else:
        return redirect('/')    

    # return render(request, 'pyq.html')


def sm_pg1(request):
    if request.user.is_authenticated:
        return render(request, 'sm_pg1.html')
    else:
        return redirect('/')

    # return render(request, 'social_media_entry.html')


def sm_pg2(request):
    if request.user.is_authenticated:
        print("chicken")
        if request.method == "POST":
            post_text = request.POST.get('post_text')
            # print('yaaaaaar')
            post_img = request.FILES.getlist('post_img')
            # post_video = request.FILES.getlist('post_video')
            if len(post_img) != 0:
                post_img = post_img[0]
            else:
                post_img = None
            # post_video = post_video[0]
            # print(post_img)
            posties = post(user_id=request.user, post_text=post_text, post_img=post_img)
            posties.save()
            print("done")
            messages.success(request, "Your post has been succesfully created.")
            return redirect('sm_pg1')
    # return render(request, 'sm_pg2.html')
    else:
        return redirect('/')
        
    return render(request, 'sm_pg2.html')



def sm_post(request):
    if request.user.is_authenticated:
        print("user is authenticated")
        posts = post.objects.all()
        for i in posts:
            setattr(i, 'username', i.user_id.username) #user_id is a foreign key so it brings the whole obj

        return render(request, 'sm_post.html', {'data':posts})
    else:
        print("else")
        return redirect('/')

def likes(request, post_id):
    if request.method=='POST':
        print("post")
        post.objects.filter(id=post_id).update(likes=post.objects.filter(id=post_id)[0].likes+1)
        print("here")
        return redirect('sm_post')

def dislikes(request, post_id):
    if request.method=='POST':
        print("post")
        post.objects.filter(id=post_id).update(dislikes=post.objects.filter(id=post_id)[0].dislikes+1)
        print("here")
        return redirect('sm_post')




def succesfull_entry(request):
    if request.user.is_authenticated:
        return render(request, 'successful_entry.html')
    else:
        return redirect('/')



def todo_fn(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            reminder_date = request.POST.get('reminder_date')
            todo_text = request.POST.get('todo_text')
            print("hi i am here")
            notif_todo = todo(user_id=request.user, reminder_date=reminder_date ,todo_text=todo_text)
            notif_todo.save()
            return redirect('home')

    else:
        return redirect('/')

    return render(request, 'todo.html')       

  
# from django.contrib.auth.mixins import LoginRequiredMixin

# class Requirement(request):
#     form_class = forms.CommentForm
#     template_name = 'ktu/comment.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         comment = models.Comment.objects.all()

#         context = {}
#         context['page_obj'] = comment
#         context['form'] = form

#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             comment_form = form.save(commit=False)
#             comment_form.user = request.user
#             comment_form.save()
#             messages.success(request, 'Your comment successfully addedd')

#             return HttpResponseRedirect(Reversible('comment'))
        
#         context = {}
#         context['form'] = form

#         return render(request, self.template_name, context)
      
      
# class UpdateCommentVote(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'next'

#     def get(self, request, *args, **kwargs):

#         comment_id = self.kwargs.get('comment_id', None)
#         opinion = self.kwargs.get('opinion', None) # like or dislike button clicked

#         comment = ge t_object_or_404(models.Comment, id=comment_id)

#         try:
#             # If child DisLike model doesnot exit then create
#             comment.dis_likes
#         except models.Comment.dis_likes.RelatedObjectDoesNotExist as identifier:
#             models.DisLike.objects.create(comment = comment)

#         try:
#             # If child Like model doesnot exit then create
#             comment.likes
#         except models.Comment.likes.RelatedObjectDoesNotExist as identifier:
#             models.Like.objects.create(comment = comment)

#         if opinion.lower() == 'like':

#             if request.user in comment.likes.users.all():
#                 comment.likes.users.remove(request.user)
#             else:    
#                 comment.likes.users.add(request.user)
#                 comment.dis_likes.users.remove(request.user)

#         elif opinion.lower() == 'dis_like':

#             if request.user in comment.dis_likes.users.all():
#                 comment.dis_likes.users.remove(request.user)
#             else:    
#                 comment.dis_likes.users.add(request.user)
#                 comment.likes.users.remove(request.user)
#         else:
#             return HttpResponseRedirect(reverse('comment'))
#         return HttpResponseRedirect(reverse('comment'))

def about_us(request):
    return render(request, 'about_us.html')


def book_transaction(request):
    lent=Lends.objects.filter(lender=request.user.id)
    borrowed=Borrower.objects.filter(borrower=request.user.id)
    if request.method=='POST':
        #return request 
        if request.POST.get('book')!=None:
            Id=request.POST.get('book')   
            receiver=request.user
            # receiver=Lends.objects.filter(bid__id__icontains=Id)
            for each in Lends.objects.filter(bid__id__icontains=Id):
                receiver=each.lender
            book=Books.objects.get(id=Id)
            sender=request.user.username
            message=notification(sender=sender,receiver=receiver,book=book)
            try:
                message.save()
                return render(request, 'book_transaction.html',{"borrowed":borrowed, "lent":lent,"message":"Your return request has been initiated."})
            except:
                return render(request, 'book_transaction.html',{"borrowed":borrowed, "lent":lent,"message":"Return request has already been intiated"})

        elif request.POST.get('response')!=None:
            id=request.POST.get('id')
            if request.POST.get('response')=="yes":
                ntf=notification.objects.get(id=id)
                bk=ntf.book
                Borrower.objects.get(bid=ntf.book.id).delete()
                ntf.delete()
                bdts=Books.objects.get(id=bk.id)
                bdts.available=True
            return render(request, 'book_transaction.html',{"borrowed":borrowed, "lent":lent})
                

    else:
        alerts=notification.objects.filter(receiver=request.user)
        if alerts:
            for alert in alerts:
                id=alert.id
                book=alert.book.name
                sender=alert.sender
                message="Return process of the book '"+str(book)+"' by "+str(sender)+" has been initiated"
                return render(request, 'book_transaction.html',{"borrowed":borrowed, "lent":lent,"alert":message,"aid":id}) 

             
        return render(request, 'book_transaction.html',{"borrowed":borrowed, "lent":lent})