from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from cities.models import City
from trains.forms import TrainForm
from trains.models import Train


class TrainListView(ListView):
    model = Train
    template_name = 'trains/home.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TrainForm()
        context['form'] = form
        return context


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Created'

class TrainDetailView(DetailView):
    model = Train
    template_name = 'trains/detail.html'


class TrainDeleteView(SuccessMessageMixin, DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Deleted'


class TrainUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Updated'


def from_city(request, pk):
    city = City.objects.get(pk=pk)
    objects = city.from_city_set.all()
    return render(request, 'trains/from_city.html', {'objects': objects, 'city': city})


def to_city(request):
    pass
