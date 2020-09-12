from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



## now login for listview and detail view
## make the whole crud with LoginRequired Mixin
## and ue it in the UPDATE,CREATE and DELETE
## the list and detail view will be no login
class AdListView(ListView):
    pass