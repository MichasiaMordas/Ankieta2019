from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import  Question, Choice, Uzytkownik, Alkohol, Czestosc


class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'app/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'app/results.html'

def Wyniki(request):
    return render(request, 'app/wyniki.html', {})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        if question_id<5:
            selected_choice = question.uzytkownik_set.get(pk=request.POST['uzytkownik'])
        if question_id>4 and question_id<8:
            selected_choice = question.czestosc_set.get(pk=request.POST['czestosc'])
        if question_id>7:
            selected_choice = question.alkohol_set.get(pk=request.POST['alkohol'])
    except (KeyError, Uzytkownik.DoesNotExist):
        return render(request, 'app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        question_id += 1

    if question_id < 9:
        return HttpResponseRedirect(reverse('app:detail', args=(question.id+1,)))
    if request.POST['alkohol'] == "1":
        return HttpResponseRedirect(reverse('app:detail', args=(question.id+1,)))
    if request.POST['alkohol'] == "2":
        return HttpResponseRedirect(reverse('app:detail', args=(question.id+2,)))
    if request.POST['alkohol'] == "3":
        return HttpResponseRedirect(reverse('app:detail', args=(question.id+3,)))
    if request.POST['alkohol'] == "4":
        return HttpResponseRedirect(reverse('app:detail', args=(question.id+4,)))
    if request.POST['alkohol'] == "5":
        return render(request, "app/results.html")
    if question_id > 9:
        return render(request, "app/results.html")