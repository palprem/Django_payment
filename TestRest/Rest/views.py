from django.shortcuts import render
from django.http import HttpResponse
from .models import Pdataile
from rest_framework.decorators import api_view
from django.http import JsonResponse
from uuid import uuid4

#
@api_view(["POST"])
def added(request):
    if request.method=="POST":
        data=request.data
        
        print(data)

        student = Pdataile(transection_date=data["transection_date"],
                                 amount=data["amount"],
                                 Order_no=data["Order_no"],
                                 customer_Id=data["customer_Id"],
                                 date_recieve=data["date_recieve"],
                                 tranjection_code=data["tranjection_code"],
                                 tranjection_text=data["tranjection_text"],
                                 )
        student.save()
        return JsonResponse({"status":True})

        
        
def manage(request):
    l=[]
    # hostels = Pdataile.objects.all()

    data= Pdataile.objects.all().values("transection_date","amount","Order_no","customer_Id","date_recieve","tranjection_code","tranjection_text")
    print(data)
    for i in data:
        l.append({"transection_date": i["transection_date"],
                  "amount": i["amount"],
                  "Order_no": i["Order_no"],
                  "customer_Id": i["customer_Id"],
                  "date_recieve": i["date_recieve"],
                  "tranjection_code": i["tranjection_code"],
                  "tranjection_text": i["tranjection_text"]}),
    return JsonResponse({"status":i})

#
#
# # Create your views here.
