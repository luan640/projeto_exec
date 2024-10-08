from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from execucao.views import criar_execucao, criar_execucao_predial, editar_solicitacao
from solicitacao.views import tarefa_rotina

urlpatterns = [
    path('criar-solicitacao/', views.criar_solicitacao, name='criar_solicitacao'),
    path('ajax/get-maquinas/', views.get_maquina_by_setor, name='get_maquina_by_setor'),
    path('ajax/get-maquinas-by-eq-falha/', views.get_maquina_by_eq_em_falha, name='get_maquina_by_eq_em_falha'),

    path('criar-solicitacao-predial/', views.criar_solicitacao_predial, name='criar_solicitacao_predial'),
    path('criar-tarefa-rotina/', views.tarefa_rotina, name='tarefa_rotina'),

    path('execucao/producao/<int:solicitacao_id>/', criar_execucao, name='criar_execucao'),
    path('execucao/predial/<int:solicitacao_id>/', criar_execucao_predial, name='criar_execucao_predial'),

    path('atualizar-status-maq-parada/', views.atualizar_status_maq_parada, name='atualizar_status_maq_parada'),

    path('filtrar-maquinas/', views.filtrar_maquinas_por_setor, name='filtrar_maquinas_por_setor'),

    path('solicitacao-sucesso/<str:area>/', views.solicitacao_sucesso, name='solicitacao_sucesso'),

    path('editar-ordem-inicial/<int:solicitacao_id>/', editar_solicitacao, name='editar_solicitacao')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)