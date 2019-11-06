from django.urls import path,re_path
from products.views import (
    # Product_List,
    # Product_Detail,
    # ProductFeaturedDetailView,
    # ProductFeaturedListView,
    # Category_List,
    Shop_List,
    slug
    )

urlpatterns = [
    path('',Shop_List),
    path('<slug>',slug),
    # path('products/',Product_List),
    # path('featured/',ProductFeaturedListView.as_view()),
    # re_path('featured/(?P<pk>\d+)/',ProductFeaturedDetailView.as_view())
    # re_path('(?P<pk>\d+)',Product_Detail),
    # path('',Shop_List),
    # re_path('(?P<pk>\d+)',Category_List),
    # path('<slug>/<detail_slug>',slug),
    # path('shop/category/',Category_List),
]