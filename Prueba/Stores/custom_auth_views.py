from oauth2_provider.views import TokenView
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class CustomTokenView(TokenView):
    def post(self, request, *args, **kwargs):
        #Obtener los datos de la solicitud POST
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        if not email or not otp:
            return JsonResponse({'error':'email y otp son requeridos'}, status=400)
        
        #Autenticar el usuario
        user = authenticate(request=request, email=email, otp=otp)
        if not user:
            return JsonResponse({'error':'credenciales invalidas'}, status=401)
        
        #Si el usuario es autenticado, generar el token
        response_data = super().post(request, *args, **kwargs)
        return JsonResponse(response_data.json(), status=response_data.status_code)