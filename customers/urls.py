from django.urls import path
from . import views

urlpatterns=[path('add',views.addCustomer,name='addClient'),
             path('logout',views.logout,name='logout'),
             path('dashboard',views.dashboard,name='dashboard'),
             path('modify/<int:cust_id>',views.modifyCustomer,name='modifyClient'),
             path('policy/add/<int:cust_id>',views.addPolicy,name='addPolicy'),
             path('policy/add/',views.addPolicy,name='addPolicy'),
             path('policy/show/<int:cust_id>',views.showPolicies,name='showPolicies'),
             path('policy/delete/<int:policy_id>',views.deletePolicy,name='deletePolicy')
             ]