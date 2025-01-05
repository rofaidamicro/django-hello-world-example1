## Django Hello World - Example 1

## Overview
This project is part of a Django assignment to demonstrate the implementation of a **Hello World** application. It uses Django's built-in framework to create a simple web page that combines HTML, CSS, and JavaScript for a visually appealing design.

## Features
- Displays a "Hello, World!" message on the webpage.
- Styled using CSS with a pastel pink gradient background.
- Includes a clickable button with hover effects and animations.
- Implements Django's template system for rendering the page.

## Project Structure

## How to Run
1. Clone the repository:
   ```bash
      git clone https://github.com/rofaidamicro/django-hello-world-example1.git
2. Navigate to the project directory:

        cd django-hello-world-example1
 3. Install dependencies: Make sure you have Python and Django installed. If not, create a virtual environment and install Django:

        python -m venv venv
        source venv/bin/activate
# On Windows: 
       venv\Scripts\activate
       pip install django 

4. Run the development server:

       python manage.py runserver
5. Open the application in your browser
 # Technologies Used
Python: Backend programming.
Django: Framework for building the web application.
HTML, CSS, JavaScript: Frontend for designing the webpage.


## Example 2: Improved Django Page with MVT Pattern
This example builds on Example 1 by introducing the Model-View-Template (MVT) pattern. It includes animations.

Features:

Dynamic animations and theme switching
Cat gallery (because I'm obssessed!)
Random fun facts about cats displayed
## Example 3: Cloud Message Board

This example implements a cloud-based message board using Django. Users can:
1. Submit messages with sender and recipient names.
2. Retrieve the latest 20 messages sent by a specific sender.

### Key Features:
- **Models:** A `Message` model is used to store messages with fields for sender, recipient, message content, and timestamp.
- **Views:**
  - `submit_message`: Accepts POST requests to save messages in the database.
  - `get_messages`: Retrieves the latest 20 messages for a given sender.
- **Dynamic Rendering:** Uses Django templates for the main interface.

### How to Run:
1. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   start the server
   Open the browser at http://127.0.0.1:8000/messageboard/.

## Example 4: Django Response Types

This example demonstrates various Django response types:
- **HttpResponse**: Text response.
- **FileResponse**: Serving files (image, PDF, and video).

### How to Test
1. Run the Django development server:
   ```bash
   python manage.py runserver
   Open these URLs in the browser:
 
   Text Response: http://127.0.0.1:8000/responses/text/
   HTML Response: http://127.0.0.1:8000/responses/html/
   JSON Response: http://127.0.0.1:8000/responses/json/
   Streaming Response: http://127.0.0.1:8000/responses/stream/
   Text File Response: http://127.0.0.1:8000/responses/textfile/
   Image Response: http://127.0.0.1:8000/responses/image/
   PDF Response: http://127.0.0.1:8000/responses/pdf/
   Video Response: http://127.0.0.1:8000/responses/video/
   CSV Response: http://127.0.0.1:8000/responses/csv/
   XML Response: http://127.0.0.1:8000/responses/xml/
## there's also a pdf report that includes the screenshots, analysis and comments about this project!
