from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
     path('Login',views.login_check,name='Login'),
      path('sales_mgmt',views.sales_mgmt,name='sales_mgmt'),
       path('New_Sales',views.New_Sales,name='New_Sales'),
       #path('Sales_editdata',views.Sales_editdata,name='Sales_editdata'),
        path('Sales_deletedata/<int:id>',views.Sales_deletedata,name='Sales_deletedata'),
       path('emp_mgmt',views.emp_mgmt,name='emp_mgmt'),
         path('Register',views.register,name='Register'),
         path('View_Sales/<int:id>',views.sale_view,name='View_Sales'),
         path('Edit_Sales/<int:id>',views.sale_edit,name='Edit_Sales'),
          path('Logout',views.Logout,name='Logout'),
]
