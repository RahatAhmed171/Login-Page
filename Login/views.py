from django.shortcuts import render,HttpResponse
from django.views import View
from .models import permission
from django.views.generic.edit import FormView
from .form import Geeksform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect


# Create your views here.
class GeeksFormView(FormView):
    form_class=AuthenticationForm
    template_name='Login/parent.html'
    success_url='home'

    def form_valid(self,form):
        login(self.request,form.get_user())
        return HttpResponseRedirect(self.success_url)
class home(View):
    template_name='Login/home.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
class about(View):
    template_name='Login/about.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    def post(self,request,*args,**kwargs):
        return HttpResponseRedirect('parent')

class JS_Tutorial(View):
    template_name='Login/corey.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
#def add(request):
 #   val1=request.POST['num1']
  #  val2=request.POST['num2']
   # all_stuf=permission.objects.all()
    #for stuff in all_stuf:
     #   the_username=stuff.username
      #  the_password=stuff.password

    #if val1==the_username and val2==the_password:


     #   return render(request,'Login/parent.html')
    #else:
     #   return render(request,'Login/about.html')

