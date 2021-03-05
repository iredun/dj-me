from django.shortcuts import render

from main.models import Skill, Language


def index(request):
    context = {
        "title": "Редун Иван",
        'skills': Skill.objects.order_by('-percent').all(),
        'langs': Language.objects.order_by('-stars').all()
    }

    return render(request, 'main/index.html', context)
