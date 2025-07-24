from django.db import models

class Theme(models.Model):
    libelle = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)
    actif = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.libelle

class Souscription(models.Model):
    numero = models.CharField(max_length=20)  # MSISDN
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='souscriptions')
    type = models.CharField(max_length=20, choices=[('Journalier','Journalier'),('Hebdomadaire','Hebdomadaire'),('Mensuel','Mensuel')])
    auto = models.BooleanField(default=False)
    date_souscription = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(null=True, blank=True)
    actif = models.BooleanField(default=True)
    paiement_succes = models.BooleanField(default=False)
    date_desactivation = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.numero} ({self.theme.libelle})"

class Publication(models.Model):
    contenu = models.TextField()
    date_publication = models.DateTimeField()
    actif = models.BooleanField(default=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='publications')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.theme.libelle} - {self.date_publication.strftime('%d/%m/%Y %H:%M')}"
