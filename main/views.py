from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import (
    Blog , HomeBG,
    OurService , OurGallery,
    AboutUS, Icons
)
from .forms import ContactUsForm
from django.core.mail import send_mail
from Vertex.settings import EMAIL_HOST_USER


class HomeListView(ListView):
    template_name = 'index.html'

    @staticmethod
    def __extract_all_data():
        blogs = Blog.objects.all()
        homebg = HomeBG.objects.get()
        services = OurService.objects.get()
        galleries = OurGallery.objects.all()
        aboutus = AboutUS.objects.get()
        icons = Icons.objects.all()
        

        context = {
            'blogs':blogs,
            'homebg':homebg,
            'services':services,
            'galleries':galleries,
            'aboutus': aboutus,
            'icons': icons,
        }

        return context


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        context = self.__extract_all_data()

        return render(request, self.template_name, context=context)


    def post(self , request):
        context = self.__extract_all_data()

        form = ContactUsForm(request.POST)
        
        if form.is_valid():
            email = request.POST['email']

            send_mail(
                subject='Vertex FeedBack',
                message='Thx For review',
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

            form.save()
        else:
            form = ContactUsForm()

        context.update({'form':form})


        return render(request, self.template_name, context=context)
























