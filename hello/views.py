from django.shortcuts import render

def hello_world(request):
    # Dynamic data passed to the template
    context = {
        'title': 'Hello, World!',
        'message': 'Welcome to the improved Django page created with the MVT pattern!',
        'button_text': 'Click Me!',
    }
    return render(request, 'hello/hello.html', context)