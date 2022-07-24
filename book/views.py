from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentication.classes.custom_auth_token import BearerTokenAuthentication
from book.models import Book, BookCompany
from book.serializer import BookCompanySerializer, BookSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(["GET"])
def get_books(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response({
        "detail": "Fetched all",
        "data": serializer.data
    })


@api_view(["POST"])
def create_book(request):
    try:
        data = request.data
        serializer = BookSerializer(data=data)
        if not serializer.is_valid():
            print(serializer.data)
            return Response(data={"detail": "Validation error", "data": serializer.errors}, status=422)

        serializer.save()
        return Response({
            "detail": "Created",
            "data": serializer.data
        })

    except Exception as e:
        print(e)
        return Response(data={"detail": "Error"}, status=500)


@api_view(["PATCH"])
def patch_book(request):
    try:
        data = request.data
        if not data.get('id'):
            return Response(data={"detail": "id is required"}, status=404)

        obj = Book.objects.get(id=data.get('id'))
        serializer = BookSerializer(obj, data=data, partial=True)
        if not serializer.is_valid():
            print(serializer.data)
            return Response(data={"detail": "Validation error", "data": serializer.errors}, status=422)

        serializer.save()
        return Response({
            "detail": "Patched",
            "data": serializer.data
        })

    except Exception as e:
        print(e)
        return Response(data={"detail": "Error"}, status=500)


# request handler using API VIEW(Recommanded)
class BookView(APIView):
    
    def get(self, request):
        book_objs = Book.objects.all()
        serializer = BookSerializer(book_objs, many=True)
        return Response({
            "detail": "Fetched all",
            "data": serializer.data
        })


    def post(self, request):
        try:
            data = request.data
            serializer = BookSerializer(data=data)
            if not serializer.is_valid():
                print(serializer.data)
                return Response(data={"detail": "Validation error", "data": serializer.errors}, status=422)

            serializer.save()
            return Response({
                "detail": "Created",
                "data": serializer.data
            })

        except Exception as e:
            print(e)
            return Response(data={"detail": "Error"}, status=500)


    def patch(self, request):
        try:
            data = request.data
            if not data.get('id'):
                return Response(data={"detail": "id is required"}, status=404)

            obj = Book.objects.get(id=data.get('id'))
            serializer = BookSerializer(obj, data=data, partial=True)
            if not serializer.is_valid():
                print(serializer.data)
                return Response(data={"detail": "Validation error", "data": serializer.errors}, status=422)

            serializer.save()
            return Response({
                "detail": "Patched",
                "data": serializer.data
            })

        except Exception as e:
            print(e)
            return Response(data={"detail": "Error"}, status=500)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes=[BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @action(methods=["GET"],detail=False)
    def get_books_from_action(self,request):
        book_objs = Book.objects.all()
        serializer = BookSerializer(book_objs, many=True)
        return Response({
            "detail": "Fetched all",
            "data": serializer.data
        })
        
    @action(methods=["GET"],detail=False)
    def get_companies(self,request):
        book_author_objs = BookCompany.objects.all()
        serializer = BookCompanySerializer(book_author_objs, many=True)
        return Response({
            "detail": "Fetched all",
            "data": serializer.data
        })
        
    @action(methods=["POST"],detail=False)
    def add_company(self,request):
        try:
            data = request.data
            print("data",data)
            serializer = BookCompanySerializer(data=data)
            if not serializer.is_valid():
                print(serializer.data)
                return Response(data={"detail": "Validation error", "data": serializer.errors}, status=422)

            serializer.save()
            return Response({
                "detail": "Created",
                "data": serializer.data
            })

        except Exception as e:
            print(e)
            return Response(data={"detail": "Error"}, status=500)