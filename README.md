# <a id="djangoformsfieldset_0"></a>django-forms-fieldset

Django form fieldset inspire django admin fieldset

## <a id="Installation_4"></a>Installation

    pip install django-forms-fieldset

## <a id="Usage_9"></a>Usage

`settings`

Add `forms_fieldset` to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'forms_fieldset',
    ]

`load template`

    {% load forms_fieldset static %}

    {% fieldset form fieldsets '#42945c' %}

**_Note_** : The first argument of `fieldset` tag is the `form` the second the list  
`fieldsets` where you have defined the positioning of your different elements and  
the last the color of the title of the fieldset (by default this value is at `#79AEC8`)

## <a id="Complete_Guide_32"></a>Complete Guide

`models`

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

`forms`

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

`views`

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
        context = {
            'form': form,
            'fieldsets': form.fieldsets,
            'inline_formset': InlineForm()
        }
        return render(request, 'home.html', context)

`template`

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
            {% fieldset form fieldsets '#42945c' %}
            {% fieldset inline_formset '#42945c' "Note des eleves" %}
        </form>
    </body>
    </html>

`enjoy`  
![Screenshot](https://github.com/hadpro24/django-forms-fieldset/blob/main/result_test.png?raw=true)

## <a id="Features_131"></a>Features

1.  Fieldset django form
2.  Fieldset (tabular style) inline form

## <a id="Credit_135"></a>Credit

# <a id="Harouna_Diallo_136"></a>Harouna Diallo