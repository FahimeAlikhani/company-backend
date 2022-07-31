from rest_framework.response import Response
from rest_framework import generics
import json
from .models import ProjectRequest , NewsLetterForm , ConsultingPage




class ProjectRequestSubmit(generics.ListAPIView):

    def post(self,request):
        data = json.loads(request.body)
        ProjectRequest.objects.create(
                                    name = data['name'],
                                    email = data['email'],
                                    message = data['message'])
        return Response("ProjectRequest created successfully")

class ConsultingRequestSubmit(generics.ListAPIView):

    def post(self,request):
        data = json.loads(request.body)
        ConsultingPage.objects.create(
                                    name = data['name'],
                                    email = data['email'],
                                    phone = data['phone'],
                                    message = data['message'])
        return Response("ProjectRequest created successfully")
class NewsLetterFormSubmit(generics.ListAPIView):
    
    def post(self,request):
        data = json.loads(request.body)
        NewsLetterForm.objects.create(
                                    email = data['email']
                                    )
        return Response("NewLetterForm created successfully")

