from django.shortcuts import render
from django.contrib.auth.models import User,auth
from . models import Employee,Sale
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
   
  
    return render(request,'index.html')

def login_check(request):
    if request.method=='POST':
        username= request.POST['your_name']
        password= request.POST['password']
        user = auth.authenticate(password=password,username=username)
        if user is not None:
           auth.login(request,user)
           if user.groups.filter(name='Director').exists():
               return render (request,'homepage.html', {'username':username})
           else:
               return render (request,'homepage_staff.html', {'username':username})
    
           
        else:
           return render(request,'Login.html',{'msg':'Incorrect Username/Password. Try Again!'})
    else:
         return render(request,'Login.html')
def Logout(request):
    logout(request)
    
    return redirect('index')  
def is_team(user):
    return user.groups.filter(name='Team').exists()
def is_manager(user):
    return user.groups.filter(name='Manager').exists()
def is_north(user):
    return user.groups.filter(name='North-India').exists()
def is_south(user):
    return user.groups.filter(name='South-India').exists()
@login_required
def sales_mgmt(request):
     #user=request.user
     
     if is_team(request.user):
          
          #username=request.user.username
          #emp_dept=Employee.objects.filter(user_name=username).values('department')
          if is_north(request.user):
              sales=Sale.objects.filter(Q(Emp_role='Team')&Q(Emp_department='North-India')).values()
              user_name=request.user.username
              print(user_name)
              
              return render(request,'sales_team.html',{'sale':sales,'username':user_name})
          else:
              sales=Sale.objects.filter(Q(Emp_role='Team')&Q(Emp_department='South-India')).values()
              user_name=request.user.username
              print(user_name)
              return render(request,'sales_team.html',{'sale':sales,'username':user_name})
     elif is_manager(request.user):
         print("iko")
         sales=Sale.objects.filter(Q(Emp_role='Team')|Q(Emp_role='Manager')).values()
         if is_north(request.user):
              print("jan")
              emp_dept="North-India"
              return render(request,'sales.html',{'sale':sales,'emp_dept':emp_dept})
         else:
              print("bye")
              emp_dept="South-India"
              return render(request,'sales.html',{'sale':sales,'emp_dept':emp_dept})

         

     else:
         sales=Sale.objects.all().values()
         return render(request,'sales_admin.html',{'sale':sales})
@login_required   
def emp_mgmt(request):
    emp=Employee.objects.all().values()
  
    role=User.objects.filter(groups__name='North-India')
    for user in emp:
         print("Role:",user['role'])
         #print("Dept:",emp.dept)
         #print("Name:",emp.username)

    print("gerat sucess")
   
    
    return render(request,'emp.html',{'users':emp})
@login_required
def sale_view(request,id):
    sale_data=Sale.objects.filter(id=id).values()
    
    return render(request,'view_sales.html',{'sale':sale_data})
@login_required
def sale_edit(request,id):
    if request.method=='POST':
         
         sale_data=Sale.objects.get(id=id)
        
         sale_data.business_partner=request.POST['business_partner']
         sale_data.product_name=request.POST['product_name']
         sale_data.order_quantity=request.POST['order_quantity']
         order_quantity=request.POST['order_quantity']
         price=request.POST['price']
         sale_data.price=request.POST['price']
         sale_data.Total_price=int(order_quantity)*int(price)
         sale_data.country=request.POST['country']
         sale_data.Phone_number=request.POST['Phone_number']
         sale_data.Email_Id=request.POST['Email_Id']
         sale_data.save()
         sales=Sale.objects.all().values()
         
  
        
         return render(request,'sales.html',{'sale':sales})


    else:
         sale_data=Sale.objects.filter(id=id).values()
         return render(request,'edit_sales.html',{'sale':sale_data})
@login_required
def Sales_deletedata(request,id):
    sale_data=Sale.objects.get(id=id)
    sale_data.delete()
    sales=Sale.objects.all().values()
    return render(request,'sales.html',{'sale':sales})
@login_required
def New_Sales(request):
    if request.method=="POST":
         username=request.user.username
         Emp_Id=Employee.objects.get(user_name=username)
         emp=Employee.objects.filter(user_name=username).values()
         for user in emp:
             Emp_name=user['user_name']
             Emp_role=user['role']
             Emp_dept=user['department']
             print("Role:",user['role'])
         business_partner=request.POST['business_partner']
         product_name=request.POST['product_name']
         order_quantity=request.POST['order_quantity']
         price=request.POST['price']
         Total_price=int(order_quantity)*int(price)
         country=request.POST['country']
         Phone_number=request.POST['Phone_number']
         Email_Id=request.POST['Email_Id']
         sale=Sale.objects.create(Emp_Id=Emp_Id,Emp_name=Emp_name,Emp_role=Emp_role,Emp_department=Emp_dept,product_name=product_name,business_partner=business_partner,order_quantity=order_quantity,price=price,Total_price=Total_price,Country=country,Phone_number=Phone_number,Email_Id=Email_Id)   
         sale.save()
         sales=Sale.objects.all().values()
         
  
         return sales_mgmt(request)
         #return render(request,'sales.html',{'sale':sales})
        
       
    else:
         return render(request,'order.html')
def register(request):
     if request.method =='POST':
       username=request.POST['username']
      
       psw=request.POST['psw']
       psw_repeat=request.POST['psw-repeat']
       role=request.POST['role']
       print(role)
       dept=request.POST['dept']
       print(dept)
       username_check=User.objects.filter(username = username).exists()
       
       if psw==psw_repeat:
           psw_check=False
       else:
           psw_check=True
     
       if username_check and psw_check:
           messages.info(request,"Password Doesn't match!")
           messages.info(request,'Username Taken!')
           
           return render(request,'Register.html')
       elif username_check :
           messages.info(request,'Username Taken!')
           
           return render(request,'Register.html')
       elif username_check and psw_check:
           messages.info(request,"Password Doesn't match!")
           messages.info(request,'Username Taken!')
           return render(request,'Register.html')
       elif psw_check:
           messages.info(request,"Password Doesn't match!")
           messages.info(request,'E-mail Taken!')
           return render(request,'Register.html')
      
       else:
           user=User.objects.create_user(username=username,password=psw)
           my_group = Group.objects.get(name=role) 
           my_group.user_set.add(user)
           my_group_dept = Group.objects.get(name=dept) 
           my_group_dept.user_set.add(user)
           user1=user.save()
           user2=User.objects.get(username=username)
           print(user2)
           print("sucess")
           emp=Employee.objects.create(user=user2,user_name=username,department=dept,role=role)
           print("true")
           emp.save()
           
           
           
           
         
           return render (request,'register.html', {'s_msg':'Account Successfully Created'})
           
    
          
       
     else:
          return render(request,'register.html') 
          
    
   