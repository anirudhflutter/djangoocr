from rest_framework import viewsets

from my_awesome_api.serializers import PersonSerializer, SpeciesSerializer, OcrdataSerializer
from my_awesome_api.models import Person, Species
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from doctr.models import ocr_predictor
from doctr.io import DocumentFile

class PersonViewSet(viewsets.ModelViewSet):
   queryset = Person.objects.all()
   serializer_class = PersonSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Species.objects.all()
   serializer_class = SpeciesSerializer


class OcrDataView(APIView):
   def post(self, request):
      serializer = OcrdataSerializer(data=request.data)
      if serializer.is_valid():
         ocr = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)
         result = ocr(DocumentFile.from_images("12.png"))
         return Response({"status": "success", "data": result.export()}, status=status.HTTP_200_OK)
      else:
         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)