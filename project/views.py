from django.template import RequestContext
from django.shortcuts import render_to_response
from project.forms import ProjectForm
def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am from the context"}
    return render_to_response('project/index.html', context_dict, context)

