from django.template import RequestContext
from django.shortcuts import render_to_response
from idea.models import Idea
def index(request):
    context = RequestContext(request)

    # Query for categories - add the list to our context dictionary.
    idea_list = Idea.objects.all()
    context_dict = {'idea': idea_list}
    return render_to_response('idea/index.html', context_dict, context)