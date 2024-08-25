from django.db import models

class Titulo(models.Model):
    '''Cria um titulo para a postagem.'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''devolve um representação em STRING do modelo.'''
        return self.text
    
class Corpo(models.Model):
    '''Cria o corpo do título selecionado.'''
    topic = models.ForeignKey(Titulo, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Artigos'

    def __str__(self):
        '''devolve um representação em STRING do modelo.'''
        return self.text[:50] + "..."
    
class Novidade(models.Model):
    titulo = models.CharField(max_length=200)
    corpo = models.TextField(max_length=1500)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
