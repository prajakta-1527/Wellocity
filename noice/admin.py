from django.contrib import admin
from noice.models import User
from django.contrib import admin
from .models import Manufacturer
from .models import AskADoctor
from .models import Doctor
from .models import Faq
from .models import HealthArticles
from .models import Inventory
from .models import ShoppingCartItems
from .models import OrderDetails
from .models import Payment
from .models import Product
from .models import Rating
from .models import OrderItems
from .models import Reviews
from .models import ShoppingCart
from .models import SubCategory

from .models import Wishlist
from .models import WishlistItems
from .models import User3
from .models import Category
# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(OrderDetails)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(WishlistItems)
admin.site.register(AskADoctor)
admin.site.register(Doctor)
admin.site.register(ShoppingCartItems)
admin.site.register(Faq)
admin.site.register(HealthArticles)
admin.site.register(Rating)
admin.site.register(Inventory)
admin.site.register(OrderItems)
admin.site.register(Reviews)
admin.site.register(ShoppingCart)
admin.site.register(SubCategory)

admin.site.register(Wishlist)
admin.site.register(Category)
admin.site.register(User3)

# Register your models here.

admin.site.register(User)
