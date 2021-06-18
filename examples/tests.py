from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.db import models
from django import forms
from django.forms import inlineformset_factory
from django.template import Context, Template

from .models import Student, Note
from .forms import StudentForm

from forms_fieldset.templatetags.forms_fieldset import fieldset, inline_fieldset
# Create your tests here.
class FieldsetInlineFieldsetTestTags(TestCase):
	def setUp(self):
		self.form = StudentForm()

	def test_render_fieldset(self):
		context = Context({'form': self.form})
		template_render = Template(
			"""
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
					</form>
				</body>
				</html>

			"""
		)
		rendered = template_render.render(context)
		self.assertInHTML('<h2 style="background-color: #42945c">Student Information</h2>', rendered)

		self.assertInHTML('<input type="text" name="first_name" maxlength="200" required id="id_first_name">', rendered)
		self.assertInHTML('<label class="required" for="id_first_name">First Name :</label>', rendered)

		self.assertInHTML('<input type="text" name="last_name" maxlength="200" required id="id_last_name">', rendered)
		self.assertInHTML('<label class="required inline" for="id_adress">Adress :</label>', rendered)

		self.assertInHTML('<input type="email" name="email" maxlength="254" required id="id_email">', rendered)
		self.assertInHTML('<label class="required" for="id_email">Email :</label>', rendered)

		self.assertInHTML('<input type="text" name="adress" maxlength="200" required id="id_adress">', rendered)
		self.assertInHTML('<label class="required inline" for="id_adress">Adress :</label>', rendered)


	def test_render_inline_fieldset(self):
		InlineForm = inlineformset_factory(Student, Note, 
			fields=('subject', 'value',), exclude=('pk',), can_delete=False,
		)
		context = Context({'form': self.form, 'form_inline': InlineForm()})
		template_render = Template(
			"""
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
						{{ form_inline|inline_fieldset:'#42945c, Note des eleves' }}
					</form>
				</body>
				</html>

			"""
		)
		rendered = template_render.render(context)
		self.assertInHTML('<h2 style="background-color: #42945c">Student Information</h2>', rendered)

		self.assertInHTML('<input type="text" name="first_name" maxlength="200" required id="id_first_name">', rendered)
		self.assertInHTML('<label class="required" for="id_first_name">First Name :</label>', rendered)

		self.assertInHTML('<input type="text" name="last_name" maxlength="200" required id="id_last_name">', rendered)
		self.assertInHTML('<label class="required inline" for="id_adress">Adress :</label>', rendered)

		self.assertInHTML('<input type="email" name="email" maxlength="254" required id="id_email">', rendered)
		self.assertInHTML('<label class="required" for="id_email">Email :</label>', rendered)

		self.assertInHTML('<input type="text" name="adress" maxlength="200" required id="id_adress">', rendered)
		self.assertInHTML('<label class="required inline" for="id_adress">Adress :</label>', rendered)
		## inline
		self.assertInHTML('<h2 style="background-color: #42945c">Note des eleves</h2>', rendered)
		self.assertInHTML('<input type="hidden" name="notes-TOTAL_FORMS" value="3" id="id_notes-TOTAL_FORMS">', rendered)
		self.assertInHTML('<a href="#" id="add-info">Ajout supplémentaire</a>', rendered)

