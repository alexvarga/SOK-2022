from django.contrib import admin

# Register your models here.
from .models import Attribute, Node, Link

# Register your models here.


@admin.register(Attribute)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Node)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Link)
class GradeAdmin(admin.ModelAdmin):
    pass

