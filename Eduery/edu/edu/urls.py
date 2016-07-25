"""edu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include, patterns
from django.contrib import admin

urlpatterns = [
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'d:/VagrantPath/fedora24-python35-master/Eduery/edu/static'}), 
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'MOOC.register.homepage'), #主页（学生和未登录）
    url(r'^register/', 'MOOC.register.register'), #选择注册身份
    url(r'^registerstudent/', 'MOOC.register.registerstudent'), #学生用户注册
    url(r'^registerteacher/', 'MOOC.register.registerteacher'), #教师用户注册
    url(r'^registerschool/', 'MOOC.register.registerschool'), #学校用户注册
    #四种不同种用户的登陆界面
    url(r'^login/', 'MOOC.login.login'),
    url(r'^logout/', 'MOOC.logout.logout'), #登出
    url(r'^changepassword/', 'MOOC.changepassword.changepassword'), #修改密码
    url(r'^changeselfinformation/', 'MOOC.changeselfinformation.changeselfinformation'), #修改个人信息
    url(r'^video/', 'MOOC.notes.note_list'),
]
