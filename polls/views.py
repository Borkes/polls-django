from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    #template = loader.get_template('polls/index.html')
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)  #使用render函数代替

#用try catch 捕获错误
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id) #用get_object_or_404代替上面try except捕获错误
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)