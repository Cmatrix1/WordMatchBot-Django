from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Condition
from .serializers import MessageResponseSerializer


class RetrieveResponseView(APIView):
    def get(self, request, format=None):
        message = request.query_params.get('message', '')
        conditions = Condition.objects.all()

        for condition in conditions:
            ruleset_operation = condition.ruleset.operation
 
            if condition.check_condition(message):
                if ruleset_operation == "or":
                    serializer = MessageResponseSerializer(condition.ruleset.response)
                    return Response(status=status.HTTP_200_OK , data=serializer.data)
                
                for rulset_condition in condition.ruleset.conditions.all():
                    if not rulset_condition.check_condition(message):
                        return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = MessageResponseSerializer(condition.ruleset.response)
                return Response(status=status.HTTP_200_OK , data=serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)
