from datetime import datetime
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.utils.text import slugify
from django.utils.timesince import timesince


# Create your models here.
class Cliente(models.Model):

    CLASSE_CHOISES = (
        ("VIP", "cliente tipo VIP"),
        ("NOR", "cliente normal")
    )

    nome_cliente = models.CharField(max_length=100, null=False, blank=False)
    tipo_classe = models.CharField(max_length=3, choices=CLASSE_CHOISES)
    cpf = models.IntegerField(null=False, blank=False)
    endereco = models.CharField(max_length=255, null=False, blank=False)
    pessoa_contato = models.CharField(max_length=200, null=False, blank=False)
    telefone = models.CharField(max_length=11)
    upload = models.ImageField(upload_to ='uploads/', null=True)

    def __str__(self):
        return self.nome_cliente


class Apartamento(models.Model):

    TIPO_CHOISES = (
        ("1", "simples solteiro"),
        ("2", "duplo solteiro"),
        ("3", "simples casal"),
        ("4", "apartamento")
    )

    numero_apto = models.IntegerField(null=False, blank=False)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOISES, null=False, blank=False)

    def __str__(self):
        return str(self.numero_apto) + " - " + self.tipo


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reserva')
    Apartamento = models.OneToOneField(Apartamento, on_delete=SET_NULL, null=True)
    data_reserva = models.DateTimeField(auto_now_add=True)
    periodo_inicio = models.DateField(null=False, blank=False)
    periodo_fim = models.DateField(null=False, blank=False)
    encerrado = models.BooleanField(default=False)
    valor_total = models.FloatField(null=True)
    valor_total_produtos = models.FloatField(null=True)

    def __str__(self):
        return self.cliente.nome_cliente + " - " + str(self.Apartamento.numero_apto) + " - " + str(self.data_reserva)

    def get_time_diff(self):
        return timesince(self.periodo_inicio, self.periodo_fim)  # Assuming dt2 is the more recent time

    def get_total(self):
        return self.valor_total + self.valor_total_produtos
    


class Produto(models.Model):
    nome = models.CharField(max_length=40, null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    estoque = models.IntegerField(null=False, blank=False)
    codigo_barras = models.CharField(max_length=44, null=False, blank=False)

    def __str__(self):
        return self.nome


class Produto_Cliente(models.Model):
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def get_total_value(self):
        produto = Produto.objects.get(pk=self.id_produto.id)
        reserva = Reserva.objects.filter(cliente=self.id_cliente).get(encerrado=False)
        valor_total = self.quantidade * produto.preco

        reserva.valor_total_produtos += valor_total
        reserva.save()
        
        return valor_total
