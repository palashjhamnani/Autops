from django import template
from autosys.models import Category
from autosys.models import Farm
from autosys.models import LinuxServer

register = template.Library()
#farmname = Farm.objects.farmname()

@register.inclusion_tag('autosys/dogs.html')
def get_farm_list():
    return {'dogs': Farm.objects.all()}

@register.inclusion_tag('autosys/cats.html')
def get_category_list():
    return {'cats': Category.objects.all()}

@register.inclusion_tag('autosys/cows.html')
def get_linux_server_list():
    return {'cows': LinuxServer.objects.all()}