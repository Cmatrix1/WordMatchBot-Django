from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Condition
from .serializers import MessageResponseSerializer


class RetrieveResponseView(APIView):
    def get(self, request, format=None):
        message = request.query_params.get('message', '')
        conditions = Condition.objects.all()
        
        matched_responses = []
        for condition in conditions:
            keywords = list(map(lambda x: x.strip(), condition.get_keywords()))
            print(keywords)
            if (condition.operation == 'and' and all(keyword in message for keyword in keywords)) or \
               (condition.operation == 'or' and any(keyword in message for keyword in keywords)):
                matched_responses.append(condition.response)

        serializer = MessageResponseSerializer(matched_responses, many=True)
        return Response(status=status.HTTP_200_OK , data=serializer.data)
