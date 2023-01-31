from django.shortcuts import render
from . models import apiModel
from . serializers import apiSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

#menampilkan semua data
@api_view(["GET"])
def readall(request):
    showall = apiModel.objects.all()
    serializer = apiSerializer(showall, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

#menampilkan data berdasarkan id
@api_view(["GET"])
def readdetail(request, id):
    reads = apiModel.objects.get(id=id)
    serializer = apiSerializer(reads, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)

#menambah data
@api_view(["POST"])
def create(request):
    serializer = apiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status.HTTP_201_CREATED)

#mengupdate data berdasarkan id
@api_view(["POST"])
def update(request,id):
    datas = apiModel.objects.get(id=id)
    serializer = apiSerializer(instance=datas, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#menghapus data berdasarkan id
@api_view(["GET"])
def delete(request,id):
     datas = apiModel.objects.get(id=id)
     datas.delete()
     
     return Response('DATA BERHASIL DIHAPUS!', status=status.HTTP_204_NO_CONTENT)