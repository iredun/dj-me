from pprint import pprint

from django.shortcuts import render

from main.forms import ContactFormForm
from main.models import Skill, Language, Education, SocLink, Project, ContactForm


def index(request):
    context = {
        'skills': Skill.objects.order_by('-percent').all(),
        'langs': Language.objects.order_by('-stars').all(),
        'edu_list': Education.objects.order_by('-year_end').all(),
        'soc_links': SocLink.objects.all(),
        'projects': Project.objects.all(),
    }

    return render(request, 'main/index.html', context)


def project_detail(request, pk):
    project = Project.objects.filter(id=pk).first()
    context = {
        'soc_links': SocLink.objects.all(),
        'title': project.name,
        'project': project,
    }

    return render(request, 'main/project_detail.html', context)


def contact_form(request):
    form = ContactFormForm()
    context = {
        'soc_links': SocLink.objects.all(),
    }

    if request.method == 'POST':
        form = ContactFormForm(data=request.POST)
        if form.is_valid():
            form.save()

    context['form'] = form
    return render(request, 'main/contact_form.html', context)
