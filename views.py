from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from {{ app_name }}.models import *

# Create your views here.

# For more information on this file, see
# https://docs.djangoproject.com/en/{{ docs_version }}/intro/tutorial03/

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {
        'active_nav': '{{ app_name }}',
        'latest_poll_list': latest_poll_list
    }
    return render(request, '{{ app_name }}/index.html', context)

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    context = {
        'active_nav': '{{ app_name }}',
        'poll': poll
    }
    return render(request, '{{ app_name }}/detail.html', context)

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    context = {
        'active_nav': '{{ app_name }}',
        'poll': poll
    }
    return render(request, '{{ app_name }}/results.html', context)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, '{{ app_name }}/detail.html', {
            'active_nav': '{{ app_name }}',
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
        return detail(request, poll_id)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('{{ app_name }}:results', args=(p.id,)))