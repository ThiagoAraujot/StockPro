from django.db.models.signals import post_save
from django.dispatch import receiver
from outflows.models import OutFlow


@receiver(post_save, sender=OutFlow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.quantity -= instance.quantity
        product.save()
