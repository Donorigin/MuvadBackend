from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer



@api_view(['POST'])
@authentication_classes([])  # Disable authentication
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data
        return Response({
            'token': token.key,
            'user': user_data
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def list_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BlogSerializer(blog)
    return Response(serializer.data)

@api_view(['POST'])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=404)
    
    serializer = BlogSerializer(blog, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
    blog.delete()
    return Response({'message': 'Blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)