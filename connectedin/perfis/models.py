# connectedin/perfis/models.py

from django.db import models

class Perfil(models.Model):
	nome = models.CharField(max_length=255, null=False, default = '')
	email = models.CharField(max_length=255, null=False, default= '')     
	telefone = models.CharField(max_length=15, null=False, default = '')
	nome_empresa = models.CharField(max_length=255, null=False, default='')
	contatos = models.ManyToManyField('self')

	def convidar(self,perfil_convidado):
		convite = Convite(solicitante=self,convidado=perfil_convidado).save()


class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, related_name = 'convites_feitos')
	convidado = models.ForeignKey(Perfil, related_name = 'convites_recebidos')

	def aceitar(self):
		self.convidado.contatos.add(self.solicitante)
		self.solicitante.contatos.add(self.convidado)
		self.delete()
