from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AssetMaster


# @api_view(['POST'])
# def verify_asset(request):

#     asset_tag = request.data.get("asset_tag_id")
#     serial_no = request.data.get("serial_no")
#     email = request.data.get("email")

#     # Step 1: Validate input
#     if not asset_tag and not serial_no:
#         return Response(
#             {"error": "Provide either asset_tag_id or serial_no"},
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     # Step 2: Find asset
#     asset = None

#     if asset_tag:
#         asset = AssetMaster.objects.filter(AssetTagID=asset_tag).first()

#     elif serial_no:
#         asset = AssetMaster.objects.filter(AssetSerialNo=serial_no).first()

#     # Step 3: If asset not found
#     if not asset:
#         return Response(
#             {"status": "Asset not found"},
#             status=status.HTTP_404_NOT_FOUND
#         )

#     # Step 4: If email provided → validate internally
#     if email:
#         if asset.EmailId != email:
#             return Response(
#                 {"status": "Asset found but email does not match"},
#                 status=status.HTTP_403_FORBIDDEN
#             )

#     # Step 5: Success response (DO NOT return email)
#     return Response(
#         {
#             "status": "Asset found",
#             "asset_tag_id": asset.AssetTagID,
#             "serial_no": asset.AssetSerialNo,
#             "assigned_to": asset.AssignedTo,
#         },
#         status=status.HTTP_200_OK
#     )

@api_view(['POST'])
def verify_asset(request):

    asset_tag = request.data.get("asset_tag_id")
    serial_no = request.data.get("serial_no")

    if not asset_tag and not serial_no:
        return Response(
            {"error": "Provide either asset_tag_id or serial_no"},
            status=status.HTTP_400_BAD_REQUEST
        )

    asset = AssetMaster.objects.filter(
        AssetTagID=asset_tag
    ).first() or AssetMaster.objects.filter(
        AssetSerialNo=serial_no
    ).first()

    if not asset:
        return Response(
            {"error": "Invalid asset_tag_id or serial_no"},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(
        {
            "status": "Asset found",
            "asset_tag_id": asset.AssetTagID,
            "serial_no": asset.AssetSerialNo,
            "assigned_to": asset.AssignedTo,
        },
        status=status.HTTP_200_OK
    )
