from django.forms import ModelForm
from users.models import Usuarios

class CadastraUsuario(ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'