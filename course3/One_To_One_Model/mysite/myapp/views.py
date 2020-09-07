from django.shortcuts import render,redirect,get_object_or_404
from .models import Breed,Cat
from django.urls import reverse,reverse_lazy
from django.views import View
from .forms import BreedForm,CatForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class CatList(LoginRequiredMixin,View):
    def get(self,request):
        bc      = Breed.objects.all().count()
        cl      = Cat.objects.all()
        context = {'breed_count':bc,'cat_list':cl}
        return render(request,'myapp/cat_list.html',context)

class BreedList(LoginRequiredMixin,View):
    def get(self,request):
        bl      = Breed.objects.all()
        ctx     = {'breed_list':bl}
        return render(request,'myapp/breed_list.html',ctx)

class BreedCreate(LoginRequiredMixin,View):
    template = "myapp/breed_form.html"
    success_url = reverse_lazy('cats:all')

    def get(self,request):
        form = BreedForm()
        ctx = {'form':form}
        return render(request,self.template,ctx)    

    def post(self,request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,self.template,ctx)
        breed = form.save()
        return redirect(self.success_url)

class CatCreate(LoginRequiredMixin,CreateView):
    model  = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin,UpdateView):
    model  = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin,UpdateView):
    model  = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all') 

class BreedDelete(LoginRequiredMixin,DeleteView):
    model  = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all') 


class CatDelete(LoginRequiredMixin,DeleteView):
    model  = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all') 
