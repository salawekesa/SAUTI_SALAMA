from django import forms
from .models import SGBVReport
from multiupload.fields import MultiFileField

class SGBVReportForm(forms.ModelForm):
    class Meta:
        model = SGBVReport
        fields = ['user','incident_type', 'description', 'location', 'evidence', 'comments', 'is_anonymous','media_files']


    media_files = MultiFileField(min_num=1, max_num=5, max_file_size=1024*1024*5)  # Adjust max_num and max_file_size as needed
