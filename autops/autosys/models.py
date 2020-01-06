from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Farm(models.Model):
    farmname = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.farmname)
        super(Farm, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.farmname


class Category(models.Model):
    DMZ = 'DMZ'
    Primary = 'Primary'
    server_choices = (
        (DMZ, 'DMZ'),
        (Primary, 'Primary'),
    )
    farm = models.ForeignKey(Farm)
    name = models.CharField(max_length=128, unique=True)
    type = models.CharField(max_length=8, choices=server_choices, default=Primary)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    serverip = models.CharField(max_length=128, blank=True)
    loadbid = models.CharField(max_length=128, blank=True)
    loadbrid = models.CharField(max_length=128, blank=True)
    loadbsid = models.CharField(max_length=128, blank=True)
    loadreqlink = models.CharField(max_length=128, blank=True, unique=True)
    loadenable = models.CharField(max_length=2000, blank=True)
    loaddisable = models.CharField(max_length=2000, blank=True)
    linkk = models.CharField(max_length=2000, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class LinuxServer(models.Model):
    DMZ = 'DMZ'
    Primary = 'Primary'
    server_choices = (
        (DMZ, 'DMZ'),
        (Primary, 'Primary'),
    )
    farm = models.ForeignKey(Farm)
    servname = models.CharField(max_length=128, unique=True)
    type = models.CharField(max_length=8, choices=server_choices, default=Primary)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    serverip = models.CharField(max_length=128, blank=True)
    loadbid = models.CharField(max_length=128, blank=True)
    loadbrid = models.CharField(max_length=128, blank=True)
    loadbsid = models.CharField(max_length=128, blank=True)
    loadreqlink = models.CharField(max_length=128, blank=True, unique=True)
    loadenable = models.CharField(max_length=2000, blank=True)
    loaddisable = models.CharField(max_length=2000, blank=True)
    slink = models.CharField(max_length=2000, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.servname)
        super(LinuxServer, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.servname


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128, blank=True)
    # idd = models.CharField(max_length=128)
    service = models.CharField(max_length=128, unique=True)
    result = models.CharField(max_length=128, unique=True)
    delete = models.CharField(max_length=128, blank=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.title


class LinuxOperation(models.Model):
    linuxserver = models.ForeignKey(LinuxServer)
    ltitle = models.CharField(max_length=128)
    # serveripp = models.CharField(max_length=128)
    lservice = models.CharField(max_length=128, unique=True)
    lresult = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=128)
    command = models.CharField(max_length=2000)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.ltitle


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    apausername = models.CharField(max_length=128, blank=True)
    apapassword = models.CharField(max_length=128, blank=True)
    bewenousername = models.CharField(max_length=128, blank=True)
    bewenopassword = models.CharField(max_length=128, blank=True)
    linuxusername = models.CharField(max_length=128, blank=True)
    linuxpassword = models.CharField(max_length=128, blank=True)
    lbusername = models.CharField(max_length=128, blank=True)
    lbpassword = models.CharField(max_length=128, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

