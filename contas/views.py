import datetime

from django.shortcuts import render, redirect

from .form import TransacaoForm
from .models import Transacao


# Create your views here.
def home(request):
    lista = {}
    lista['feiras'] = [{'localizacao': {'descrição': 'Praça do Relógio', 'logradouro': 'Rua 16 de Novembro'}},
                       {'localizacao': {'descrição': 'Praça das Serias', 'logradouro': 'Rua Dutra'}},
                       {'localizacao': {'descrição': 'Praça da República', 'logradouro': 'Avenida Presidente Vargas'}}]
    now = datetime.datetime.now()
    # html = """
    #         <html>
    #             <body>
    #             It is now %s
    #             </body>
    #         </html>
    # """ % now
    return render(request, 'contas/home.html', lista)


def listagem(request):
    transacoes = Transacao.objects.all()

    return render(request, 'contas/listagem.html', {'transacoes': transacoes})


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, 'contas/form.html', {'form': form})


def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['transaca'] = transacao
    data['form'] = form
    return render(request, 'contas/form.html', data)


def delete(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
