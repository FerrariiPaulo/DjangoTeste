from rest_framework.test import APITestCase 
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CT1',
            descricao='Curso Teste 1',
            nivel= 'B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CT2',
            descricao='Curso Teste 2',
            nivel= 'A'
        )
        
    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a conexão GET para listar cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a conexão POST para adicionar curso"""
        data = {
            'codigo_curso' : 'CT3',
            'descricao': 'Curso Teste',
            'nivel': 'A'
        }
        
        response = self.client.post(self.list_url, data = data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        
    def test_requisicao_delete_para_deletar_curso(self):
        """Teste para verificar a requisição DELETE não permitida para deletar um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
