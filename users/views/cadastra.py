from django.views.generic.base import  TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from users.models.cadastra import Usuarios
from django.shortcuts import render
from users.forms import CadastraUsuario

class CadUser(TemplateView):
    template_name = "cadastra/cadastra.html"

    def get(self, request, id=None):
        if id:
            usuario = Usuarios.objects.get(pk=id)
            form = CadastraUsuario(instance=usuario)
            return render(request,self.template_name,locals())
        else:
            form = CadastraUsuario()
            usuario = Usuarios.objects.all()
            return render(request, self.template_name,{'usuario': usuario,'form':form})

    def post(self,request,id=None):
         if id:
            usuario = Usuarios.objects.get(pk=id)
            form = CadastraUsuario(instance=usuario, data=request.POST)
         else:
            form = CadastraUsuario(request.POST)
            usuario = Usuarios.objects.all()
         if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('add'))
         else:
            return render(request, self.template_name,{'usuario': usuario, 'form': form})

class DeleteUser(TemplateView):
    def get(self,request,id):
        usuario = Usuarios.objects.get(pk=id)
        usuario.delete()
        return HttpResponseRedirect(reverse('showall'))

class ShowAllUsers(TemplateView):
    template_name = "cadastra/index.html"
    def get(self,request):
        usuario = Usuarios.objects.all()
        return render(request, self.template_name, locals())