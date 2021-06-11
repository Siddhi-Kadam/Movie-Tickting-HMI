"""movieTickting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from employee import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.login, name='Employee Login Page'),
    path('logging', views.logging, name='Employee Logging'),
    path('logout', views.logout, name='Employee LogOut'),

    path('empDashboard', views.empDashboard, name='Employee Dashboard'),
    path('mainSlideTable', views.mainSlideTable, name='Main SlideBar Table'),
    path('mainSlideAdd', views.mainSlideAdd, name='Add Main SlideBar Entry'),
    path('mainSlideAdded', views.mainSlideAdded, name='Added Main SlideBar Entry'),
    path('mainSlideDelete/<int:id>', views.mainSlideDelete, name='Delete Main SlideBar Entry'),
    path('mainSlideEdit/<int:id>', views.mainSlideEdit, name='Edit Main SlideBar Entry'),
    path('mainSlideEdited', views.mainSlideEdited, name='Edited Main SlideBar Entry'),

    path('newReleaseTable', views.newReleaseTable, name='New Release Table'),
    path('newReleaseAdd', views.newReleaseAdd, name='Add New Release Entry'),
    path('newReleaseAdded', views.newReleaseAdded, name='Added New Release Entry'),
    path('newReleaseDelete/<int:id>', views.newReleaseDelete, name='Delete New Release Entry'),
    path('newReleaseEdit/<int:id>', views.newReleaseEdit, name='Edit New Release Entry'),
    path('newReleaseEdited', views.newReleaseEdited, name='Edited New Release Entry'),

    path('customerPaymentTable', views.customerPaymentTable, name='Customer Payment Table'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


