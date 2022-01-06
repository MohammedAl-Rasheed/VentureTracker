from django.db import models

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from django.db.models import signals

import requests
import json

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=60, unique=True)
    affiliateLink = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='media', blank=True, null=True)
    companyType = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name', 'affiliateLink', 'twitter', 'logo', 'companyType']


class Asset(models.Model):
    company = models.ManyToManyField(Company, blank=False)
    name = models.CharField(max_length=60, unique=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=60, blank=True, null=True)

    # Smart Contract Detail
    smartContractAddress = models.CharField(max_length=500, blank=True, null=True, unique=True)
    
    asset_platform = models.CharField(max_length=60, blank=True, null=True)
    
    currentMarketCap = models.FloatField(blank=True, null=True) 
    currentPrice = models.FloatField(blank=True, null=True)
    
    lastMonthMarketCap = models.FloatField(blank=True, null=True, default=0)

    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    # I beleive this is deprecated
    class Meta:
        unique_together = (('name', 'url', 'image', 'category', 'smartContractAddress', 'asset_platform'),)


@receiver(post_save, sender=Asset)
def updatePrices(sender, instance, signal, *args, **kwargs):
    if instance.smartContractAddress != None:
        # if not instance.initialMarketCap and instance.asset_platform: 
        # Get current marketcap and price from coingeko
        currency = "USD"
        contractAddress = instance.smartContractAddress
        assetPlatform = instance.asset_platform

        url = f"https://api.coingecko.com/api/v3/simple/token_price/{assetPlatform}?contract_addresses={contractAddress}&vs_currencies={currency}&include_market_cap=true"

        response = requests.get(url)
        data = json.loads(response.text)
        
        # instance.initialMarketCap = data[contractAddress][currency.lower() + "_market_cap"] 
        # instance.initialPrice = data[contractAddress][currency.lower()]
        Asset.objects.filter(id=instance.id).update(initialMarketCap=data[contractAddress][currency.lower() + "_market_cap"] , initialPrice=data[contractAddress][currency.lower()])
