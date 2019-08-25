from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from api.models import Produto
from rest_framework.response import Response

class BuscaProdutos(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def create(self, request, *args, **kwargs):
        buscador = Produto()
        dados = request.data
        dados_scrapping = buscador.buscaProduto(dados=dados)
        return Response({"status":200,"dados":dados_scrapping})
