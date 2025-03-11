from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm

def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            return render(request, 'shortener/index.html', {'form': form, 'short_url': url})
    else:
        form = URLForm()
    return render(request, 'shortener/index.html', {'form': form})

def redirect_to_original(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    return redirect(url.original_url)