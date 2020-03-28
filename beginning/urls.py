"""beginning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from general import views as viewsbeg
from mainapp import views as viewsmain
from javascript1 import views as viewsj1
from forum import views as viewsforum
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	path('article1', viewsbeg.index, name = 'article1'),
	path('article2', viewsbeg.index2, name = 'article2'),
	path('javascript1', viewsj1.index, name = 'javascript1'),
	path('javascript2', viewsj1.index2, name = 'javascript2'),
	path('forum', viewsforum.index, name = 'forum'),
	path('', viewsmain.index, name = 'mainsh'),
	path('create/', viewsforum.create),
	path('delcode8998/', viewsforum.delete),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
