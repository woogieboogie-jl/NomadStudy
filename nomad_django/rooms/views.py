from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models

class HomeView(ListView):

    """Homeview Definition"""
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = 'created'
    context_object_name = 'rooms'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context['now'] = now
        return context

    
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, 'rooms/detail.html', context = {
#             'room' : room,
#         })
#     except models.Room.DoesNotExist:
#         # return redirect(reverse('core:home'))
#         raise Http404()

class RoomDetail(DetailView):
    model = models.Room
