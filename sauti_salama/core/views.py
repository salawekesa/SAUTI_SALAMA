from django.shortcuts import render, redirect
from .models import SGBVReport
from .forms import SGBVReportForm 
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


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
            form.save()
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