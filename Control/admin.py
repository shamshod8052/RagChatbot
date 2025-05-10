from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .models import Info, Message


@admin.register(Info)
class InfoAdmin(OrderedModelAdmin):
    list_display = ('order_display', "name", 'part_text', "status")
    list_filter = ("status",)
    search_fields = ("name", "text")
    ordering = ("order",)
    list_editable = ("status",)

    def part_text(self, obj: Info, length=32):
        if len(obj.text) > length:
            return obj.text[:length] + "..."
        else:
            return obj.text
    part_text.short_description = "Matn"

    def order_display(self, obj: Info):
        return obj.order + 1

    order_display.short_description = "Tartib"
    order_display.admin_order_field = "order"


@admin.register(Message)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('author__username', 'question_display', 'answer_display', 'created_at')
    search_fields = ('question', 'answer')
    list_filter = ('author', 'created_at',)
    ordering = ('-created_at',)

    def question_display(self, obj: Message, length=32):
        if len(obj.question) > length:
            return obj.question[:length] + "..."
        else:
            return obj.question
    question_display.short_description = "Savol"
    question_display.admin_order_field = "question"

    def answer_display(self, obj: Message, length=32):
        if len(obj.answer) > length:
            return obj.answer[:length] + "..."
        else:
            return obj.answer
    answer_display.short_description = "Javob"
    answer_display.admin_order_field = "answer"
