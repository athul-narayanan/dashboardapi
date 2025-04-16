from rest_framework import generics
from rest_framework.response import Response
import os
from django.conf import settings
from dashboard.models import DashboardFile
import pandas as pd
from django.conf import settings
import google.generativeai as genai


genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')



class QuestionGeminiView(generics.GenericAPIView):
    """
        This view is to get question answer from gemini
    """

    def post(self, request):
        """
            Get question answer for questions on file
        """
        try:
            df = {}
            question = request.data.get("question")
            filetype = request.data.get("filetype")

            file = DashboardFile.objects.get(file_name = filetype)
            file_name = file.link

            if question is None:
                return Response({'error': "question is required"}, status=400)
            
            filepath = os.path.join(settings.MEDIA_ROOT, file_name )
            if filepath.find("xlsx") != -1:
                df = pd.read_excel(filepath)
            else:
                df = pd.read_csv(filepath)

            # Define the prompt based on question and file
            prompt = f"""
                Given the following information.
                {df.to_string()}

                answer the following question: {question}
            """

            response = model.generate_content(prompt)
            answer = response.text

            return Response({'answer': answer})
        except Exception as exp:
            print(exp)
            return Response({'error': "something went wrong"}, status=500)
    