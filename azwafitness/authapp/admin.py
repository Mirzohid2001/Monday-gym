from django.contrib import admin

from authapp.models import Contact,MembershipPlan,Enrollment,Trainer,Gallery,Attendance,Athends,Leg



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('name','email', 'phonenumber','description')
    list_display = ['name','email','phonenumber']

@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    fields = ('plan','price')
    list_display = ['plan','price']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    fields = ('fullname','email','gender','phoneNumber','DOB','SelectMembershipplan','SelectTrainer','Reference','paymentStatus','Price','DueDate','timeStamp')
    


# admin.site.register(Contact)
# admin.site.register(MembershipPlan)
# admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(Gallery)
admin.site.register(Attendance)
admin.site.register(Athends)
admin.site.register(Leg)