from django.forms import ModelForm

from .models import Student

class StudentForm(ModelForm):
	fieldsets = [
		("Student Information", {'fields': [
			('first_name', 'last_name'),
			('email', 'adress'),
		]}),
		("Parent Information", {'fields': [
			'mother_name',
			'father_name',
		]}),
	]
	class Meta:
		model = Student
		fields = '__all__'
