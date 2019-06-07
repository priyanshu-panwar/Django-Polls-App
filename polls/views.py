from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.utils import timezone
from django.views import generic
import datetime
from django.views.generic.edit import CreateView
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if 1==0: #question.date_valid<=timezone.now():
        return render(request, 'polls/results.html question.id', {'error_message': "The Question is no longer available for voting."})
    else:
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except(KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {'question':question, 'error_message':"You didnt select any choice."})
        else:
            selected_choice.votes+=1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

'''
class QuestionCreate(CreateView):
    model = Question
    fields ='__all__'
'''