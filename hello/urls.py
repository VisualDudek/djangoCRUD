from django.urls import path
from hello import views
from hello.models import LogMessage

# make a variable for the new view, which retrieves the five most recent
#LogMessage objects

# home_list_view = views.HomeListView.as_view(
#     queryset=LogMessage.objects.order_by("-log_date")[:5],
#     context_object_name="message_list",
#     template_name="hello/home.html",
# )

# modyify the path to the home page to use the 'home_list_view' variable
#depricated: 'path("", views.home, name="home"),'

urlpatterns = [
    path("", views.HomeListView.as_view(), name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("hello_render/<name>", views.hello_render, name="hello_render"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("log/delete/<id>", views.LogMessageDeleteView.as_view(), name="deleteLogMessage"),
    path("log/create/", views.LogMessageCreateView.as_view(), name='createMessage'),
]