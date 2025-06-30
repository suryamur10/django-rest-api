from django.shortcuts import render
from .serializers import MessageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def message_list(request):
    if request.method == 'GET':
        query = request.query_params.get('q')
        logger.info("GET /messages called")
        if query:
            messages = Message.objects.filter(text__istartswith=query)
        else:
            messages = Message.objects.all()

        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        logger.info("POST /messages called with data: %s", request.data)
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("POST /messages error: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
