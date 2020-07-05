from django.contrib import messages
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import Context
from django.template.loader import get_template
from django.urls import reverse
from django.utils.html import escape
from xhtml2pdf import pisa
from io import StringIO, BytesIO
from simpleDjangoProject.settings import EMAIL_HOST_USER
from .models import Students, Teachers, Courses, StudentSubjects, Subjects, MultiStepFormModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def ShowChatHome(request):
    return render(request,"chat_home.html")

def ShowChatPage(request,room_name,person_name):
    return render(request,"chat_screen.html",{'room_name':room_name,'person_name':person_name})
    #return HttpResponse("Chat page "+room_name+""+person_name)
