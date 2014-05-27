# coding=utf-8
# Create your views here.

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from polls.forms import AddPollForm, AddChoiceForm

from polls.models import Choice, Poll


class IndexView(generic.ListView):
    template_name = 'polls/list.html'
    context_object_name = 'poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        # print self.request.user.username
        return Poll.objects.filter(user=self.request.user.pk)


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Poll.objects.all()


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def add_poll(request):
    # return render(request, 'polls/add_poll.html')
    if request.method == "POST":
        form = AddPollForm(request.POST)
        if form.is_valid():
            # user = request.user.username
            # question = form.cleaned_data['question']
            # pub_date = timezone.now()
            form.save()
            return redirect('polls:add_choice')

    else:
        form = AddPollForm() #request.user.username)

    poll = Poll.objects.all()

    return render(request, 'polls/add_poll.html',
                  {
                      'poll': poll,
                      'form': form,
                  })

def add_choice(request):
    # return render(request, 'polls/add_poll.html')
    if request.method == "POST":
        form = AddChoiceForm(request.POST)
        if form.is_valid():
            # user = request.user.username
            # question = form.cleaned_data['question']
            # pub_date = timezone.now()
            form.save()
            return redirect('polls:add_choice')

    else:
        form = AddChoiceForm() #request.user.username)
    choice = Choice.objects.all()

    return render(request, 'polls/add_choice.html',
                  {
                      'Choice': Choice,
                      'form': form,
                  })


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'poll': p, 'error_message': "You didn't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
