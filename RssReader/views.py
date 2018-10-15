# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

from django.shortcuts import render_to_response
from RssReader.forms import RssReaderForm

from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
import requests
from bs4 import BeautifulSoup
from django.contrib import messages


method_decorator(csrf_protect)
def RssReaderView(request):
    if request.method == "POST":
        form = RssReaderForm(request.POST)
        url = str(request.POST.get('url'))
        res = requests.get(url)
        if res.status_code == 200:
            messages.success(request, "WebPage opened Successfully")
            content = BeautifulSoup(res.text, 'html.parser')
            title = content.find("h1", {"class": "story-body__h1"}).text
            image = content.find("img", {"class": "js-image-replace"}).get('src')
            # data = content.find("p", {"class": "story-body__introduction"}).text
            p_text = ""
            container = content.find("div", {"class": "story-body__inner"})
            for p in container.findChildren("p"):
                p_text += p.text
            return render(request, 'display_content.html', {"form": form, "title" : title, "image": str(image),
                                                             "p_text": p_text})
        else:
            messages.error(request, "Error while opening Webpage")
            return render(request, 'index.html', {"form": form})

    else:
        form = RssReaderForm()
        return render(request, 'index.html' , {"form": form})
