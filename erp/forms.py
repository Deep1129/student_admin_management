from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)  #  Add a date picker for better user experience

    class Meta:
        model = Attendance
        fields = ['student', 'date', 'present']  #  Removed 'teacher' so it gets assigned automatically
