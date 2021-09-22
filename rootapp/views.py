from typing import Container
from django.http.response import HttpResponse
from django.shortcuts import render
from rootapp.forms import EmailForm
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
def root(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = "emailFormQuery"
            body = {
                "name" : form.cleaned_data["full_name"],
                "email" : form.cleaned_data["email"],
                "message" : form.cleaned_data["message"]
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, "from@gmail.com", ["to@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid Header")
            form = EmailForm()
            return render(request, 'rootapp/index.html', {"submitted" : True})
    form = EmailForm()
    return render(request, 'rootapp/index.html', {"form" : form})