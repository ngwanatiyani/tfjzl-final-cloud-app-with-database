from django.db import models
from django.contrib.auth.models import User

# Add or ensure these exist as they are required for Submission
class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()
    def __str__(self): return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    instructors = models.ManyToManyField(Instructor)
    def __str__(self): return self.name

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self): return self.title

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # Link to Course as per rubric
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1) # Required field

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE) # REQUIRED
    choices = models.ManyToManyField(Choice) # REQUIRED
    date_submitted = models.DateTimeField(auto_now_add=True)
