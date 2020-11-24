from django.shortcuts import render
from .models import order

def home(request):
   
        
    return render(request, 'comingsoon/home.html')

def milk(request):

    if request.method == 'POST':
                

                print('hello post')
                
                return render(request, 'comingsoon/milk_groupshop.html')  

    else:
                print('hello get')
                return render(request,'comingsoon/milk.html')
    
        
def milk_gp(request):
    
        
    return render(request, 'comingsoon/milk_groupshop.html')

def eggs_gp(request):
    
        
    return render(request, 'comingsoon/eggs_groupshop.html')

def yoghurt_gp(request):
   
        
    return render(request, 'comingsoon/yoghurt_groupshop.html')

def bread_gp(request):
    
        
    return render(request, 'comingsoon/bread_groupshop.html')

def eggs(request):
    
    return render(request, 'comingsoon/eggs.html')

def bread(request):
    
        
    return render(request, 'comingsoon/bread.html')

def yoghurt(request):
   
    return render(request, 'comingsoon/yoghurt.html')

def potatoes(request):
    
        
    return render(request, 'comingsoon/potatoes.html')

def delivery_milk(request):
    if request.method == 'POST':
                
                Order=order()
                print(request.POST.get('name'))
                print(request.POST.get('item'))
                Order.name= request.POST.get('name')
                Order.number= request.POST.get('number')
                Order.address= request.POST.get('address')
                Order.city= request.POST.get('city')
                Order.province= request.POST.get('province')
                Order.zipcode= request.POST.get('zipcode')
                Order.item = request.POST.get('item')
                Order.quantity = request.POST.get('quantity')
                Order.method = request.POST.get('method')
                Order.save()


                
                return render(request, 'comingsoon/confirm.html')  

    else:
                return render(request,'comingsoon/delivery_milk.html')

def milk_alone(request):
    if request.method == 'POST':
                
                Order=order()
                print(request.POST.get('name'))
                print(request.POST.get('item'))
                Order.name= request.POST.get('name')
                Order.number= request.POST.get('number')
                Order.address= request.POST.get('address')
                Order.city= request.POST.get('city')
                Order.province= request.POST.get('province')
                Order.zipcode= request.POST.get('zipcode')
                Order.item = request.POST.get('item')
                Order.quantity = request.POST.get('quantity')
                Order.method = request.POST.get('method')
                Order.save()


                
                return render(request, 'comingsoon/confirm.html')    

    else:
                return render(request,'comingsoon/milk_alone.html')

def delivery_yoghurt(request):
    if request.method == 'POST':
                
                Order=order()
                print(request.POST.get('name'))
                Order.name= request.POST.get('name')
                Order.number= request.POST.get('number')
                Order.address= request.POST.get('address')
                Order.city= request.POST.get('city')
                Order.province= request.POST.get('province')
                Order.zipcode= request.POST.get('zipcode')
                Order.item = request.POST.get('item')
                Order.quantity = request.POST.get('quantity')
                Order.method = request.POST.get('method')
                Order.save()


                
                return render(request, 'comingsoon/confirm.html')    

    else:
                return render(request,'comingsoon/delivery_yoghurt.html')

def yoghurt_alone(request):
    if request.method == 'POST':
                
                Order=order()
                print(request.POST.get('name'))
                Order.name= request.POST.get('name')
                Order.number= request.POST.get('number')
                Order.address= request.POST.get('address')
                Order.city= request.POST.get('city')
                Order.province= request.POST.get('province')
                Order.zipcode= request.POST.get('zipcode')
                Order.item = request.POST.get('item')
                Order.quantity = request.POST.get('quantity')
                Order.method = request.POST.get('method')
                Order.save()


                
                return render(request, 'comingsoon/confirm.html')    

    else:
                return render(request,'comingsoon/yoghurt_alone.html')

def delivery_bread(request):
    if request.method == 'POST':
                
                Order=order()
                print(request.POST.get('name'))
                Order.name= request.POST.get('name')
                Order.number= request.POST.get('number')
                Order.address= request.POST.get('address')
                Order.city= request.POST.get('city')
                Order.province= request.POST.get('province')
                Order.zipcode= request.POST.get('zipcode')
                Order.item = request.POST.get('item')
                Order.quantity = request.POST.get('quantity')
                Order.method = request.POST.get('method')
                Order.save()


                
                return render(request, 'comingsoon/confirm.html')    

    else:
                return render(request,'comingsoon/delivery_bread.html')

def bread_alone(request):
    if request.method == 'POST':
                
                Order=order()
                print(request.POST.get('name'))
                Order.name= request.POST.get('name')
                Order.number= request.POST.get('number')
                Order.address= request.POST.get('address')
                Order.city= request.POST.get('city')
                Order.province= request.POST.get('province')
                Order.zipcode= request.POST.get('zipcode')
                Order.item = request.POST.get('item')
                Order.quantity = request.POST.get('quantity')
                Order.method = request.POST.get('method')
                Order.save()


                
                return render(request, 'comingsoon/confirm.html')    

    else:
                return render(request,'comingsoon/bread_alone.html')

def delivery_eggs(request):
    if request.method == 'POST':
                
                Order=order()
                print(request.POST.get('name'))
                Order.name= request.POST.get('name')
                Order.number= request.POST.get('number')
                Order.address= request.POST.get('address')
                Order.city= request.POST.get('city')
                Order.province= request.POST.get('province')
                Order.zipcode= request.POST.get('zipcode')
                Order.item = request.POST.get('item')
                Order.quantity = request.POST.get('quantity')
                Order.method = request.POST.get('method')
                Order.save()


                
                return render(request, 'comingsoon/confirm.html')   

    else:
                return render(request,'comingsoon/delivery_eggs.html')

def eggs_alone(request):
    if request.method == 'POST':
                
                Order=order()
                print(request.POST.get('name'))
                Order.name= request.POST.get('name')
                Order.number= request.POST.get('number')
                Order.address= request.POST.get('address')
                Order.city= request.POST.get('city')
                Order.province= request.POST.get('province')
                Order.zipcode= request.POST.get('zipcode')
                Order.item = request.POST.get('item')
                Order.quantity = request.POST.get('quantity')
                Order.method = request.POST.get('method')
                Order.save()


                
                return render(request, 'comingsoon/confirm.html')   

    else:
                return render(request,'comingsoon/eggs_alone.html')



# def home(request):
#     context = {}
#     template = 'comingsoon/home.html'
#     return render(request, template, context)
