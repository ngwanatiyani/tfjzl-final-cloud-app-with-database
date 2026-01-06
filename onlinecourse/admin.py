from django.contrib import admin
# Ensure 7 classes are imported
from .models import Course, Lesson, Instructor, Question, Choice, Submission, Enrollment

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'course'] # Added list_display

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course'] # Added list_display

admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Choice) # This makes the 7th registered model if needed
