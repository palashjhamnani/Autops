from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

import paramiko
import logging

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response as render
from django.template import RequestContext as ctx

from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
from django.http import JsonResponse
import socket

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from autosys.models import Category, LinuxServer, LinuxOperation
from autosys.models import Page
from autosys.models import Farm
from django.contrib.auth.models import User
from autosys.models import UserProfile
from autosys.forms import UserForm
from autosys.forms import UserProfileForm
from autosys.forms import CategoryForm, LinuxServerForm
from autosys.forms import PageForm, LinuxOperationForm
from autosys.forms import FarmForm, EditProfile

import requests
import wmi
import pythoncom
import socket, sys
import os

# Create your views here.
from django.http import HttpResponse

def idol(request):


    return render(request,'autosys/idol.html')

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:10]
    context_dict = {'categories': category_list}

    if request.user.is_authenticated():
        return HttpResponseRedirect('/autosys/welcome/')


    # Render the response and send it back!
    return render(request, 'autosys/index.html', context_dict)



@login_required
def about(request):
    updated = False

    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user.userprofile)

        if form.is_valid():

            profile_obj = form.save(commit=False)
            profile_obj.user = request.user
            if 'picture' in request.FILES:
                profile_obj.picture = request.FILES['picture']
            profile_obj.save()
            updated = True



        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = EditProfile()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'autosys/about.html', {'form': form, 'updated': updated})


@login_required
def welcome(request):

    return render(request, 'autosys/welcome.html')

@login_required
def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        context_dict['server_loadreqlink'] = category.loadreqlink
        context_dict['server_loadenable'] = category.loadenable
        context_dict['server_loaddisable'] = category.loaddisable
        context_dict['server_linkk'] = category.linkk
        context_dict['server_ip'] = category.serverip


        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug

    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'autosys/category.html', context_dict)


@login_required
def linuxserver(request, linuxserver_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        linuxserver = LinuxServer.objects.get(slug=linuxserver_name_slug)
        context_dict['linuxserver_servname'] = linuxserver.servname
        context_dict['linuxserver_loadreqlink'] = linuxserver.loadreqlink
        context_dict['linuxserver_loadenable'] = linuxserver.loadenable
        context_dict['linuxserver_loaddisable'] = linuxserver.loaddisable
        context_dict['linuxserver_slink'] = linuxserver.slink
        context_dict['linuxserver_ip'] = linuxserver.serverip


        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        linuxoperations = LinuxOperation.objects.filter(linuxserver=linuxserver)

        # Adds our results list to the template context under name pages.
        context_dict['linuxoperations'] = linuxoperations
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['linuxserver'] = linuxserver
        context_dict['linuxserver_name_slug'] = linuxserver_name_slug


    except LinuxServer.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'autosys/linuxserver.html', context_dict)

@login_required
def farm(request, farm_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        farm = Farm.objects.get(slug=farm_name_slug)
        context_dict['farm_name'] = farm.farmname
        context_dict['farm_name_slug'] = farm_name_slug


        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        categories = Category.objects.filter(farm=farm)
        linuxservers = LinuxServer.objects.filter(farm=farm)

        # Adds our results list to the template context under name pages.
        context_dict['categories'] = categories
        context_dict['linuxservers'] = linuxservers
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['farm'] = farm


    except Farm.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'autosys/farm.html', context_dict)



@login_required
def add_farm(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = FarmForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = FarmForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'autosys/add_farm.html', {'form': form})




@login_required
def add_category(request, farm_name_slug):

    try:
        cat = Farm.objects.get(slug=farm_name_slug)
    except Farm.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            if cat:
                category = form.save(commit=False)
                category.farm = cat
                #category.views = 0
                category.save()
                # probably better to use a redirect here.
                return farm(request, farm_name_slug)
        else:
            print form.errors
    else:
        form = CategoryForm()

    context_dict = {'form':form, 'farm': cat}

    return render(request, 'autosys/add_category.html', context_dict)


@login_required
def add_linuxserver(request, farm_name_slug):

    try:
        cat = Farm.objects.get(slug=farm_name_slug)
    except Farm.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = LinuxServerForm(request.POST)
        if form.is_valid():
            if cat:
                linuxserver = form.save(commit=False)
                linuxserver.farm = cat
                #category.views = 0
                linuxserver.save()
                # probably better to use a redirect here.
                return farm(request, farm_name_slug)
        else:
            print form.errors
    else:
        form = LinuxServerForm()

    context_dict = {'form':form, 'farm': cat}

    return render(request, 'autosys/add_linuxserver.html', context_dict)




@login_required
def add_page(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                tryy = Page.objects.all().order_by("-id")[0]
                ser = tryy.service
                res = tryy.result
                dele = tryy.delete
                page.service = int(ser)+1
                page.result = int(res)+1
                page.delete = int(dele)+1

                #page.views = 0
                page.save()
                # probably better to use a redirect here.
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form':form, 'category': cat}

    return render(request, 'autosys/add_page.html', context_dict)


@login_required
def add_linuxoperation(request, linuxserver_name_slug):

    try:
        cat = LinuxServer.objects.get(slug=linuxserver_name_slug)
    except LinuxServer.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = LinuxOperationForm(request.POST)
        if form.is_valid():
            if cat:
                linuxoperation = form.save(commit=False)
                linuxoperation.linuxserver = cat
                tryy = LinuxOperation.objects.all().order_by("-id")[0]
                ser = tryy.lservice
                res = tryy.lresult
                tle = tryy.ltitle
                linuxoperation.ltitle = int(tle)+1
                linuxoperation.lservice = int(ser)+1
                linuxoperation.lresult = int(res)+1
                #linuxoperation.views = 0
                linuxoperation.save()
                # probably better to use a redirect here.
                return linuxserver(request, linuxserver_name_slug)
        else:
            print form.errors
    else:
        form = LinuxOperationForm()

    context_dict = {'form':form, 'linuxserver': cat}

    return render(request, 'autosys/add_linuxoperation.html', context_dict)


@login_required
def delete_service(request):

    if request.method == 'POST':
        if request.is_ajax():

            pageid = request.POST.get('pageid')
            Page.objects.filter(id=pageid).delete()

            numb = "Service Deleted"
            data = {"status": numb}
            return JsonResponse(data)



    return render(request,'autosys/category.html')




def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            else:
                profile.picture = "profile_images/default.png"

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors
            u_errors = user_form.errors
            p_errors = profile_form.errors
            err = True
            return render(request, 'autosys/index.html', {'err': err, 'u_errors': u_errors, 'p_errors': p_errors})

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'autosys/index.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.

    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')
        logged_off = True

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                logged_off = False
                return HttpResponseRedirect('/autosys/welcome/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your autosys account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'autosys/index.html', {'logged_off': logged_off})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'autosys/index.html')



@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/autosys/')




@login_required
def enable(request):
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            pythoncom.CoInitialize()
            service = request.POST.get('service')
            server_loadid = request.POST.get('server_loadid')
            tt = server_loadid
            category = Category.objects.get(loadreqlink=tt)
            server_loaddisable = category.loaddisable
            server_loadenable = category.loadenable
            server_linkk = category.linkk
            profile = UserProfile.objects.get(user=request.user)
            lbusername = profile.lbusername
            lbpassword = profile.lbpassword

            if service == 'enable':
                p = requests.post(server_linkk, auth=(lbusername,lbpassword), data=server_loadenable)

                numb = 'Server enabled'
                data = {"status": numb}
                return JsonResponse(data)

            if service == 'disable':
                p = requests.post(server_linkk, auth=(lbusername,lbpassword), data=server_loaddisable)


                numb = 'Server disabled'
                data = {"status": numb}

            return JsonResponse(data)

            pythoncom.CoUninitialize()

    return render(request,'autosys/index.html')



@login_required
def homee(request):
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            pythoncom.CoInitialize()
            service = request.POST.get('service')
            service_name = request.POST.get('service_name')
            uname = request.POST.get('usern')

            ip = Page.objects.get(id=service_name)
            server = ip.category.serverip
            type = ip.category.type
            serv_name = ip.title

            u = User.objects.get(username=uname)
            apa_username = u.userprofile.apausername
            apa_password = u.userprofile.apapassword
            beweno_username = u.userprofile.bewenousername
            beweno_password = u.userprofile.bewenopassword

            if type == 'Primary':
                userid = apa_username
                upass = apa_password

            if type == 'DMZ':
                userid = beweno_username
                upass = beweno_password



            if service == 'stop':
                from socket import *
                c = wmi.WMI(server, user=userid, password=upass)
                for service in c.Win32_Service(Name=serv_name):
                    result, = service.StopService()
                numb = 'Service stopped'
                #numbb = server
                data = {"status": numb}
                #Returning same data back to browser.It is not possible with Normal submit
                return JsonResponse(data)


            if service == 'start':
                from socket import *
                c = wmi.WMI(server, user=userid, password=upass)
                for service in c.Win32_Service(Name=serv_name):
                    result, = service.StartService()
                numb = 'Service started'
                #numbe = userid
                data = {"status": numb}
                #Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(data)
            #c = wmi.WMI(ip, user=username, password=password)
            #for service in c.Win32_Service(Name="Spooler"):
            #   result, = service.StopService()
            pythoncom.CoUninitialize()
            #Always use get on request.POST. Correct way of querying a QueryDict.
            #email = request.POST.get('email')
            #password = request.POST.get('password')

    #Get goes here
    return render(request,'autosys/index.html')




import re

from django.db.models import Q

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):

    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['name',])

        found_entries = Category.objects.filter(entry_query)

    return render(request, 'autosys/index.html', { 'query_string': query_string, 'found_entries': found_entries })



@login_required
def linuxtask(request):
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            user_name = request.POST.get('username')
            linux_id = request.POST.get('linuxid')

            u = User.objects.get(username=user_name)
            linuxusername = u.userprofile.linuxusername
            linuxpassword = u.userprofile.linuxpassword

            linuxoperation = LinuxOperation.objects.get(id=linux_id)
            command = linuxoperation.command
            serverip = linuxoperation.linuxserver.serverip

            cmd = command
            host = serverip
            user = linuxusername
            passwd = linuxpassword
            ssh = paramiko.SSHClient()

            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=user, password=passwd)
            stdin, stdout, stderr = ssh.exec_command(cmd)
                #stdin.write(passwd + '\n')
                #stdin.flush()
            resultt = stdout.readlines()
            ssh.close()

            data = {"result": resultt}
            #Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(data)

    return render(request,'autosys/linuxserver.html')



@login_required
def reboot(request):
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            pythoncom.CoInitialize()
            service = request.POST.get('service')
            server_loadid = request.POST.get('server_loadidd')

            uname = request.POST.get('usr')

            u = User.objects.get(username=uname)
            apa_username = u.userprofile.apausername
            apa_password = u.userprofile.apapassword
            beweno_username = u.userprofile.bewenousername
            beweno_password = u.userprofile.bewenopassword

            tt = server_loadid
            category = Category.objects.get(id=tt)
            server_ip = category.serverip
            type = category.type

            if type == 'Primary':
                userid = apa_username
                upass = apa_password

            if type == 'DMZ':
                userid = beweno_username
                upass = beweno_password




            if service == 'reboot':
                ip =server_ip
                username = userid
                password = upass
                from socket import *
                c = wmi.WMI(ip, user=username, password=password)
                ##other_machine = p
                ##c = wmi.WMI (computer=other_machine, privileges=["RemoteShutdown"])
                os = c.Win32_OperatingSystem (Primary=1)[0]
                os.Reboot ()

                numb = "Server Rebooted"
                data = {"status": numb}

            return JsonResponse(data)

            pythoncom.CoUninitialize()

    return render(request,'autosys/index.html')