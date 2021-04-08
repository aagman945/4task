from django.shortcuts import render
from .models import Question,Answer
from .forms import AnswerForm,QuestionForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    quests=Question.objects.all()
    return render(request, 'index.html',{'quests':quests})

def detail(request, id):
    quest=Question.objects.get(pk=id)
    ans=Answer.objects.all()
    answer=Answer.objects.filter(question=quest)
    answerform=AnswerForm
    if request.method=='POST':
        answerData=AnswerForm(request.POST)
        if answerData.is_valid():
            answer=answerData.save(commit=False)
            answer.question=quest
            answer.user=request.user
            answer.save()
    return render(request,'detail.html',{'quest':quest,'answer':answer,'answerform':answerform,'ans':ans})

def ask(request):
    questionform=QuestionForm
    if request.method=='POST':
        questionData=QuestionForm(request.POST)
        if questionData.is_valid():
            question=questionData.save(commit=False)
            question.user=request.user
            question.save()
    return render(request,'ask.html',{'questionform':questionform})
