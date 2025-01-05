import os
from django.http import (
    HttpResponse, 
    JsonResponse, 
    StreamingHttpResponse, 
    FileResponse
)
from django.conf import settings

# 1. HttpResponse - Text response
def text_response(request):
    return HttpResponse("This is a sample text response!")

# 2. HttpResponse - HTML response
def html_response(request):
    html_content = """
    <html>
        <head><title>HTML Response</title></head>
        <body>
            <h1 style="color:blue;">Welcome to Django Response Examples</h1>
        </body>
    </html>
    """
    return HttpResponse(html_content, content_type="text/html")

# 3. JsonResponse - JSON response
def json_response(request):
    data = {"message": "This is a JSON response", "status": "success"}
    return JsonResponse(data)

# 4. StreamingHttpResponse - Streaming response
def stream_response(request):
    def stream_generator():
        yield "This is a "
        yield "streaming response "
        yield "in Django."
    return StreamingHttpResponse(stream_generator())

# 5. FileResponse - Text file response
def text_file_response(request):
    file_path = os.path.join(settings.BASE_DIR, 'responseexamples/static', 'django.txt')
    return FileResponse(open(file_path, 'rb'), content_type='text/plain')

# 6. FileResponse - Image response
def image_response(request):
    image_path = os.path.join(settings.BASE_DIR, 'responseexamples/static', '10_Image.jpg')
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')

# 7. FileResponse - PDF response
def pdf_response(request):
    pdf_path = os.path.join(settings.BASE_DIR, 'responseexamples/static', 'Assignment two (1).pdf')
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')

# 8. FileResponse - Video response
def video_response(request):
    video_path = os.path.join(settings.BASE_DIR, 'responseexamples/static', 'IMG_2286[1].mp4')
    return FileResponse(open(video_path, 'rb'), content_type='video/mp4')

# 9. HttpResponse - CSV response
def csv_response(request):
    csv_content = "name,age,city\nRofaida,22,Riga\nRofaida,22,Algeria\n"
    response = HttpResponse(csv_content, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sample.csv"'
    return response

# 10. HttpResponse - Custom XML response
def xml_response(request):
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
    <note>
        <to>User</to>
        <from>Server</from>
        <heading>Response</heading>
        <body>This is a sample XML response</body>
    </note>
    """
    return HttpResponse(xml_content, content_type='application/xml')
