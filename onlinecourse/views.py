from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson, Question, Choice, Submission


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course': course}
    return render(request, 'onlinecourse/course_details_bootstrap.html', context)


@login_required
def submit(request, lesson_id=None):
    # GET request - show the exam
    if request.method == 'GET':
        lesson_id = request.GET.get('lesson_id')
        if lesson_id:
            lesson = get_object_or_404(Lesson, pk=lesson_id)
            context = {'lesson': lesson}
            return render(request, 'onlinecourse/exam.html', context)
        else:
            return redirect('/')
    
    # POST request - process the submission
    elif request.method == 'POST':
        lesson_id = request.POST.get('lesson_id')
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        
        # Get all questions for this lesson
        questions = lesson.question_set.all()
        total_questions = questions.count()
        correct_answers = 0
        
        # Process each question
        for question in questions:
            # Get all correct choices for this question
            correct_choices = set(question.choice_set.filter(is_correct=True).values_list('id', flat=True))
            
            # Get selected choices from form
            selected_choices = set()
            for choice in question.choice_set.all():
                if f'choice_{choice.id}' in request.POST:
                    selected_choices.add(choice.id)
            
            # Check if the selected choices match the correct choices
            if selected_choices == correct_choices and len(correct_choices) > 0:
                correct_answers += 1
        
        # Calculate score as percentage
        score = (correct_answers / total_questions * 100) if total_questions > 0 else 0
        
        # Create submission record
        submission = Submission.objects.create(
            student=request.user,
            lesson=lesson,
            score=int(score)
        )
        
        # Redirect to result page
        return redirect('show_exam_result', submission_id=submission.id)


@login_required
def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    context = {
        'score': submission.score,
        'submission': submission
    }
    return render(request, 'onlinecourse/exam_result.html', context)
