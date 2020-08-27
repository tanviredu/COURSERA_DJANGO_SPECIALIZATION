from django.shortcuts import render,get_object_or_404
from django.http      import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models          import Question

# Create your views here.
def owner(request):
    return HttpResponse("Hello, world. ba4002d8 is the polls index.");

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output               = '.'.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    context = {"latest_question_list":latest_question_list}
    return render(request,'polls/index.html',context)

def details(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists")

    return render(request,'polls/detail.html',{'question':question})
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})