from django.shortcuts import render
from django.http.response import HttpResponse
from books.models import Book

# Create your views here.

def search_form(request):
    return render(request, 'search_form.html')

def search_bad(request):
    if 'q' in request.GET :
        message = 'You have searched for %r' % request.GET['q']
    else :
        message = 'No search has been performed'
     
    return  HttpResponse(message)
        

def search(request):
    errors = []
    if 'q' in request.GET :
        q = request.GET['q']
        if not q :
            errors.append("Enter a valid search term.")
            
        elif len(q) > 20 :
            errors.append("Enter a valid search having less than 20 character.")
            
        else :
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books' : books,'query': q})
    
    return render(request, 'search_form.html', {'errors': errors}) 



        
    