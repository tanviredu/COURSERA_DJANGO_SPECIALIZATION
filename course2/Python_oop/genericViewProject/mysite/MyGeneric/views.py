from django.shortcuts import render

from django.contrib.admin.widgets import AdminDateWidget

from django.urls import reverse_lazy
### importing the generic views
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Publisher
from .models import Book
from .models import Author
from .forms import BookForm



class PublisherList(ListView):
    model = Publisher




# Detail View with additional Data
# Often you need to present some extra information beyond that provided by the generic view.
# For example, 
# think of showing a list of all the books on each publisher detail page.
# The DetailView generic view provides the publisher to the context
# but how do we get additional information in that template?

# The answer is to subclass DetailView and provide
# your own implementation of the get_context_data method.


class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        ## query for adding additional data
        context['book_list'] = Book.objects.all()
        return context


class BookCreate(CreateView):
    form_class = BookForm
    template_name = "MyGeneric/book_form.html"
    success_url = "/publishers"



class UpdateBook(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('p')

class DeleteBook(DeleteView):
    model = Book
    success_url = reverse_lazy('p')