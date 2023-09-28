from django.shortcuts import render, redirect
from .models import SGBVReport
from .forms import SGBVReportForm 
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail


def sgbv_report_list(request):
    # Retrieve a list of SGBVReport instances
    reports = SGBVReport.objects.all()
    context = {
        "reports": reports
    }
    
    return render(request, "report_list.html",context)

def create_sgbv_report(request):
    form = SGBVReportForm()
    if request.method == 'POST':
        # Process the form submission if it's a POST request
        form = SGBVReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save()

            subject = 'welcome to Sauti salama'
            mubject = 'Welcome to Sauti Salama - SGBV Report Received'
            message = f'Hello dear,\n\n'
            message += 'We want to express our sincere gratitude for your courage in submitting your SGBV report to Sauti Salama. Your well-being is of utmost importance to us, and we are committed to providing you with the support and assistance you need during this difficult time.\n\n'
            message += f'Your report has been assigned a unique ID: {report.id}. This ID will help us keep track of your case and ensure that it receives the attention it deserves.\n\n'
            message += 'Please know that your report will be handled with the utmost confidentiality and sensitivity. We have a dedicated team of professionals who are trained to address cases like yours with care and empathy.\n\n'
            message += 'What happens next:\n'
            message += '- A member of our support team will reach out to you shortly to discuss your report in more detail.\n'
            message += '- You will have the opportunity to share any additional information or concerns you may have.\n'
            message += '- We will work together to develop a personalized plan to support you through this process.\n\n'
            message += 'At Sauti Salama, we are here to listen, assist, and stand with you every step of the way. Please do not hesitate to contact us at any time if you have questions, need assistance, or require immediate help.\n\n'
            message += 'Your safety and well-being are our top priorities, and we are dedicated to helping you on your journey toward healing and justice.\n\n'
            message += 'Thank you for trusting Sauti Salama with your report. Together, we can work towards a safer and more supportive community.\n\n'
            message += 'Warm regards,\n'
            message += 'The Sauti Salama Team'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [report.email, ]
            send_mail( subject, message, email_from, recipient_list )
                        
            for media_file in request.FILES.getlist('media_files'):
                pass
            return redirect('report_list')  # Redirect to the list view after successful submission
    context = {
        "form":form
    }
    return render(request, 'create_report.html', context)

def single_report(request, pk):
    reports = SGBVReport.objects.get(id=pk)
    context = {
        "reports":reports
    }
    return render(request, "single_report.html", context)

from django.http import JsonResponse

def update_progress(request, report_id):
    try:
        # Check if the user is a legal counsel or mental health practitioner
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'success': False, 'error': 'User not authenticated'})

        # Retrieve the SGBVReport instance based on the report_id
        report = SGBVReport.objects.get(id=report_id)

        # Update the progress steps as needed
        progress, created = Progress.objects.get_or_create(report=report)
        progress.step_1 = True  # Mark step 1 as completed
        progress.save()

        # Return a JSON response indicating the success of the progress update
        return JsonResponse({'success': True, 'message': 'Progress updated successfully'})
    except SGBVReport.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Report not found'})


def user_profile(request):
    # Add logic to retrieve user information or any other data you want to display
    context = {
        # Include relevant context data here
    }
    return render(request, 'user_profile.html', context)