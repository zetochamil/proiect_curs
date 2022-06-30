from django.contrib import admin

# Register your models here.
from .models import Student, Curs, Question, Choice, Membership

class StudentAdmin(admin.ModelAdmin):
    list_display = ('nume', 'prenume', 'an', 'email')

admin.site.register(Student, StudentAdmin)

admin.site.register(Curs)

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Membership)

