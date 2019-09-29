from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.views.generic import ListView,DetailView
from .models import Product


def Product_List(request):
    queryset = Product.objects.all()
    context = {
        'product_list': queryset
    }
    return render(request,"product_list.html",context)

# def Product_Detail(request):
#     queryset = Product.objects.all()
#     context = {
#         'product': queryset
#     }
#     return render(request,"product_detail.html",context)

# class Product_Detail(DetailView):
#     queryset = Product.objects.all()
#     template_name = "product_detail.html"

#     def get_object(self,*args,**kwargs):
#         request = self.request
#         slug = self.kwargs.get('slug')
#         # instance = get_object_or_404(Product,slug=slug)
#         try:
#             instance = get_object_or_404(Product,slug=slug)
#         except Product.DoesNotExist:
#             print("Object does not exist")
#         except Product.MultipleObjectsReturned:
#             qs = Product.Object.filter(slug=slug)
#             instance = qs.first()
#         return instance

class Product_Slug_Detail(DetailView):
    queryset = Product.objects.all()
    template_name = "product_detail.html"

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product,slug=slug)
        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            print("Object does not exist")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        return instance

# def Product_Detail(request, pk=None, *args, **kwargs):
#     # instance = get_object_or_404(Product, pk=pk)
#     # MODEL MANAGER
#     # instance = Product.objects.get_by_id(pk)
#     # print(instance)
#     try:
#         instance = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         raise Http404("Product doesn't exist")

#     context = {
#         'product': instance
#     }
#     return render(request,"product_detail.html",context)

# def Product_Detail(request, slug=None, *args, **kwargs):
#     # instance = get_object_or_404(Product, pk=pk)
#     # MODEL MANAGER
#     # instance = Product.objects.get_by_id(pk)
#     # print(instance)
#     try:
#         instance = Product.objects.get(slug=slug)
#     except Product.DoesNotExist:
#         raise Http404("Product doesn't exist")

#     context = {
#         'product': instance
#     }
#     return render(request,"product_detail.html",context)

class ProductFeaturedListView(ListView):
    queryset = Product.objects.all().featured()
    template_name = "product_list.html"

    # def get_queryset(self,*args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "product_detail.html"

    # def get_queryset(self,*args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()