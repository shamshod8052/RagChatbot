import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rag_chat_bot import RAGChatBot
from .models import Info, Message, BOTS


def index(request):
    return render(request, "Control/index.html")


def ask(request):
    if request.method != "POST":
        return
    data = json.loads(request.body)
    question = data.get("question")
    bot = BOTS.get(request.user.id)
    if not bot:
        bot = RAGChatBot()
        BOTS[request.user.id] = bot

    answer = bot.ask(question)
    if request.user.id:
        Message.objects.create(author_id=request.user.id, question=question, answer=answer)

    return JsonResponse({"answer": answer})


@csrf_exempt
def update_info_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        order = data.get('order', [])
        for index, obj_id in enumerate(order):
            Info.objects.filter(id=obj_id).update(order=index + 1)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

def load_messages(request):
    # Fetch all messages from the database
    messages = Message.objects.filter(author_id=request.user.id).all()[:50].values('question', 'answer')

    # Return the messages as JSON
    return JsonResponse({"messages": list(messages)}, safe=False)
