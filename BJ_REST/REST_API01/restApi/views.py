from django.shortcuts import render
from . models import produkModel
# kebutuhan api
from .serializers import produkSerializer
# kebutuhan rest
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET']) #untuk menamilkan
def readProduk(request):
    produks = produkModel.objects.all() #ambilsemua data
    serializer = produkSerializer(produks, many=True) #semua data trsb simpan di serializer
    return Response(serializer.data)

@api_view(['GET']) #untuk menamilkan
def ProdukDetail(request, id):
    produks = produkModel.objects.get(id=id) #ambilsemua data
    serializer = produkSerializer(produks, many=False) #semua data trsb simpan di serializer
    return Response(serializer.data)

@api_view(['POST']) #untuk menamilkan
def createProduk(request):
    serializer = produkSerializer(data=request.data) #semua data trsb simpan di serializer
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST']) #untuk menamilkan
def updateProduk(request, id):
    produks = produkModel.objects.get(id=id) #ambilsemua data
    serializer = produkSerializer(instance=produks, data=request.data) #semua data trsb simpan di serializer
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET']) #untuk menamilkan
def deleteProduk(request, id):
    produks = produkModel.objects.get(id=id) #ambilsemua data
    produks.delete()

    return Response('Data berhasil di HAPUS!')

