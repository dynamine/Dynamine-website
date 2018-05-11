from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic

class Create_Cluster(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cluster_admin/create_cluster.html'


def overview(request):
    if request.user.is_authenticated:
        context = {} #TODO: populate with cluster state databases
        return render(request, 'cluster_admin/overview.html', context)
    else:
        return redirect(reverse('login'))
