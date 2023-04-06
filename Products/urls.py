from django.urls import path
from .views import createnewProduct,ProductDetail,ProductList

urlpatterns = [
    path('createnewproduct/', createnewProduct,name = "createnewfile"),
    path('getproductdata/<int:pk>',ProductDetail.as_view(),name='getfiledata'),
    path('getallproductsdata/',ProductList.as_view(),name='getfiledata')
]
