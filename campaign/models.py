from django.db import models

# 1. CAMPAGNES SMS

class Campaign(models.Model):
    name = models.CharField(max_length=200)
    sender = models.CharField(max_length=20)
    message = models.TextField()
    number_file = models.FileField(upload_to='campaign_numbers/', null=True, blank=True)
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    daily_start_time = models.TimeField(null=True, blank=True)
    daily_end_time = models.TimeField(null=True, blank=True)
    excluded_days = models.CharField(max_length=50, blank=True, help_text="0=Dimanche, 6=Samedi. Ex: 0,6")
    ignore_before = models.CharField(max_length=20, blank=True, null=True)
    ignore_after = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Brouillon'),
            ('planified', 'Planifiée'),
            ('running', 'En cours'),
            ('paused', 'En pause'),
            ('finished', 'Terminée'),
            ('aborted', 'Annulée')
        ],
        default='draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CampaignSendLog(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='send_logs')
    number = models.CharField(max_length=20)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'En attente'),
            ('sent', 'Envoyé'),
            ('failed', 'Échec'),
            ('blacklisted', 'Black-listé')
        ],
        default='pending'
    )
    sent_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.number} ({self.campaign.name})"

# 2. BLACKLIST

class BlacklistEntry(models.Model):
    number = models.CharField(max_length=20, unique=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number

class BlacklistBatchImport(models.Model):
    file = models.FileField(upload_to='blacklist_imports/')
    imported_at = models.DateTimeField(auto_now_add=True)
    imported_by = models.CharField(max_length=100, blank=True, null=True)
    processed = models.BooleanField(default=False)
    result = models.TextField(blank=True, null=True)

# 3. CONVERSION DE NUMERO

class NumberAlias(models.Model):
    number = models.CharField(max_length=20, unique=True)
    alias = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.number} -> {self.alias}"

# 4. DESACTIVATION

class DeactivatedNumber(models.Model):
    number = models.CharField(max_length=20, unique=True)
    alias = models.CharField(max_length=64, blank=True, null=True)
    deactivated_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(blank=True, null=True)
    is_blacklisted = models.BooleanField(default=False)

    def __str__(self):
        return self.number

# 5. LOGS GLOBAUX (actions diverses)

class ActionLog(models.Model):
    action = models.CharField(max_length=100)
    target_number = models.CharField(max_length=20, blank=True, null=True)
    performed_by = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    performed_at = models.DateTimeField(auto_now_add=True)
