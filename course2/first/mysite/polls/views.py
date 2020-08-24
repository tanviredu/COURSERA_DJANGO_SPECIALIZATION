from django.shortcuts import render
from django.http      import HttpResponse,Http404
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
