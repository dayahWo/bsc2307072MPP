# Create your views here.
from django.shortcuts import render
from hobbies.models import Student, Mentor, Programme
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

def index(request):
    context={
        'nickname':'fatimah',
    }       
    return render(request,"index.html", context)

def hobby(request):
    number1=int(request.GET.get('number1', 0))
    number2=int(request.GET.get('number2', 0))

    dict={
        'number1':number1,
        'number2':number2
    }
    return render(request,'u_hobby.html', dict)

def newmentor(request):
    displaydata=Mentor.objects.all().values()
    if request.method=='POST':
        menid1=request.POST['mentorid']
        menname1=request.POST['mentorname']
        menroomno1=request.POST['mentorroomno']
        data=Mentor(menid=menid1, menname=menname1,menroomno=menroomno1)
        data.save()

        context={
        'displaydata':displaydata,
        'message': 'NEW MENTOR HAS BEEN SAVED'
        }
        
        return render(request,"newmentor.html",context)
    else:
        dict={
            'message': 'tiada method post activate',
            'displaydata':displaydata,
        }
    return render(request,"newmentor.html",dict)



def update(request,menid):
    updateid=Mentor.objects.get(menid=menid)
    dict={
        'updateid':updateid,
        'message':'PAGE RENDERED, DATA IS NOT UPDATED YET'
    }
    return render(request,"update.html",dict)

def updatedata(request,menid):
    data=Mentor.objects.get(menid=menid)
    menname1=request.POST['mentorname']
    menroomno=request.POST['mentorroomno']
    data.menname=menname1
    data.menroomno=menroomno
    data.save()
    
    return HttpResponseRedirect(reverse("newmentor"))




def viewdelete(request,menid):
    datanakdelete=Mentor.objects.get(menid=menid)
    dict={
        'datatobedeleted':datanakdelete
    }
    return render(request,"delete.html",dict)

def delete(request,menid):
    deletementor=Mentor.objects.get(menid=menid)
    deletementor.delete()
    return HttpResponseRedirect(reverse("newmentor"))


def searchpage(request):
    query = request.GET.get('search')
    if query:
        # icontains can be use for partial and case-insensitive matches
        findmentor = Mentor.objects.filter(
            Q(menid__icontains=query) | Q(menname__icontains=query)
        )
    else:
        findmentor = Mentor.objects.none()  # Return an empty queryset if no search query
    
    dict = {
        'findmentor': findmentor
    }
    return render(request, 'searchpage.html', dict)




def newstudent(request):
    stumentor1=Student.objects.all().values()
    mymentor=Mentor.objects.all().values()

    if request.method=='POST':
        stuid=request.POST['studentid']
        stuname=request.POST['studentname']
        stuemail=request.POST['studentemail']
        stuage=request.POST['studentage']

        menid1=request.POST['selectmenid']
        mentornew = Mentor.objects.get(menid=menid1)
        
        data=Student(stuid=stuid, stuname=stuname,stuemail=stuemail, 
                     stuage=stuage, stumentor=mentornew)
        data.save()

        context={
        'stumentor':stumentor1,
        'mymentor':mymentor,
        'message': 'NEW STUDENT HAS BEEN SAVE'
        }
        
        return render(request,"newstudent.html",context)
    else:
        dict={
            'stumentor':stumentor1,
            'mymentor':mymentor,
            'message': 'PAGE IS REFRESHED',
        }
    return render(request,"newstudent.html",dict)
