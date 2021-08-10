from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView


class PushNotification(APIView):
    def post(self, request, *args, **kwargs):

        result = settings.PUSH_SERVICE.notify_single_device(registration_id="cJJxVXRiSCqbPStH2uL66Q:APA91bHuUwrD4jVHpvGcPMPPkHCXv-btwJ3HzCnMOoVDTFABzKAULgYiUTFRYDoaltmBvoIMRkbQ-XtArfxUAwOkRKCutjv6IdBBYGEBicgVBdtdK6Sej8HyRP_k6HfzqmKaanYGjn_n",
                                                        message_title="Hello", message_body="Testing message body",
                                                        )
        if result['success'] is 1:
            return Response({'message': "notificaiton sended successfully"})
        
        return Response(result)
