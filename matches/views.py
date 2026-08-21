from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Match
from datetime import datetime

TODAY = datetime(2026, 8, 23, 19, 30, 0)

def matches_all_list(request):
    template = loader.get_template('matches/matches.html')
    matches = Match.objects.order_by('-start_time')
    rendered = template.render({'matches': matches, 'page_type': 'all'})

    return HttpResponse(rendered)

def matches_live_list(request):
    template = loader.get_template('matches/matches.html')
    matches = Match.objects.filter(
        start_time__lte=TODAY,
        end_time__gte=TODAY
    ).order_by('start_time')
    rendered = template.render({'matches': matches, 'page_type': 'live'})

    return HttpResponse(rendered)

def matches_future_list(request):
    template = loader.get_template('matches/matches.html')
    matches = Match.objects.filter(start_time__gt=TODAY).order_by('start_time')
    rendered = template.render({'matches': matches, 'page_type': 'future'})

    return HttpResponse(rendered)

def match_by_id(request, match_id):
    template = loader.get_template('matches/match_by_id.html')
    match = get_object_or_404(Match, pk=match_id)
    rendered = template.render({'match': match})

    return HttpResponse(rendered)
