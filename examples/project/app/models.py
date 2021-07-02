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
