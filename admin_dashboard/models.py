from django.db import models


class SessionModel(models.Model):
    start_year = models.FloatField()
    end_year = models.FloatField()
    DELIMITER = (('-', '-'), ('/', '/'))
    delimiter = models.CharField(max_length=1, choices=DELIMITER)

    def __str__(self):
        return str(round(self.start_year)) + self.delimiter + str(round(self.end_year))


class SchoolAcademicInfoModel(models.Model):
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE)
    TERM = (
        ('1st term', '1st TERM'), ('2nd term', '2nd TERM'), ('3rd term', '3rd TERM')
    )
    term = models.CharField(max_length=20, choices=TERM)


class TermRecordModel(models.Model):
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


class SiteInfoModel(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='images/logo')
    mobile_1 = models.CharField(max_length=20)
    mobile_2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name.upper()


class SiteSettingModel(models.Model):
    count_inactive_student = models.BooleanField()

    def __str__(self):
        return 'SITE SETTING'

