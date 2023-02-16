"""products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from application2 import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main_page/', views.Test_case1),
    url(r'^registration/', views.Test_case2,name="web1"),
    url(r'^loginform/', views.Test_case3,name="web2"),
    url(r'^information/', views.Test_case4,name="web3"),
    url(r'^rgister_info/', views.Test_case5,name="web4"),
    url(r'^get_information/', views.Test_case6,name="web5"),
    url(r'^registration1/', views.Test_case1,name="web6"),
    url(r'^loginform1/', views.Test_case1,name="web7"),
    url(r'^information1/', views.Test_case1,name="web8"),
    url(r'^register_info1/', views.Test_case1,name="web9"),
    url(r'^get_information1/', views.Test_case1,name="web10"),
    
    
    
]
