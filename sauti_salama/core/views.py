from django.shortcuts import render, redirect
from .models import SGBVReport
from .forms import SGBVReportForm  # You'll need to create an SGBVReportForm

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
