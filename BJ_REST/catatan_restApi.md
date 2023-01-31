#PERTANYAAN
-apa maksud dari many=True, cth:
@api_view(['GET', 'POST'])
def book_collection(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

-apa maksud try and exception, cth:
@api_view(['GET', 'DELETE'])
def book_element(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)
#BELAJAR API

-ENDPOINT / URL
-METHODE
C   = POST
R   = GET
U   = PUT/PATCH
D   = DELETE


