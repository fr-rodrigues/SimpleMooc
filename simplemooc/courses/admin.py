from django.contrib import admin
from .models import Course, Enrollment, Announcement, Comment, Lesson, Material


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    # slug automatico
    prepopulated_fields = {'slug': ('name',)}


class MaterialInlineAdmin(admin.StackedInline):
    model = Material


class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'release_date']
    search_fields = ['name', 'number']
    list_filter = ['created_at']

    inlines = [
        MaterialInlineAdmin
    ]


admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment, Material])
admin.site.register(Lesson, LessonAdmin)
