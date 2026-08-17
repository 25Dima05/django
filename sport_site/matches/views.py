from django.http import HttpResponse
from django.template import loader
from .models import Match


def matches_list(request):
    template = loader.get_template("matches/matches.html")
    matches = Match.objects.order_by('-start_time')
    rendered = template.render(request, {'matches': matches})

    return HttpResponse(rendered)