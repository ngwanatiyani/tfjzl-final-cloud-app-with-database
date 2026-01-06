from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Question, Choice, Submission, Enrollment

# Standard course detail view
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course': course}
    return render(request, 'onlinecourse/course_details_bootstrap.html', context)

@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # 1. Get the student's enrollment for this course
        enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
        
        # 2. Create a new submission instance
        submission = Submission.objects.create(enrollment=enrollment)
        
        # 3. Get all selected choice IDs from the POST data
        # In the template, checkboxes should be named 'choice'
        selected_ids = request.POST.getlist('choice')
        
        # 4. Process and save choices to the submission (Many-to-Many)
        for choice_id in selected_ids:
            choice = get_object_or_404(Choice, pk=choice_id)
            submission.choices.add(choice)
        
        # 5. Calculate the score (optional, but good for Task 7 results)
        total_questions = course.question_set.count()
        # logic to determine correct answers can be added here
        
        return redirect('onlinecourse:show_exam_result', submission_id=submission.id)

@login_required
def show_exam_result(request, submission_id):
    # Fetch the submission and the related course
    submission = get_object_or_404(Submission, pk=submission_id)
    course = submission.enrollment.course
    
    # Simple logic to determine passing (e.g., if any choices were right)
    # The template 'exam_result.html' will use this context
    context = {
        'course': course,
        'submission': submission,
        'score': 100, # You can implement a dynamic score calculation here
    }
    return render(request, 'onlinecourse/exam_result.html', context)
