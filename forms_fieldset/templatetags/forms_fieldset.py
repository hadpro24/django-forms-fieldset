from django import template
from django.contrib.admin.helpers import AdminForm
from django.template.loader import render_to_string

class FieldsetsNotSupported(Exception):
	""" form field sets type error, it must be a list """
	pass

register = template.Library()
@register.simple_tag
def fieldset(form, fieldsets, color='#79AEC8'):
	if not isinstance(fieldsets, list):
		raise FieldsetsNotSupported("form field sets type error, it must be a list")
	form_fieldset = AdminForm(form, list(fieldsets),{})
	context = {
		'form_fieldset': form_fieldset,
		'color': color,
	}
	return render_to_string('forms_fieldset/fieldset.html', context)

@register.simple_tag
def inline_fieldset(inline_formset, color='#79AEC8', label='Inline Form'):
	context = {
		'inline_formset': inline_formset,
		'color': color,
		'label': label,
	}
	return render_to_string('forms_fieldset/tabular.html', context)
