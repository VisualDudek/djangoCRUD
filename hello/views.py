from django.shortcuts import render
from django.http import HttpResponse
import re
from datetime import datetime
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     return HttpResponse("Hello, Django!")

def home_depricated(request):                   # NOTE: depricated, new: class HomeListView
    return render(request, "hello/home.html")

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage
    queryset=LogMessage.objects.order_by("-log_date")[:5]
    context_object_name="message_list"
    template_name="hello/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

class LogMessageDeleteView(DeleteView):
    model = LogMessage
    success_url = reverse_lazy('home') 
    template_name = "hello/confirm.html"
    pk_url_kwarg = 'id'

class LogMessageCreateView(CreateView):
    model = LogMessage
    form_class = LogMessageForm
    # fields = ['message']

    def form_valid(self, form):
        message = form.save(commit=False)
        message.log_date = datetime.now()
        message.save()
        return redirect("home")
    
def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)


def hello_render(request, name):
    return render(
        request,
        'hello/hello_render.html',context={
            'name': name,
            'date': datetime.now(),
        }
    )


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})

# TIP: To make it easier to repeatedly navigate to a specific URL ...
print('--- TIP ---')
print('http://127.0.0.1:8000')
print('http://127.0.0.1:8000/log/create')
print('http://127.0.0.1:8000/hello/Marcin')
print('http://127.0.0.1:8000/hello_render/Marcin')
