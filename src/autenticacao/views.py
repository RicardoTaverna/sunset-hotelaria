from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from hotel.models import Cliente, Reserva, Produto_Cliente

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'autenticacao/signup.html', context=context)

def profile(request):

    reservas = Reserva.objects.all()
    cliente_produtos = Produto_Cliente.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get("cliente_id")
        reserva = Reserva.objects.filter(cliente=cliente_id).get(encerrado=False)
        reserva.encerrado = True
        print(reserva.encerrado)
        reserva.save()

    print("passei aqui")

    context = {
        "reservas": reservas,
        "cliente_produtos": cliente_produtos
    }

    return render(request, 'accounts/profile.html', context=context)