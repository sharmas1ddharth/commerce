
from django.contrib import admin
from .models import User, Listing, Bid,Comment,Watchlist,Closedbid,Alllisting
# Register your models here.

admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Watchlist)
admin.site.register(User)
admin.site.register(Alllisting)
admin.site.register(Comment)
admin.site.register(Closedbid)