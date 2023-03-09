from django.shortcuts import render, redirect, get_object_or_404
from .models import Resource
from .forms import ResourceForm
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def list_resources(request):
    resources = Resource.objects.all()
    # add .orderby('date_added') ???
    return render(request, 'resources/index.html', {'resources': resources})


@login_required
def get_info(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'resources/get_info.html', {'resource': resource})


@login_required
def add_resource(request):
    if request.method == 'POST':
        new_resource = ResourceForm(request.POST)
        if new_resource.is_valid():
            new_resource.save()
            return redirect('home')
    form = ResourceForm()
    return render(request, 'resources/add_resource.html', {'form': form})


@login_required
def edit_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        edited_resource = ResourceForm(request.POST, instance=resource)
        if edited_resource.is_valid():
            edited_resource.save()
            return redirect('home')
    form = ResourceForm(instance=resource)
    return render(request, 'resources/edit_resource.html', {'form': form, 'pk': pk})


# @ user_passes_test(lambda user: user.is_staff)
@login_required
def delete_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        resource.delete()
        return redirect('home')
    return render(request, 'resources/delete_resource.html')
