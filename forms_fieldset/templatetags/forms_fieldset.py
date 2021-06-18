import logging

from django import template
from django.contrib.admin.helpers import AdminForm
from django.template.loader import render_to_string

from django.conf import settings

logger = logging.getLogger(__name__)

class FieldsetsNotSupported(Exception):
	""" form field sets type error, it must be a list """
	pass

class ArgumentNotSupported(Exception):
	""" form field sets type error, it must be a list """
	pass

register = template.Library()
@register.filter
def fieldset(form, color='#79AEC8'):
	if not hasattr(form, 'fieldsets') or not isinstance(form.fieldsets, list):
		raise FieldsetsNotSupported("your form does not contain 'fieldsets' or is not the correct type")
	form_fieldset = AdminForm(form, list(form.fieldsets),{})
	context = {
		'form_fieldset': form_fieldset,
		'color': color,
	}
	return render_to_string('forms_fieldset/fieldset.html', context)

@register.filter
def inline_fieldset(inline_formset, args):
	if len(str(args).split(',')) != 2:
		raise ArgumentNotSupported("The 'inline fieldset' argument \
			does not have the correct argument. \
			it must be a str (ex: '#000000, title inline form')")
	color, label = args.split(',')
	color = color or '#79AEC8'
	label= label or 'Inline Form'
	LANGEAGE_DATA = {
		'en-en': 'Add another',
		'en': 'Add another',
		'EN-EN': 'Add another',
		'EN': 'Add another',
		'fr-fr': 'Ajout supplémentaire',
		'fr': 'Ajout supplémentaire',
		'FR-FR': 'Ajout supplémentaire',
		'Fr': 'Ajout supplémentaire',
		'de': 'Ajout supplémentaire',
	}
	context = {
		'inline_formset': inline_formset,
		'color': color,
		'label': label,
		'title_add': LANGEAGE_DATA.get(settings.LANGUAGE_CODE, 'Add another') 
	}
	return render_to_string('forms_fieldset/tabular.html', context)

# old version
USED = False
@register.simple_tag
def fieldset(form, fieldsets, color='#79AEC8'):
	logger.warning("""you are using the features of an old version, replace the tags with filters.
	 more information on this link: https://github.com/hadpro24/django-forms-fieldset """)
	USED = True
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
	if not USED:
		print()
		logger.error("""WARNING: you are using the features of an old version, replace the tags with filters.\nMore information on this link: https://github.com/hadpro24/django-forms-fieldset""")
		print()
	LANGEAGE_DATA = {
		'en-en': 'Add another',
		'en': 'Add another',
		'EN-EN': 'Add another',
		'EN': 'Add another',
		'fr-fr': 'Ajout supplémentaire',
		'fr': 'Ajout supplémentaire',
		'FR-FR': 'Ajout supplémentaire',
		'Fr': 'Ajout supplémentaire',
		'de': 'Ajout supplémentaire',
	}
	context = {
		'inline_formset': inline_formset,
		'color': color,
		'label': label,
		'title_add': LANGEAGE_DATA.get(settings.LANGUAGE_CODE, 'Add another') 
	}
	return render_to_string('forms_fieldset/tabular.html', context)