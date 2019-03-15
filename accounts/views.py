from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
# Create your views here.
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from accounts.models import AudioFile, Button, Pad

from .forms import UserLoginForm, UserRegisterForm, AudioFileForm, SettingForm, PadForm


def login_view(request):
    print(request.user.is_authenticated())
    title = 'Login'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'userform.html', {'form': form, 'title': title})


def register_view(request):
    title = 'Registrieren'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        get_user_model = form.save(commit=False)
        password = form.cleaned_data.get('password')
        get_user_model.set_password(password)
        get_user_model.save()

        new_user = authenticate(username=get_user_model.username, password=password)
        login(request, new_user)
    return render(request, 'userform.html', {'form': form, 'title': title})


def logout_view(request):
    logout(request)
    return redirect('home')



def model_form_upload(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AudioFileForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


def view_home(request):
    form_login = UserLoginForm(request.POST or None)
    form_register = UserRegisterForm(request.POST or None)
    form_menu = SettingForm(None)
    form_upload = AudioFileForm(request.POST or None)
    form_pad = PadForm(None)
    audio = None
    pad = None
    form_button = SettingForm(None, request.POST or None)
    title = "audioQuery [PreAlpha]"
    if request.user.is_authenticated():
        form_pad = PadForm(request.user, request.POST or None)
        audio = AudioFile.objects.filter(user=request.user)
        pad = Pad.objects.filter(user=request.user)
        form_button = SettingForm(request.user, request.POST or None)
        form_upload = AudioFileForm()
    if request.method == 'POST':


        form_upload = AudioFileForm(request.POST or None, request.FILES)

        if form_upload.is_valid():
            file = AudioFile()
            if request.method == 'POST':
                userids = AudioFile.objects.values_list('user_id', flat=True)
                uploadcount = 0
                for i in userids:
                    if i == request.user.id:
                        uploadcount += 1
                if request.method == 'POST':
                    if uploadcount < 20:
                        file = form_upload.save(commit=False)
                        file.user = request.user
                        file.save()
                    else:
                        file = form_upload.save(commit=False)
            return redirect('/home/')

        if form_button.is_valid():
            btn = Button(request.user)
            if request.method == 'POST':
                btn = form_button.save(commit=False)
                btn.user = request.user
                btn.save()
                return redirect('/home/')
        if form_pad.is_valid():
            pad = Pad()
            if request.method == 'POST':
                pad = form_pad.save(commit=False)
                pad.user = request.user

                pad.save()
                return redirect('/home/')
        if form_login.is_valid():
            username = form_login.cleaned_data.get('username')
            password = form_login.cleaned_data.get('password')
            login(request, authenticate(username=username, password=password))
            # print(request.user.is_authenticated())
            return redirect('/home/')
        if form_register.is_valid():
            get_user_model = form_register.save(commit=False)
            password = form_register.cleaned_data.get('password')
            get_user_model.set_password(password)
            get_user_model.save()
            new_user = authenticate(username=get_user_model.username, password=password)
            login(request, new_user)




    return render(request, 'home.html', {'page_title': title, 'form_login': form_login, 'form_register': form_register,
                                         'form_upload': form_upload,'form_button' : form_button,'form_pad' : form_pad,
                                         'user_active': request.user.is_authenticated(),
                                         'username': request.user.username, 'data': audio, 'pad': pad})

def getButtons(request):
    buttons = Button.objects.all()
    return render(request, 'viewmodeldata.html', {
        'data': buttons
    })


def getAudio(request):
    audio = AudioFile.objects.filter(user=request.user)
    return render(request, 'viewmodeldata.html', {
        'data': audio
    })


def getPad(request):
    pad = Pad.objects.all()
    return render(request, 'viewmodeldata.html', {
        'data': pad
    })

def getPadData(request):
    pad = Pad.objects.objects.filter(buttonlist)
    return render(request, 'viewmodeldata.html', {
        'data': pad
    })

def addAudio(request):
    audio = AudioFile()
    page_title = 'Audio hinzufügen'
    if request.method == 'POST':
        form = AudioFileForm(request.POST, instance=audio)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            pass

    else:
        form = AudioFileForm(instance=audio)

    return render(request, 'userform.html', {'page_title': page_title, 'form': form})

def editPad(request):
    pad = None
    if request.user.is_authenticated():
        pad = Pad.objects.filter(user=request.user)

    return render(request, 'editPad.html', {'page_title': 'Deine Pads', 'pad': pad, 'usercur':request.user})

def editButton(request,pk=None,user=None):
    btn = Button.objects.filter(pk=pk)
    page_title = 'Button editieren'

    if request.method=='POST':
        form=SettingForm(request.user,request.POST,instance=btn[0])
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('edit_pad'))
        else:
            pass
    else:
        form = SettingForm(request.user,instance=btn[0])

    return render(request, 'editButton.html', {
        'page_title': 'Button editieren',
        'form': form,
    })

def delButton(request,pk=None,user=None):
    btn = Button.objects.get(pk=pk)
    btn.delete()
    return HttpResponseRedirect(reverse('home'))

def delPad(request,pk=None,user=None):
    pad = Pad.objects.get(pk=pk)
    pad.delete()
    return HttpResponseRedirect(reverse('home'))

def pad_details(request, pk=None):
    if pk==None:
        pad = Pad()
        page_title ='Pad hinzufügen'
    else:

        pad = get_object_or_404(Pad, pk=pk)
        page_title = 'Pad editieren'

    if request.method =='POST':
        form = PadForm(request.user, request.POST, instance=pad)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            pass
    else:
        form = PadForm(request.user, instance=pad)

    return render(request, 'standard_form.html', {'page_title':page_title, 'form':form})

def delAudio(request,pk=None):
    audio = AudioFile.objects.get(pk=pk)
    audio.delete()
    return HttpResponseRedirect(reverse('home'))