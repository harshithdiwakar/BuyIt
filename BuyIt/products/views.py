from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse
from django.views.generic import ListView,DetailView
from .models import Product, Shop, Product_Category


def slug(request,slug):
    shops = [s.shop_slug for s in Shop.objects.all()]
    if slug in shops:
        category = Product_Category.objects.filter(category__shop_slug = slug) 
        print(category)
        queryset = category
        context = {
            'category_list': queryset
        }
        return render(request,"products/category.html",context)

    products = [p.category_slug for p in Product_Category.objects.all()]
    if slug in products:
        items = Product.objects.filter(category__category_slug = slug)
        print(items)
        queryset = items
        context = {
            "product_list": queryset
        }
        print(context)
        return render(request,"products/product_list.html",context)


    product = [p.slug for p in Product.objects.all()]
    if slug in product:
        details = Product.objects.filter(slug = slug)
        print(details)
        queryset = details
        context = {
            "detail_list": queryset
        }
        print(context)
        return render(request,"products/product_detail.html",context)
    
    return HttpResponse(f"Check again")

def Shop_List(request):
    queryset = Shop.objects.all()
    context = {
        'shop_list': queryset
    }
    return render(request,"index.html",context)


# def Product_List(request):
#     queryset = Product.objects.all()
#     context = {
#         'product_list': queryset
#     }
#     return render(request,"product_list.html",context)


# def Product_Detail(request, pk=None, *args, **kwargs):
#     # instance = get_object_or_404(Product, pk=pk)
#     # MODEL MANAGER
#     # instance = Product.objects.get_by_id(pk)
#     # print(instance)
#     try:
#         instance = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         raise Http404("Product doesn't exist")

#     context = {
#         'product': instance
#     }
#     return render(request,"product_detail.html",context)


# class ProductFeaturedListView(ListView):
#     queryset = Product.objects.all().featured()
#     template_name = "product_list.html"


# class ProductFeaturedDetailView(DetailView):
#     queryset = Product.objects.all().featured()
#     template_name = "product_detail.html"