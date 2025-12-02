from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ml.predict import predict_sentiment

@api_view(['POST'])
def get_sentiment(request):
    text = request.data.get("review", "")
    sentiment, confidence = predict_sentiment(text)
    return Response({
        "sentiment": sentiment,
        "confidence": confidence
    })
