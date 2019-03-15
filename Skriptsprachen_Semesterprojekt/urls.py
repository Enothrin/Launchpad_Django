import os
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from accounts.views import login_view, delPad,delAudio, logout_view,pad_details ,register_view, model_form_upload, view_home, getAudio, getButtons, getPad,getPadData,editPad,editButton,delButton
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
    url(r'^o/', model_form_upload,name='upload'),
    url(r'^list_audio/', getAudio, name='list_audio'),
    url(r'^list_button/', getButtons, name='list_but'),
    url(r'^list_pad/', getPad, name='list_pad'),
    url(r'^list_paddata/',  getPadData, name='data'),
    url(r'^add_Audio/', getPad, name='list_pad'),
    url(r'^edit_pad/', editPad, name='edit_pad'),
    url(r'^edit_button/(?P<pk>.*)/(?P<user>.*)/$', editButton, name='edit_button'),
    url(r'^delete_button/(?P<pk>.*)/(?P<user>.*)/$', delButton, name='delete_button'),
    url(r'^delete_pad/(?P<pk>.*)/$', delPad, name='delPad'),
    url(r'^delete_audio/(?P<pk>.*)/$', delAudio, name='delAudio'),
    url(r'^pad/(?P<pk>[0-9]+)?/$', pad_details, name='pad'),
    url(r'$', view_home, name='home'),
]
#os.path.join((BASE_DIR), "static_cdn"
if settings.DEBUG:
    urlpatterns += static('/user_audio/', document_root=os.path.join((settings.BASE_DIR), "user_audio"))
