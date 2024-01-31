from django.db import models
from admin_dashboard.models import SessionModel
from django.contrib.auth.models import User
from school.models import SchoolInfoModel
from cryptography.fernet import Fernet


class ModuleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name.upper()


class FeatureModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name.upper()


class PlanModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    features = models.ManyToManyField(FeatureModel, blank=True)
    modules = models.ManyToManyField(ModuleModel, blank=True)
    years_of_backup = models.IntegerField(default=5)
    price_per_term = models.FloatField()

    def __str__(self):
        return self.name.upper()


class SubscriptionModel(models.Model):
    school = models.ForeignKey(SchoolInfoModel, on_delete=models.SET_NULL, null=True)
    plan = models.ForeignKey(PlanModel, on_delete=models.SET_NULL, null=True)


class SubscriptionPaymentModel(models.Model):
    school = models.ForeignKey(SchoolInfoModel, on_delete=models.SET_NULL, null=True)
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE)
    TERM = (
        ('1st term', '1st TERM'), ('2nd term', '2nd TERM'), ('3rd term', '3rd TERM')
    )
    term = models.CharField(max_length=10, choices=TERM)
    amount = models.FloatField()
    METHOD = (
        ('online', 'ONLINE'), ('transfer', 'TRANSFER'), ('cash', 'CASH'), ('bank', 'BANK'), ('wallet', 'WALLET')
    )
    payment_method = models.CharField(max_length=10, choices=METHOD)
    proof_of_payment = models.FileField(upload_to='subscription/payment', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)


class OnlinePaymentModel(models.Model):
    METHOD = (('paystack', 'PAYSTACK'), ('flutterwave', 'FLUTTERWAVE'))

    name = models.CharField(max_length=250, choices=METHOD)
    public_key = models.CharField(max_length=250)
    private_key = models.CharField(max_length=250)
    email = models.EmailField()
    vat = models.FloatField(default=0.0)
    key = models.CharField(max_length=250, blank=True, null=True)
    STATUS = (
        ('active', 'ACTIVE'), ('inactive', 'INACTIVE')
    )
    status = models.CharField(max_length=20, choices=STATUS, default='active', blank=True)

    def __str__(self):
        return self.name.upper()

    def save(self, *args, **kwargs):
        key = Fernet.generate_key().decode()
        fernet = Fernet(key)
        self.key = key
        self.public_key = fernet.encrypt(self.public_key.encode()).decode()
        self.private_key = fernet.encrypt(self.private_key.encode()).decode()
        super(OnlinePaymentModel, self).save(*args, **kwargs)

