from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .forms import VideoForm
from .models import Video


def home(request):
    """view for a home page that is shown if a user navigates to the base url. passes app_name into home.html to fill the template""" 
    app_name = "Cooking Videos"
    return render(request, 'video_collection/home.html', {'app_name': app_name})

def add(request):
    """view that has split functionality depending on the request method. If method is GET, directs user to a new form to add a new video. If method is POST, saves that video to the database and displays a confirmation message"""
    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            try:

                new_video_form.save()
                return redirect('video_list')
            except ValidationError:
                messages.warning(request, 'Invalid Youtube URL')
            except IntegrityError:
                messages.warning(request, 'You already added that video')

        #if form is invalid, adds a warning message to the messages object, which will be displayed in add.html. Redirects to add.html with the invalid form data auto-populated
        messages.warning(request, 'Please check the data entered')
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

    
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_collection/video_list.html', {'videos': videos})