from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
import json

# Quotes for the Message Board
QUOTES = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Dream big and dare to fail.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
]

# Main page view


def index(request):
    return render(request, 'messageboard/index.html')

@csrf_exempt
def submit_message(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        sender = data.get('sender')
        recipient = data.get('recipient')
        message = data.get('message')

        if sender and recipient and message:
            # Save the message to the database
            Message.objects.create(sender=sender, recipient=recipient, message=message)
            return JsonResponse({'status': 'Message sent successfully!'})
        else:
            return JsonResponse({'error': 'Invalid input data'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_messages(request, sender_name):
    # Retrieve the latest 20 messages sent by the given sender
    messages = Message.objects.filter(sender=sender_name).order_by('-timestamp')[:20]
    messages_data = [
        {'recipient': msg.recipient, 'message': msg.message, 'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        for msg in messages
    ]
    return JsonResponse({'messages': messages_data})