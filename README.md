django-forms-fieldset
==============
![https://github.com/hadpro24/django-forms-fieldset/actions](https://github.com/hadpro24/django-forms-fieldset/actions/workflows/test.yml/badge.svg)
![](https://img.shields.io/pypi/v/django-forms-fieldset.svg)
![https://pypi.org/project/django-forms-fieldset/](https://img.shields.io/pypi/pyversions/django-forms-fieldset)

Django form fieldset inspire django admin fieldset

Installation
-----
```sh
pip install django-forms-fieldset
```

Usage
-----
`settings`

Add `forms_fieldset` to your INSTALLED_APPS setting like this:
```python
INSTALLED_APPS = [
    ...
    'forms_fieldset',
]
```

`load template`

```html
{% load forms_fieldset static %}
<link rel="stylesheet" type="text/css" href="{% static 'forms_fieldset/css/main.css' %}">

<form>
	{{ form|fieldset:'#42945c' }}
</form>
```
***Note*** : The fieldset filter receives the color of the titles of the form groups, by default this color is used: # 79AEC8)

Complete Guide
----------

``models``
```python
from django.db import models

# Create your models here.
class Student(models.Model):
	first_name = models.CharField(max_length=200, verbose_name="First Name")
	last_name = models.CharField(max_length=200, verbose_name="Last Name")
	email = models.EmailField(unique=True, verbose_name="Email")
	adress = models.CharField(max_length=200, verbose_name="Adress")
	mother_name = models.CharField(max_length=200, verbose_name="Mother Name")
	father_name = models.CharField(max_length=200, verbose_name="Father Name")


class Note(models.Model):
	SUBJECTS = (
		('Math', 'Math'),
		('French', 'French'),
		('Physical', 'Physical'),
	)
	student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name="notes")
	subject = models.CharField(max_length=200, choices=SUBJECTS, verbose_name="Subject")
	value = models.IntegerField(verbose_name="Notation")

	class Meta:
		verbose_name = "Les notes"
		verbose_name_plural = "Les notes"
```

``forms``
```python
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

```

``views``
```python
from django.shortcuts import render
from django.forms import inlineformset_factory

from .forms import StudentForm
from .models import Student, Note
# Create your views here.
def home(request):
	form = StudentForm()
	InlineForm = inlineformset_factory(Student, Note, 
		fields=('subject', 'value',), exclude=('pk',), can_delete=False,
	)
	if request.method == 'POST':
		form = Form(request.POST, request.FILES)
		formset = InlineForm(request.POST, request.FILES)
		#save...
	context = {
		'form': form,
		'inline_form': InlineForm()
	}
	return render(request, 'home.html', context)
```

``template``
```jinja2
{% load forms_fieldset static %}
<!DOCTYPE html>
<html>
<head>
	<title>Home page</title>
	<link rel="stylesheet" type="text/css" href="{% static 'forms_fieldset/css/main.css' %}">
</head>
<body style="width: 75%; margin: 50px auto">
	<h1>Student form information</h1>

	<form>
		{{ form|fieldset:'#42945c' }}
		{{ form_inline|inline_fieldset:"#42945c,Note des eleves" }}
	</form>
</body>
</html>
```

`` enjoy ``
![Screenshot](https://github.com/hadpro24/django-forms-fieldset/blob/main/result_test.png?raw=true)

## Features
1. Fieldset django form
2. Fieldset (tabular style) inline form

## Release
	- version 1.0.2 
		fix #6
	- version 1.0.1
		fix #3

## Credit
Harouna Diallo
=======
