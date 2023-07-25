from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from .models import Register, Rooms, Booking, FeedBack
from django.db.models import Q

def home_page(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        if request.POST.get('fn') and request.POST.get('ln')and request.POST.get('em')and request.POST.get('pwd')and request.POST.get('re'):
            post = Register()
            post.First_Name = request.POST.get('fn')
            post.Last_Name = request.POST.get('ln')
            post.E_mail = request.POST.get('em')
            post.password = request.POST.get('pwd')
            post.Re_password = request.POST.get('re')
            post.save()
    return render(request,'register.html')

def introduction(request):

    email = request.POST['em']
    pwd = request.POST['pwd']

    flag = Register.objects.filter(Q(E_mail=email) & Q(password = pwd))

    if flag:
        return render(request,'introduction.html')

    else:
        messages.error(request,'Invalid Login credentials...!')
        return redirect('login')


def retrieve(request):

    rooms = Rooms.objects.all()
    print(rooms)
    params = {'rm':rooms}

    return render(request,'roomsfetch.html',params)


def booking(request):
    # room = Rooms.objects.get(id = Rooms.Room_ID)
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('ph_no') and request.POST.get('check-in-date'):
            post = Booking()
            post.Name= request.POST.get('name')
            post.Email = request.POST.get('email')
            post.Contact_No = request.POST.get('ph_no')
            post.Check_In = request.POST.get('check-in-date')
            post.save()

    return render(request,'booking_form.html')

def b_status(request):
    status = Booking.objects.all()
    book = {'stat':status}
    return render(request,'status.html',book)


def feed(request):
    if request.method == 'POST':
        if request.POST.get('em') and request.POST.get('comments'):
            post = FeedBack()
            post.e_mail = request.POST.get('em')
            post.comments = request.POST.get('comments')
            post.save()

            messages.success(request, 'success..!')
            return redirect('FDBHNDLE')

        else:
            return render(request, 'feedback.html')

    else:
        return render(request, 'feedback.html')



def feedbackhandle(request):
    ret = FeedBack.objects.all()
    params = {'comments': ret}

    return render(request, 'fhandle.html', params)





