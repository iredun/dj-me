from django.shortcuts import render

from main.models import Skill, Language, Education


def index(request):
    context = {
        "title": "Редун Иван",
        'skills': Skill.objects.order_by('-percent').all(),
        'langs': Language.objects.order_by('-stars').all(),
        'edu_list': Education.objects.order_by('-year_end').all(),
    }

    return render(request, 'main/index.html', context)
