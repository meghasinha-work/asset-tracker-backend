# from django.http import JsonResponse
# from .models import EmployeeMaster

# def check_employee(request):
#     email = request.GET.get("email")

#     if not email:
#         return JsonResponse({"error": "Email is required"}, status=400)

#     emp = EmployeeMaster.objects.filter(company_email_id=email).first()

#     if not emp:
#         return JsonResponse({"status": "Employee not found"}, status=404)

#     return JsonResponse({
#         "status": "Employee found",
#         "full_name": emp.full_name,
#         "email": emp.company_email_id,
#         "date_of_exit": emp.date_of_exit
#     })


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmployeeMaster

@api_view(["POST"])
def check_employee(request):
    email = request.data.get("email")

    if not email:
        return Response({"error": "Email is required"}, status=400)

    emp = EmployeeMaster.objects.filter(company_email_id=email).first()

    if not emp:
        return Response({"status": "Employee not found"}, status=404)

    return Response({
        "status": "Employee found",
        "full_name": emp.full_name,
        "email": emp.company_email_id,
        "date_of_exit": emp.date_of_exit
    })
