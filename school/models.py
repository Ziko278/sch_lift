from django.apps import apps
from django.db import models
from django.db.models import Sum

from admin_dashboard.models import SessionModel
from django.contrib.auth.models import User
from admin_dashboard.models import SchoolAcademicInfoModel
from django.apps import apps


class SchoolFormModel(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='images/logo', null=True, blank=True)
    mobile_1 = models.CharField(max_length=20)
    mobile_2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name.upper()


class SchoolInfoModel(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='images/logo', null=True, blank=True)
    short_name = models.CharField(max_length=50)
    mobile_1 = models.CharField(max_length=20)
    mobile_2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True, blank=True)
    wallet = models.FloatField(default=0, blank=0)
    STATUS = (('active', 'ACTIVE'), ('inactive', 'INACTIVE'))
    status = models.CharField(max_length=30, choices=STATUS, default='active', blank=True)

    def __str__(self):
        return self.name.upper()

    def has_db(self):
        database_count = SchoolDBModel.objects.filter(school=self).count()
        if database_count > 0:
            return SchoolDBModel.objects.filter(school=self).first()
        return False

    def has_made_payment(self):
        academic_info = SchoolAcademicInfoModel.objects.first()
        if not academic_info:
            return False
        session = academic_info.session
        term = academic_info.term
        SubscriptionPaymentModel = apps.get_model('subscription', 'SubscriptionPaymentModel')
        payment = SubscriptionPaymentModel.objects.filter(session=session, term=term, school=self)
        if len(payment) > 0:
            return True
        return False

    def number_of_students(self):
        return 257

    def current_payment(self):
        UserProfileModel = apps.get_model('account', 'UserProfileModel')
        school_profile = UserProfileModel.objects.filter(school=self).first()
        if not school_profile:
            return 0
        current_plan = school_profile.current_plan
        return current_plan.price_per_term * self.number_of_students()

    def amount_paid(self):
        academic_info = SchoolAcademicInfoModel.objects.first()
        if not academic_info:
            return 0
        session = academic_info.session
        term = academic_info.term
        SubscriptionPaymentModel = apps.get_model('subscription', 'SubscriptionPaymentModel')
        payment = \
        SubscriptionPaymentModel.objects.filter(session=session, term=term, school=self).aggregate(Sum('amount'))[
            'amount__sum']
        if not payment:
            payment = 0
        return payment

    def current_balance(self):

        return self.current_payment() - self.amount_paid()

    def payment_list(self):
        SubscriptionPaymentModel = apps.get_model('subscription', 'SubscriptionPaymentModel')
        return SubscriptionPaymentModel.objects.filter(school=self).order_by('id').reverse()


class SchoolSettingModel(models.Model):
    school = models.ForeignKey(SchoolInfoModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{} SETTING".format(self.school.name.upper())


class SchoolTermRecordModel(models.Model):
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE)
    TERM = (
        ('1st term', '1st TERM'), ('2nd term', '2nd TERM'), ('3rd term', '3rd TERM')
    )
    term = models.CharField(max_length=10, choices=TERM)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    no_of_schools = models.FloatField()
    no_of_students = models.FloatField()
    no_of_staff = models.FloatField()
    no_of_parents = models.FloatField()


class SchoolDBModel(models.Model):
    school = models.OneToOneField(SchoolInfoModel, on_delete=models.CASCADE, related_name='school_db')
    host = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    database = models.CharField(max_length=100)
    port = models.CharField(max_length=100)






