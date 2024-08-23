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
        verbose_name_plural = 'Corpo_do_texto'

    def __str__(self):
        '''devolve um representação em STRING do modelo.'''
        return self.text[:50] + "..."
    

