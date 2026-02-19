from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ITAssetAppSubmission
from django.utils import timezone


@api_view(['POST'])
def create_submission(request):

    employee_email = request.data.get("employee_email")
    submitted_for = request.data.get("submitted_for")
    asset_owner_email_id = request.data.get("asset_owner_email_id")
    asset_id = request.data.get("asset_id")
    serial_no = request.data.get("serial_no")

    # Basic validation
    if not employee_email or not asset_id or not serial_no:
        return Response(
            {"error": "Missing required fields"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Create entry
    ITAssetAppSubmission.objects.create(
        employee_email=employee_email,
        submitted_for=submitted_for,
        asset_owner_email_id=asset_owner_email_id,
        asset_id=asset_id,
        serial_no=serial_no,
        date=timezone.now()   # timestamp
    )

    return Response(
        {"status": "Submission saved successfully"},
        status=status.HTTP_201_CREATED
    )
