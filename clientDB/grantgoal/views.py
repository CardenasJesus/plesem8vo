from django.shortcuts import render, redirect
from django.views import generic
import requests
from .forms import CreateGrantGoalClientForm
# Create your views here.

class CreateGrantGoalClientView(generic.View):
    template_name = "grantgoal/create_gg_cl.html"
    context = {}
    payload = {}
    url = "http://127.0.0.1:8000/api/v1/create/grantgoal/"
    response = None
    form_class = CreateGrantGoalClientForm
    def get(self, request):
        self.context = {
            "form": self.form_class,
        }
        return render(request, self.template_name, self.context)

    def post(self, request):
        payload = {
            "ggname": request.POST["ggname"],
            "description": request.POST["description"],
            "user": request.user.username,
            "days_duration": request.POST["days_duration"],
            "priority": 'HG',
            "state": 'Not Started',
            "status": request.POST["status"],
            "slug": request.POST["slug"],
        }
        self.response = requests.post(url=self.url, data=payload)
        return redirect("gg:list_gg_cl")




class ListGrantGoalClientView(generic.View):
    template_name = "grantgoal/list_gg_cl.html"
    url = "http://127.0.0.1:8000/api/v1/list/grantgoal/"
    response = None
    context= {}
    def get(self, request):
        self.response = requests.get(url=self.url)
        self.context = {
            "grantgoals": self.response.json(),
        }
        return render(request, self.template_name, self.context)




class DetailGrantGoalClientView(generic.View):
    template_name = "grantgoal/detail_gg_cl.html"
    context = {}
    url = "http://127.0.0.1:8000/api/v1/detail/grantgoal/"
    response = None

    def get(self, request, pk):
        self.url = self.url + f'{pk}/'
        self.response = requests.get(url=self.url)
        self.context = {
            "grantgoal": self.response.json(),
        }
        return render(request, self.template_name, self.context)

