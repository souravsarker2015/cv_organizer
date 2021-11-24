from django.db import models

STATE_CHOICE = (
    ('Dhaka', 'Dhaka'),
    ('Chittagong', 'Chittagong'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Mymensingh', 'Mymensingh'),
    ('Barisal', 'Barisal'),
    ('Rangpur', 'Rangpur'),
    ('Comilla', 'Comilla'),
    ('Narayanganj', 'Narayanganj'),
    ('Gazipur', 'Gazipur'),
)


class CV(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)
    # present_address=models.CharField(max_length=500)
    # permanent_address=models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    profile_file = models.FileField(upload_to='profile_files', blank=True)
