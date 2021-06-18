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
		'form_inline': InlineForm()
	}
	return render(request, 'home.html', context)
