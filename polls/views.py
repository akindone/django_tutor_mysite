from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# from django.http import Http404
# from django.template import loader
from .models import Question,Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_lists
    #}
    #return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
    # ------
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request,'polls/detail.html',{'question':question})
    # ------
    # return HttpResponse("You are looking at question %s."% question_id)


def results(request,question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request,'polls/results.html',{'question':question})
    # ------
    # response = "You are looking at the results of question %s."
    # return HttpResponse(response % question_id)

def vote(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        # redisplay the quesiton voting form.
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You did not select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if a user hit the Back button
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    # ------
    # return HttpResponse("You're voting on question %s." % question_id)
