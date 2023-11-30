from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, Http404
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
def view_pdf(request):
    # filename = None
    pdf_url=None
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        # fs = FileSystemStorage()
        fs = FileSystemStorage(location=settings.STATIC_ROOT)
        filename = fs.save(pdf_file.name, pdf_file)
        pdf_url = fs.url(filename)
     
    return render(request, 'view_pdf.html', {'pdf_url': pdf_url})
@csrf_exempt  # Only if you're using this for testing, consider CSRF protection for production
def your_view(request):
    if request.method=='POST':
            text = request.POST.get('textbox', '')  # Get the value of the textarea field
            num_questions = request.POST.get('numQuestions', '')  # Get the value of the select field
            print(text)
            print(num_questions)
        # Process the data as needed
        # Your logic here...

            # Return a JSON response, if needed
            quiz_data = [
            {
                'question': "What is the capital of France?",
                'options': ["London", "Paris", "Berlin", "Madrid"],
                'correct_answer': 1  # Index of the correct answer in the options array
            },
            {
                'question': "Which planet is known as the Red Planet?",
                'options': ["Venus", "Mars", "Jupiter", "Saturn"],
                'correct_answer': 1  # Index of the correct answer in the options array
            },
            # Add more questions here in a similar format
        ]
        
            context = {
            'quiz_data': quiz_data,
        }
            return render(request, 'quiz.html', context)
    else:
        return JsonResponse({'error': 'Invalid request method'})    

def about_us(request):
    print('here')
    return render(request, 'aboutus.html')

def contact_us(request):
    return render(request, 'contact.html')        
def homepage(request):
    return render(request, 'homepage.html')      