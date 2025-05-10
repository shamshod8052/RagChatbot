from django.contrib.auth.models import User
from django.db import models
from ordered_model.models import OrderedModel, OrderedModelManager

BOTS = dict()

class InfoManager(OrderedModelManager):
    def get_texts(self):
        text = '\n'.join(
            [
               info.text for info in self.filter(status=True).all()
            ]
        )

        return text

class Info(OrderedModel):
    objects = InfoManager()

    name = models.CharField(verbose_name="Nomi", max_length=100)
    text = models.TextField(
        verbose_name="AI o'rganish matni",
        help_text="Bu kiritilgan ma'lumotni AI o'rganib oladi!"
    )
    status = models.BooleanField(
        verbose_name="Holati",
        default=True,
        help_text="Matnni o'rganish yoki o'rganmaslik holati."
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        global BOTS
        BOTS.clear()

        super(Info, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Ma'lumot "
        verbose_name_plural = "Ma'lumotlar "
        ordering = ['order']


class Message(OrderedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(
        verbose_name="Savol"
    )
    answer = models.TextField(
        verbose_name="Javob"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:32] + '...' if len(self.question) > 32 else self.question

    class Meta:
        verbose_name = "Xabar "
        verbose_name_plural = "Xabarlar "
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['author', 'created_at']),
        ]
