

# Create your views here.
from django.shortcuts import render
from .models import Question
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from .models import Question, Choice

def quiz(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        total = questions.count()
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                selected_choice = Choice.objects.get(id=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1
        return render(request, 'quiz/result.html', {'score': score, 'total': total})
    return render(request, 'quiz/quiz.html', {'questions': questions})