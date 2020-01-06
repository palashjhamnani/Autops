from django import forms
from django.contrib.auth.models import User
from autops.models import Category, Page, Farm, LinuxServer, LinuxOperation
from autops.models import UserProfile
from django.forms import ModelForm

class CategoryForm(forms.ModelForm):
    DMZ = 'DMZ'
    Primary = 'Primary'
    server_choices = (
    (DMZ, 'DMZ'),
    (Primary, 'Primary'),
    )
    name = forms.CharField(max_length=128, help_text="Please enter the server name.")
    serverip = forms.CharField(max_length=128, help_text="Please enter server ipv4 address.")
    type = forms.ChoiceField(choices = server_choices, required=True, help_text="Select the server type")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    loadreqlink = forms.CharField(max_length=128, help_text="Enter the load balancer unique ID." )
    loadenable = forms.CharField(widget=forms.widgets.Textarea(), help_text="Enter the load balancer enable data.")
    loaddisable = forms.CharField(widget=forms.widgets.Textarea(), help_text="Enter the load balancer disable data.")
    linkk = forms.CharField( widget=forms.widgets.Textarea(), help_text="Enter the load balancer link." )

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name', 'type', 'serverip', 'loadreqlink', 'linkk', 'loadenable', 'loaddisable')



class LinuxServerForm(forms.ModelForm):
    DMZ = 'DMZ'
    Primary = 'Primary'
    server_choices = (
    (DMZ, 'DMZ'),
    (Primary, 'Primary'),
    )
    servname = forms.CharField(max_length=128, help_text="Please enter the server name.")
    serverip = forms.CharField(max_length=128, help_text="Please enter server ipv4 address.")
    type = forms.ChoiceField(choices = server_choices, required=True, help_text="Select the server type")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    loadreqlink = forms.CharField(max_length=128, help_text="Enter the load balancer unique ID." )
    loadenable = forms.CharField(widget=forms.widgets.Textarea(), help_text="Enter the load balancer enable data.")
    loaddisable = forms.CharField(widget=forms.widgets.Textarea(), help_text="Enter the load balancer disable data.")
    slink = forms.CharField( widget=forms.widgets.Textarea(), help_text="Enter the load balancer link." )

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = LinuxServer
        fields = ('servname', 'type', 'serverip', 'loadreqlink', 'slink', 'loadenable', 'loaddisable')


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    #service = forms.CharField(max_length=128, help_text="Please enter the service id.")
    #result = forms.CharField(max_length=128, help_text="Please enter the result id.")


    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        exclude = ('category', 'service', 'result', 'delete')


class LinuxOperationForm(forms.ModelForm):

    description = forms.CharField(max_length=128, help_text="Please enter a short description for task.")
    command = forms.CharField(widget=forms.widgets.Textarea(), help_text="Please enter the script. (Ex: cd /data/schneider/;ls -lrt)")
    #ltitle = forms.CharField(max_length=128, help_text="Please enter the title id of the task.")
    #lservice = forms.CharField(max_length=128, help_text="Please enter the service id.")
    #lresult = forms.CharField(max_length=128, help_text="Please enter the result id.")


    class Meta:
        # Provide an association between the ModelForm and a model
        model = LinuxOperation
        fields = ('description', 'command')



class FarmForm(forms.ModelForm):
    farmname = forms.CharField(max_length=128, help_text="Please enter the name of the farm.")


    class Meta:
        # Provide an association between the ModelForm and a model
        model = Farm
        fields = ('farmname',)



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    apausername = forms.CharField(max_length=128, required=False, help_text="Please enter your details (Eg. : APA\SESA****).")
    apapassword = forms.CharField(max_length=128, required=False, help_text="Please enter your details.")
    bewenousername = forms.CharField(max_length=128, required=False, help_text="Please enter your details (Eg. : BEWENO\SESA****).")
    bewenopassword = forms.CharField(max_length=128, required=False, help_text="Please enter your details.")
    linuxusername = forms.CharField(max_length=128, required=False, help_text="Please enter your details.")
    linuxpassword = forms.CharField(max_length=128, required=False, help_text="Please enter your details.")
    lbusername = forms.CharField(max_length=128, required=False, help_text="Please enter your details.")
    lbpassword = forms.CharField(max_length=128, required=False, help_text="Please enter your details.")
    class Meta:
        model = UserProfile
        fields = ('apausername', 'apapassword', 'bewenousername', 'bewenopassword', 'linuxusername', 'linuxpassword', 'lbusername', 'lbpassword', 'picture')

class EditProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'website', 'picture')

