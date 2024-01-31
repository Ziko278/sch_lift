from django.apps import apps
from django.db import models
from admin_dashboard.models import SessionModel
from django.contrib.auth.models import User, Group
from school.models import SchoolInfoModel
from subscription.models import PlanModel


class UserAccountModel(models.Model):
    """"""
    fullname = models.CharField(max_length=150)
    image = models.FileField(upload_to='images/account_images', blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    GENDER = (
        ('MALE', 'MALE'), ('FEMALE', 'FEMALE')
    )
    gender = models.CharField(max_length=10, choices=GENDER)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    account_id = models.CharField(max_length=100, blank=True, null=True)
    employment_date = models.DateField(blank=True, null=True)
    salary = models.BigIntegerField(blank=True, null=True, default=0)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    account_name = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=30, blank=True, default='active')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):

        user_profile = UserProfileModel.objects.filter(account=self).first()
        if user_profile:
            user = user_profile.user
            user.email = self.email
            user.save()
            # remove user from other group
            self.group.user_set.add(user)

        super(UserAccountModel, self).save(*args, **kwargs)


class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_schoollift = models.BooleanField()
    school = models.OneToOneField(SchoolInfoModel, on_delete=models.CASCADE, null=True, related_name='school_profile')
    account = models.OneToOneField(UserAccountModel, on_delete=models.CASCADE, null=True, related_name='account_profile')
    wallet = models.FloatField(default=0)
    current_plan = models.OneToOneField(PlanModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

