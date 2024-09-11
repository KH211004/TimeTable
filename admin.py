from django.contrib import admin

# Register your models here.
from .models import Subject,Faculty,LoadAllocate,LabAllocation,Faculty_Availability,Faculty_Subject_Totalhours,TheoryAllocation,Sem_4_C,Sem_4_D,Sem_6_D,Monday,Tuesday,Wednesday,Thursday,Friday,Sem_4_C_lab,Sem_4_D_lab,Sem_6_C_lab,Sem_6_D_lab

admin.site.register(Subject)
admin.site.register(Faculty)
admin.site.register(LoadAllocate)
admin.site.register(LabAllocation)
admin.site.register(Faculty_Availability)
admin.site.register(Faculty_Subject_Totalhours)
admin.site.register(TheoryAllocation)
admin.site.register(Sem_4_C)
admin.site.register(Sem_4_D)
admin.site.register(Sem_6_D)
admin.site.register(Monday)
admin.site.register(Tuesday)
admin.site.register(Wednesday)
admin.site.register(Thursday)
admin.site.register(Friday)
admin.site.register(Sem_4_C_lab)
admin.site.register(Sem_4_D_lab)
admin.site.register(Sem_6_C_lab)
admin.site.register(Sem_6_D_lab)