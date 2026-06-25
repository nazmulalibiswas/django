from django.urls import path
from new_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

  path ('',student_info_view, name='student_info_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)