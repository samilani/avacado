import os
import sys
from django.utils import timezone

def populate():
    android_idea = add_idea('android app', "This app is for london tube.....")

    android_project = add_project(name = 'London Tube Android App', idea= android_idea)

    add_task(project=android_project, summery="User interface design", description="I will use CSS, Javascript and .. to "
        "design the UI",deadline=timezone.now(), comment='Like the Idea but should work on the CSS part more, how about a '
        'little bit of bootstrap' )




def add_idea(title, description):
    i = Idea.objects.get_or_create(title = title, description = description)[0]
    return i

def add_project(name, idea):
    p = Project.objects.get_or_create(name = name, idea = idea)[0]
    return p

def add_task(project, summery, description, deadline, comment):
    t = Task.objects.get_or_create(project = project, summery = summery, description = description, deadline = deadline, comment = comment)
    return t

if __name__ == '__main__':
    print "Starting Project population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avacado.settings')
    from project.models import Idea, Task, Project, Supervisor, Student
    populate()