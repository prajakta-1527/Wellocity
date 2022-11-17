from .models import Product, Category, SubCategory, Manufacturer, AskADoctor, ShoppingCart, ShoppingCartItems, Wishlist, WishlistItems
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
User = get_user_model()
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,'abcd.html')
    return render(request, 'home.html')

from .models import ShoppingCart
from .models import Product
from .models import ShoppingCartItems
from django.core.exceptions import ObjectDoesNotExist

def addtocart(request,add):
    # pr=Product.objects.filter(idproduct=add)
    if request.user.is_authenticated:
        
        # ins=User.objects.get(iduser=request.user.iduser)
        cart=ShoppingCart.objects.get(user_id=request.user.iduser)
        pr=Product.objects.get(idproduct=int(add))
        if cart is not None:
            ShoppingCartItems(shopping_cart_id_cart=cart,quantity=1,product_id=int(add)).save()
            amt=int(cart.amount)
            a=int(pr.discounted_price)
            amt+=a
            cart.amount=amt
            print(amt)
            cart.save()
        
        return redirect('/prod/'+add)


    else:
        return render(request, 'home.html')
    
def prod(request,pin):
    if request.user.is_authenticated:
        content=Product.objects.get(idproduct=pin)
        cart=ShoppingCart.objects.get(user_id=request.user.iduser)
        ins=ShoppingCartItems.objects.filter(shopping_cart_id_cart=cart,product_id=pin).first()
        if ins is not None:
            flag=True
        else:
            flag=False
        wish=Wishlist.objects.filter(user_id=request.user.iduser).first()
        ins=wish
        if wish is None:
            ins=Wishlist(user_id=request.user.iduser)
            ins.save()
        item= WishlistItems.objects.filter(wishlist_idwishlist=ins,product_id=pin).first()
        if item is None:
            str="Add to Wishlist"
        else:
            str="Added to Wishlist"
        if content.stock==0:
            flag2=True
        else:
            flag2=False
        mf=content.manufacturer_idmanufacturer
        dict={'content':content,'flag':flag,'flag2':flag2,'str':str,'mf':mf}
        return render(request,'product.html',dict)
    else:
        return render(request, 'home.html')

def remove(request):
    if request.method=="GET":
        pd=request.GET['prod_id']
        prod_id=int(pd)
        print(pd)
        pr=Product.objects.get(idproduct=prod_id)
        cart=ShoppingCart.objects.get(user_id=request.user.iduser)
        item=ShoppingCartItems.objects.get(Q(product_id=prod_id) & Q(shopping_cart_id_cart=cart))
        
        prodprice=(item.quantity)*(pr.discounted_price)
        cart.amount-=prodprice
        cart.save()
        item.delete()
        data ={
            
            'amount' : cart.amount,
            
        }
        return JsonResponse(data)

def wishtocart(request):
    if request.method=="GET":
        pd=request.GET['prod_id']
        
        prod=int(pd)
        cart=ShoppingCart.objects.get(user_id=request.user.iduser)
        item=ShoppingCartItems.objects.filter(Q(product_id=prod) & Q(shopping_cart_id_cart=cart)).first()
        if item is not None:
            str="Added to Cart"
            data={
                'str':str,
            }
            return JsonResponse(data)
        add=prod
        wish=Wishlist.objects.filter(user_id=request.user.iduser).first()
        ins=wish
        
        item= WishlistItems.objects.filter(wishlist_idwishlist=ins,product_id=prod).first()
        str="Added to Cart"
        data={
            'str':str,
        }
        if item is None:
            return JsonResponse(data)
        item.delete()
        cart=ShoppingCart.objects.get(user_id=request.user.iduser)
        pr=Product.objects.get(idproduct=int(add))
        if cart is not None:
            ShoppingCartItems(shopping_cart_id_cart=cart,quantity=1,product_id=int(add)).save()
            amt=int(cart.amount)
            a=int(pr.discounted_price)
            amt+=a
            cart.amount=amt
            cart.save()

        
        return JsonResponse(data)

def removewish(request):
    if request.method=="GET":
        pd=request.GET['prod_id']
        
        prod=int(pd)
        wish=Wishlist.objects.filter(user_id=request.user.iduser).first()
        ins=wish
        
        item= WishlistItems.objects.filter(wishlist_idwishlist=ins,product_id=prod).first()
        item.delete()
        data={
            'prod':prod,
        }
        return JsonResponse(data)
        

from .models import OrderDetails
from .models import OrderItems
from datetime import datetime, date, timedelta
def buynow(request):
    if request.user.is_authenticated:
        allprods=Product.objects.all()
        cart=ShoppingCart.objects.get(user_id=request.user.iduser)
        ins=ShoppingCartItems.objects.filter(shopping_cart_id_cart=cart)
        dict=[]
        foo=[]
        dict2=[]
        dict3=[]
        reqprods=Product.objects.none()
        
        for i in ins:
            dict.append(i.product_id)
        if len(dict)!=0:
            flag=True
        else:
            flag=False
        for p in allprods:
            if p.idproduct in dict:
                if p.stock<=0:
                    item=ShoppingCartItems.objects.get(Q(product_id=p.idproduct) & Q(shopping_cart_id_cart=cart))
                    q=item.quantity
                    p=p.discounted_price
                    cart.amount-=q*p
                    item.delete()
                else:
                    foo.append(p)
                    getcartitem=ShoppingCartItems.objects.get(shopping_cart_id_cart=cart,product_id=p.idproduct)
                    var=(p.discounted_price)*(getcartitem.quantity)
                    dict3.append(var)
                    dict2.append(getcartitem.quantity)
        
        amt=cart.amount
        mylist = zip(foo, dict2,dict3)

        
    # if request.user.is_authenticated:
    #     cart=ShoppingCart.objects.get(user_id=request.user.iduser)
    #     date_1=datetime.now()
    #     result_1 = date_1 + timedelta(days=5)
    #     order=OrderDetails(user_id=request.user.iduser,amount=cart.amount,date_of_order=datetime.now(),date_of_delivery=result_1)
    #     order.save()
    #     item=ShoppingCartItems.objects.filter(shopping_cart_id_cart=cart)
    #     dict=[]
    #     for i in item:
    #         prod=Product.objects.get(idproduct=i.product_id)
    #         dict.append(prod)
    #         OrderItems(quantity=i.quantity,order_details_idorder=order,price=prod.discounted_price,product_id=prod.idproduct).save()
    #         i.delete()

    #     cart.amount=0
    #     cart.save()
    #     list=zip(item,dict)
        ins=User3.objects.get(auth_id=request.user.iduser)
        if ins.address==None or ins.address=='None' :
            flag1=False
        else:
            flag1=True
        if ins.state==None or ins.state=='None':
            flag2=False
        else:
            flag2=True
        if ins.city ==None or ins.city=='None':
            flag3=False
        else:
            flag3=True
        if ins.pincode==None or ins.pincode=='None':
            flag4=False
        else:
            flag4=True
        if ins.phone_number==None or ins.phone_number=='None':
            flag5=False
        else:
            flag5=True
        user=ins
        content={'mylist':mylist,'cart':cart,'amt':amt,'flag1':flag1,'flag2':flag2,'flag3':flag3,'flag4':flag4,'flag5':flag5,'user':user}
        # content={'list':list,}
        return render(request,'orderdetails.html',content)

def payment(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            ins=User3.objects.get(auth_id=request.user.iduser)
            if ins.address is None:
                address=request.POST['address']
                ins.address=address
                ins.save()
            
            if ins.state is None:
                state=request.POST['state']
                ins.state=state
                ins.save()
            if ins.city is None:
                city=request.POST['city']
                ins.city=city
                ins.save()
            if ins.pincode is None:
                pincode=request.POST['Pincode']
                ins.pincode=pincode
                ins.save()
            if ins.phone_number is None:
                phonenumber=request.POST['phonenumber']
                ins.phone_number=phonenumber
                ins.save()
            
            
            
            
            return render(request,'payment.html')
        else:
            return render(request,'orderdetails.html')
        
                 
            
            
            
            
            
from .models import Payment
def paydone(request):
     if request.user.is_authenticated:
        
        if request.method=="POST":
            cart=ShoppingCart.objects.get(user_id=request.user.iduser)
            date_1=datetime.now()
            result_1 = date_1 + timedelta(days=5)
            order=OrderDetails(user_id=request.user.iduser,amount=cart.amount,date_of_order=datetime.now(),date_of_delivery=result_1)
            order.save()
            item=ShoppingCartItems.objects.filter(shopping_cart_id_cart=cart)
            dict=[]
            for i in item:
                prod=Product.objects.get(idproduct=i.product_id)
                prod.stock-=i.quantity
                prod.save()
                dict.append(prod)
                OrderItems(quantity=i.quantity,order_details_idorder=order,price=prod.discounted_price,product_id=prod.idproduct).save()
                i.delete()

            cart.amount=0
            cart.save()
            # list=zip(item,dict)
            # content={'list':list,}

            otp=request.POST['otp']
            order=OrderDetails.objects.filter(user_id=request.user.iduser)
            # order_details_idorder=order[-1]
            # order1=OrderDetails.objects.latest('date_of_order')
            ord=OrderDetails.objects.filter(user_id=request.user.iduser).last()
            # ord=OrderDetails.objects.filter(idorder=order1)
            time_of_payment=datetime.now()
            type_of_payment='Cash On delivery'
            time_of_payment=datetime.now()
            pay=Payment(order_details_idorder=ord,status="completed",type_of_payment=type_of_payment,time_of_payment=time_of_payment)
            pay.save()
            content={'pay':pay,'ord':ord}
            return render(request,'orderstatus.html',content)

            


import itertools
def showcart(request):
    if request.user.is_authenticated:
        allprods=Product.objects.all()
        cart=ShoppingCart.objects.get(user_id=request.user.iduser)
        ins=ShoppingCartItems.objects.filter(shopping_cart_id_cart=cart)
        
        dict=[]
        foo=[]
        dict2=[]
        dict3=[]
        reqprods=Product.objects.none()
        
        for i in ins:
            dict.append(i.product_id)
        if len(dict)!=0:
            flag=True
        else:
            flag=False
        for p in allprods:
            if p.idproduct in dict:
                if p.stock<=0:
                    item=ShoppingCartItems.objects.get(Q(product_id=p.idproduct) & Q(shopping_cart_id_cart=cart))
                    q=item.quantity
                    p=p.discounted_price
                    cart.amount-=q*p
                    item.delete()
                else:
                    foo.append(p)

                    getcartitem=ShoppingCartItems.objects.get(shopping_cart_id_cart=cart,product_id=p.idproduct)
                    var=(p.discounted_price)*(getcartitem.quantity)
                    dict3.append(var)
                    dict2.append(getcartitem.quantity)
        
        amt=cart.amount
        mylist = zip(foo, dict2,dict3)

        content={'mylist':mylist,'cart':cart,'amt':amt,'flag':flag}
        return render(request,'cart.html',content)
    else:
        return render(request, 'home.html')

def pluscart(request):
    if request.method=="GET":
        pd=request.GET['prod_id']
        prod_id=int(pd)
        print(pd)
        pr=Product.objects.get(idproduct=prod_id)
        cart=ShoppingCart.objects.get(user_id=request.user.iduser)
        item=ShoppingCartItems.objects.get(Q(product_id=prod_id) & Q(shopping_cart_id_cart=cart))
        if not (item.quantity+1>pr.stock):

            item.quantity+=1
            item.save()
            cart.amount+=pr.discounted_price
            cart.save()
            prodprice=(item.quantity)*(pr.discounted_price)
        data ={
            'quantity':item.quantity,
            'amount' : cart.amount,
            'prodprice' : prodprice
        }
        
        return JsonResponse(data)

def minuscart(request):
    if request.method=="GET":
        pd=request.GET['prod_id']
        prod_id=int(pd)
        print(pd)
        pr=Product.objects.get(idproduct=prod_id)
        cart=ShoppingCart.objects.get(user_id=request.user.iduser)
        item=ShoppingCartItems.objects.get(Q(product_id=prod_id) & Q(shopping_cart_id_cart=cart))
        if item.quantity!=1:
            
            item.quantity-=1
            item.save()
            cart.amount-=pr.discounted_price
            cart.save()
        prodprice=(item.quantity)*(pr.discounted_price)
        data ={
            'quantity':item.quantity,
            'amount' : cart.amount,
            'prodprice' : prodprice
        }
        return JsonResponse(data)


def inhome(request):
    # print("knknk")
    # print(request.user.user_name)
    if request.user.is_authenticated:
        return render(request, 'abcd.html')
    else:
        return render(request, 'home.html')

from .models import User3
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        password = request.POST['password']
        print(email, user_name)
        myuser = User.objects.create_user(
            email, user_name, password, first_name)
        myuser.save()
        
        
        messages.success(request, 'Your account has been succesfully created')
        login(request, myuser)
        User3(user_name=user_name,first_name=first_name,auth_id=request.user.iduser).save()
        ShoppingCart(user_id=request.user.iduser,amount=0).save()
        return render(request, 'abcd.html')

    else:
        return render(request, 'signup.html')


def handlelogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'successfully logged in')
            return redirect('inhome')
        else:
            return redirect('handlelogin')
    return render(request, 'handlelogin.html')


def handlelogout(request):
    if (request.user.is_authenticated):
        # print("yes")
        logout(request)
        return render(request, 'home.html')
    else:
        # print("anony")
        return render(request, 'home.html')


# def well(request):
#     return render(request,'abcd.html')
# Create your views here.

def shop(request, slug):
    if request.user.is_authenticated:

        category_list = Category.objects.all()
        # sub_category_list = SubCategory.objects.all()
        product_list = Product.objects.all()
        req = SubCategory.objects.filter(category_idcategory=slug)
        allProds = []
        for i in req:
            allProds.append(i.id_sub_category)
    # print(allProds)
    # print("jhj")
    # cats = req.values('id_sub_category')
    # for cat in cats:
    #     prod=Product.objects.filter(sub_category_id_sub_category=cat)
    #     allProds.append([prod])
    #req2 = Product.objects.filter( sub_category_id_sub_category = req3 )
        context = {'shop': product_list, 'shop2': req,
                   'shop3': category_list, 'allProds': allProds}
        return render(request, 'shop.html', context)
    else:
        return render(request, 'home.html')


# id_sub_category
def shop2(request, hemlo):
    if request.user.is_authenticated:
        sub_category_list = SubCategory.objects.all()
        product_list = Product.objects.all()
        req = Product.objects.filter(sub_category_id_sub_category=hemlo)
        req2 = SubCategory.objects.filter(id_sub_category=hemlo)
        slug = req2[0].category_idcategory
        category_list = Category.objects.all()
    # sub_category_list = SubCategory.objects.all()
        product_list = Product.objects.all()
        req6 = SubCategory.objects.filter(category_idcategory=slug)
        allProds = []
        for i in req6:
            allProds.append(i.id_sub_category)
        context = {'cat': sub_category_list, 'prod': req, 'req': req,
                   'req6': req6, 'req2': req2, 'cate': category_list, 'allProds': allProds}
        return render(request, 'shop2.html', context)
    else:
        return render(request, 'home.html')

from .models import HealthArticles



import math
def blog(request):
    page=request.GET.get('page')
    if page==None :
        page=1
    else:
        page=int(page)
    no_of_posts=3
    
    # 0 1 2 ..1
    # 3 4 5 ..2
    # 6
    
    
    if page==1 :
        prev=None
    else:
        prev=page-1
    if page>=math.ceil((HealthArticles.objects.count())/no_of_posts ):
        next=None
    else:
        next=page+1
    allblogs=HealthArticles.objects.all()[(page-1)*no_of_posts : no_of_posts*page]
    context={'allblogs' :allblogs, 'prev':prev,'next':next}

    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    req=HealthArticles.objects.filter(slug=slug).first()
    context={'req': req}
    return render(request,'blog/blogpost.html',context)

def contact(request):
    return render(request,'contact.html')

def yourprofile(request):
    if request.user.is_authenticated:
        i=User3.objects.get(auth_id=request.user.iduser)
        
        print(i.profile_image)
        help={'i':i}
        return render(request,'yourprofile.html',help)

def medicines(request):
    if request.user.is_authenticated:
        abc=SubCategory.objects.get(sub_category='Medicine')
        ham =Product.objects.filter(sub_category_id_sub_category=abc)
    helu ={'ham':ham}
    return render(request,'medicines.html',helu)

def search(request):
   query = request.GET['query']
   Pro = Product.objects.filter(product_name__icontains=query)
   params={'Pro':Pro}
   return render(request,'search.html',params)

def searchdisplay(request):
    query2 = request.GET['query2']
    Pro2 = Product.objects.filter(product_name__icontains=query2)
    params2 ={'Pro2': Pro2}
    return render(request,'searchdisplay.html',params2)

def editprofile(request):
    
    if request.user.is_authenticated:
        ins=User3.objects.get(auth_id=request.user.iduser)
        content={'ins':ins}
        
        
        if request.method=="POST" or request.FILES:
            
            user_name=request.POST['user_name']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            address=request.POST['address']
            pincode=request.POST['pincode']
            state=request.POST['state']
            city=request.POST['city']
            phone_number=request.POST['phone_number']
            if request.FILES:
                profile_image=request.FILES['profile_image']
                ins.profile_image=profile_image
                ins.save()
            if pincode!='':
                ins.pincode=pincode
                ins.save()
            
            ins.user_name=user_name
            ins.save()
            ins.first_name=first_name
            ins.save()
            ins.last_name=last_name
            ins.save()
            ins.address=address
            ins.save()
            
            ins.state=state
            ins.save()
            ins.city=city
            ins.save()
        
            ins.phone_number=phone_number
            ins.save()
            
            return render(request,'abcd.html')
        else:
            return render(request,'editprofile.html',content)

from .models import Wishlist
from .models import WishlistItems

def wishlist(request):

    if request.method=="GET":
        pr=request.GET['prod']
        prod=int(pr)
        wish=Wishlist.objects.filter(user_id=request.user.iduser).first()
        ins=wish
        if wish is None:
            ins=Wishlist(user_id=request.user.iduser)
            ins.save()
        item= WishlistItems.objects.filter(wishlist_idwishlist=ins,product_id=prod).first()
        # WishlistItems(wishlist_idwishlist=ins,product_id=prod).save()
        if item is None:
            req=WishlistItems(wishlist_idwishlist=ins,product_id=prod).save()
            str="Added to Wishlist"
        else:
            item.delete()
            str="Add to Wishlist"
        data= {
            'str':str,
        }
        return JsonResponse(data)


def  viewwishlist(request):
        wish=Wishlist.objects.filter(user_id=request.user.iduser).first()
        ins=wish
        if wish is None:
            ins=Wishlist(user_id=request.user.iduser)
            ins.save()
        list= WishlistItems.objects.filter(wishlist_idwishlist=ins)
        prodlist=Product.objects.all()
        dict=[]
        for i in list :
            item=Product.objects.filter(idproduct=i.product_id).first()
            dict.append(item)
            dtr="Add to cart"
        content={'dict':dict,'list':list,'str':str}
        return render(request,'viewwishlist.html',content)



