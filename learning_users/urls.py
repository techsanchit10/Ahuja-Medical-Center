"""learning_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.base,name='index'),
    url(r'^admin/', admin.site.urls),

    url(r'^special/',views.special,name='special'),
    url(r'^basic_app/',include('basic_app.urls')),
    url(r'^registration/',views.registration,name='registration'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^epr_app/',include('epr_app.urls')),
    url(r'^appointment/',include('appointment.urls')),
    url(r'^doctor-login/',include('doctors_app.urls')),
    url(r'^orders/',include('orders.urls')),
    url(r'^payment/',include('payment.urls')),
    url(r'^test-app/',include('testapp.urls')),
    url(r'^cart/',include('cart.urls')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),



]
