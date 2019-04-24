from django.db import models

class ContactForm(models.Model):
    HOW_DID_YOU_HEAR_ABOUT_US_CHOICES = (
        ('SE', 'Search Engine'),
        ('Q', 'Quakkels.com'),
        ('F', 'From a friend'),
        ('O', 'Other')
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    comments = models.CharField(max_length=500)
    how_did_you_hear_about_us = models.CharField(max_length=2, choices=HOW_DID_YOU_HEAR_ABOUT_US_CHOICES)
