"""mysite02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import main.views as mainviews
import user.views as userviews
import guestbook.views as guestbookviews
import board.views as boardviews

urlpatterns = [
    path('', mainviews.index),

    path('user/joinform', userviews.joinform),
    path('user/join', userviews.join),
    path('user/joinsuccess', userviews.joinsuccess),
    path('user/loginform', userviews.loginform),
    path('user/login', userviews.login),
    path('user/logout', userviews.logout),
    path('user/updateform', userviews.updateform),
    path('user/update', userviews.update),

    path('guestbook/', guestbookviews.index),
    path('guestbook/add', guestbookviews.add),
    path('guestbook/deleteform', guestbookviews.deleteform),
    path('guestbook/delete', guestbookviews.delete),

    path('board/', boardviews.index),
    path('board/write', boardviews.write),
    path('board/add', boardviews.add),
    path('board/view', boardviews.view),
    path('board/updateform', boardviews.updateform),
    path('board/update', boardviews.update),
    path('board/delete', boardviews.delete),
]
