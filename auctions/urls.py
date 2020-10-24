from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("submit", views.submit, name="submit"),
    path("listing/<int:id>", views.listingPage, name="listingpage"),
    path("bidsubmit/<int:listingid>", views.bid_submit, name="bidsubmit"),
    path("allcategories", views.categories, name="allcategories"),
    path("category/<str:category>", views.category, name="category"),
    path("cmtsubmit/<int:listingid>", views.cmtsubmit, name="cmtsubmit"),
    path("addwatchlist/<int:listingid>",views.addwatchlist,name="addwatchlist"),
    path("removewatchlist/<int:listingid>",views.removewatchlist,name="removewatchlist"),
    path("watchlist/<str:username>",views.watchlistpage,name="watchlistpage"),
    path("closebid/<int:listingid>",views.closebid,name="closebid"),
    path("mywinnings",views.mywinnings,name="mywinnings"),
]
