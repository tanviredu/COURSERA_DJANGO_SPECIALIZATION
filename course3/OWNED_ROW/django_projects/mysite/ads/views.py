from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ad


## now login for listview and detail view
## make the whole crud with LoginRequired Mixin
## and ue it in the UPDATE,CREATE and DELETE
## the list and detail view will be no login


class AdListView(ListView):
    model = Ad 
    context_object_name = 'ads'


### make the detail view without any authentication

class AdDetailView(DetailView):
    model = Ad
    context_object_name = 'add'

class AdCreateView(LoginRequiredMixin,CreateView):
    model = Ad
    fields = ['title','price','text']

    ## this code will be executed after the form 
    ## is submitted
    ## this will take the form and do further modification
    ## this is the oop way of update view
    ## with further work

    def form_valid(self,form):
        print("form valid is called")
        object = form.save(commit=False)
        object.owner = self.request.user 
        object.save()
        #askt he parent class to execute this form
        return super(AdCreateView,self).form_valid(form)



## update value is like create value
## but remember user can unly update 
## what they create not others

class AdUpdateView(LoginRequiredMixin,UpdateView):
    model = Ad
    fields = ['title','price','text']

    ## change the query set so the update
    ## option will be avilable to user
    ## to his post not other

    def get_queryset(self):
        print('update get_queryset is called')
        ## fetch the query set of the current user
        qs = super(AdUpdateView,self).get_queryset()
        ## now filter this
        return qs.filter(owner=self.request.user)


class AdDeleteView(LoginRequiredMixin,DeleteView):
    model = Ad 

    def get_queryset(self):
        print("delete get_queryset is called")
        qs = super(AdDeleteView,self).get_queryset()
        return qs.filter(owner=self.request.user)
