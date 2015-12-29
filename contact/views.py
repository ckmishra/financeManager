from django.core.mail import send_mail
from django.http.response import  HttpResponseRedirect
from django.shortcuts import render
from contact.forms import ContactForm


def contact(request):
    errors =[]
    if request.method == 'POST' :
        if not request.POST.get('subject',''):
            errors.append("Subject is mandatory field")
        if not request.POST.get('message','') :
            errors.append("Feedback should not be empty")
        if 'email' in request.POST and '@' not in request.POST.get('email') :
            errors.append("Enter valid Email id")
        if not errors :
            send_mail(request.POST.get('subject'),request.POST.get('message'),request.POST.get('email','noreply@test.com'),['ckmishra01@gmail.com'],)
            return HttpResponseRedirect('/thanks/')
    
    return render(request,'contact_form.html', {'errors': errors})

def thanks(request):
    return render(request, 'thanks.html')
        


def contact_adv(request):
    if request.method == 'POST' :
       form = ContactForm(request.POST)
       if form.is_valid()  :
           cd = form.cleaned_data
           send_mail(cd['subject'],cd['message'],cd.get('email','noreply@test.com'),['ckmishra01@gmail.com'],)
           return HttpResponseRedirect('/thanks/')
    else :
        form = ContactForm(
                           initial={'subject': 'I love your site!','email':'test@example.com','message':'Your feedback.'}
                           )
    return render(request,'contact_for_adv.html', {'form': form})