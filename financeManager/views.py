from django.shortcuts import  render,render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.http.response import HttpResponseRedirect,HttpResponse
from financeManager.forms import financeManagerForm, RegisterForm, ProfileForm
from financeManager.models import financeDetails
from SampleProject.settings import STATIC_URL
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.core.mail import send_mail
from django.core import mail

# Create your views here.
def auth(request):
    state = ''
    username = password =''
    if  request.method =='POST' :
        username = request.POST['username']
        password =request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None :
            if user.is_active: 
                login(request,user)
                state = "User has been Successfully logged in."
                return HttpResponseRedirect('/home/')
            else:
                state="User is inactive. Please contact Admin."
        else :
            state ="Your username and password didn't match. Please try again."
    return render_to_response('login.html',{'state':state,'username':username,}, context_instance=RequestContext(request))

def home(request):
    return render(request,'home.html')


@login_required(login_url='/login/')
def addPolicy(request):
    form = financeManagerForm()
    if request.user.is_authenticated():
        userId= request.user.id
        user = User.objects.get(id=userId)
    else:
        userId =0
        #return render(request,'auth.html',{'state':" Please re-login. "})
    if request.method == 'GET':
        policyDetails =financeDetails.objects.filter(userName=userId)
        if request.GET.get('add'):
            return render(request, 'home.html', {'forms' : form, 'enableAdd': False, 'policyDetails':policyDetails,'username':user.first_name +" "+ user.last_name})
        else :
            return render(request, 'home.html', {'forms' : form, 'enableAdd': True,'policyDetails':policyDetails,'username':user.first_name+ " "+user.last_name })
    
    else :
        form = financeManagerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.get(id=userId)
            fd = financeDetails(name=cd['name'],policyNumber=cd['policyNumber'],financeType=cd['financetype'],issueDate=cd['issueDate'],maturityDate=cd['maturityDate'],amount=cd['amount'],remarks=cd['remarks'],userName=user)
            fd.save()
            return HttpResponseRedirect('/home/')
    return HttpResponseRedirect('/home/')

import json  
def updatePolicy(request):
    policy= financeDetails.objects.get(policyNumber=request.POST['policyNumber'])
    policy.name = request.POST['name']
    policy.financeType = request.POST['financeType']
    policy.amount = request.POST['amount']
    policy.issueDate = request.POST['issueDate']
    policy.maturityDate = request.POST['maturityDate']
    policy.remarks = request.POST['remarks']
    policy.save()
    payload = {'success': "Selected policy has been updated"}
    return HttpResponse(json.dumps(payload), content_type='application/json')



def deletePolicy(request):
    policy= financeDetails.objects.get(policyNumber=request.POST['policyNumber'])
    policy.delete()
    payload = {'success': "Selected policy has been deleted."}
    return HttpResponse(json.dumps(payload), content_type='application/json')

def logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


class Profile(View):
    
    def get(self, request,offset):
        params = dict()

        offset= (int)(offset)
        
        if(offset==1):
            params['enablePasswordChange'] = False
        
        if(offset==2):
            params['enablePasswordChange'] = True

        userId= request.user.id
        user = User.objects.get(id=userId)
        registration_form = RegisterForm(initial={'firstname':user.first_name,'lastname':user.last_name,'username':user.username,'email':user.email,'password':user.password},)
        params['register'] = registration_form
        return render(request, 'profile.html', params)
        pass

    def post(self, request,offset):
        params = dict()
        form = ProfileForm(request.POST)
        params['register'] = form
        if form.is_valid():
            firstname= form.cleaned_data['firstname']
            lastname= form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                error= "Confirm Password did not match."
                params['error']= error
                return render(request, 'profile.html', params)
            userId= request.user.id
            user = User.objects.get(id=userId)
            user.first_name=firstname
            user.last_name=lastname
            user.email = email
            user.password= password
            commit = True
            #user = super(user, self).save(commit=False)
            #user.set_password(password)
            if commit:
                user.save()

            return HttpResponseRedirect('/home')

class Register(View):
    error = ""
    def get(self, request):
        params = dict()
        registration_form = RegisterForm()
        code = request.GET.get('code')
        params['code'] = code
        params['register'] = registration_form
        return render(request, 'registration/register.html', params)
        pass

    def post(self, request):
        params = dict()
        form = RegisterForm(request.POST)
        params['register'] = form
        if form.is_valid():
            firstname= form.cleaned_data['firstname']
            lastname= form.cleaned_data['lastname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                error= "Confirm Password did not match."
                params['error']= error
                return render(request, 'registration/register.html', params)
            try:
                user = User.objects.filter(username=username).filter(email=email)
                error = "User already exist with given user name or email"
                params['error']= error
                return render(request, 'registration/register.html', params)
            except:
                user = User()
                user.username = username
                user.first_name=firstname
                user.last_name=lastname
                user.email = email
                commit = True
                #user = super(user, self).save(commit=False)
                user.set_password(password)
                if commit:
                    user.save()

                return HttpResponseRedirect('/login')

     
def table_dynamic(request):
    return render(request,'table_dynamic.html',{'STATIC_URL':STATIC_URL})

def sendEmail(request):
    connection = mail.get_connection()
    connection.open()
    send_mail('Subject here', 'Here is the message.', 'mishrac9@gmail.com',
    ['ckmishra01@gmail.com'], fail_silently=True)
    return HttpResponseRedirect('/home') 