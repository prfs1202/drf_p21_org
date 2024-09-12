# from django.db.models.signals import post_delete
# from django.dispatch import receiver
#
# from apps.models import User, ProductHistory, Product
#
#
# @receiver(post_delete, sender=Product)
# def my_handler(sender, instance: Product, **kwargs):
#     ProductHistory.objects.create(
#         product_id=instance.id,
#         name=instance.name,
#         price=instance.price,
#         action="o'chirildi",
#     )
#
#
# # celery, django signals
