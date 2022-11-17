from django.contrib import admin
from django.urls import path,include
from noice import views
urlpatterns = [
   path('', views.home, name='home'),
   path('signup', views.signup, name='signup'),
   path('handlelogin', views.handlelogin, name='handlelogin'),
   path('handlelogout', views.handlelogout, name='handlelogout'),
   path('inhome', views.inhome, name='inhome'),
   path('shop/<str:slug>',views.shop,name='shop'),
   path('shop2/<str:hemlo>',views.shop2 ,name='shop2'),
   path('prod/<str:pin>',views.prod ,name='prod'),
   path('addtocart/<str:add>',views.addtocart ,name='addtocart'),
   path('showcart',views.showcart ,name='showcart'),
   path('pluscart',views.pluscart ,name='pluscart'),
   path('minuscart',views.minuscart ,name='minuscart'),
   path('remove',views.remove ,name='remove'),
   path('removewish',views.removewish ,name='removewish'),
   path('wishtocart',views.wishtocart ,name='wishtocart'),
   path('buynow',views.buynow ,name='buynow'),
   path('payment',views.payment ,name='payment'),
   path('paydone',views.paydone ,name='paydone'),
   path('blog',views.blog,name='blog'),
   path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
   path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
   path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('yourprofile',views.yourprofile ,name='yourprofile'),
   path('contact',views.contact ,name='contact'),
   path('editprofile',views.editprofile ,name='editprofile'),
   path('viewwishlist',views.viewwishlist ,name='viewwishlist'),
   path('wishlist',views.wishlist ,name='wishlist'),
   path('medicines',views.medicines ,name='medicines'),
   path('search',views.search ,name='search'),
   path('searchdisplay',views.searchdisplay ,name='searchdisplay'),
]

# urlpatterns = [
#     path('', views.well, name='well'),
#     path('shop/<str:slug>',views.shop,name='shop'),
#     path('shop2/<str:hemlo>',views.shop2 ,name='shop2'),
# ]