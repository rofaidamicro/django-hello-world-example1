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
   git clone https://github.com/rofaidamicro/django-hello-world-example1.git
2. Navigate to the project directory: cd django-hello-world-example1
3. Install dependencies: Make sure you have Python and Django installed. If not, create a virtual environment and install Django: python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install django 
4. Run the development server: python manage.py runserver
5. Open the application in your browser
 # Technologies Used
Python: Backend programming.
Django: Framework for building the web application.
HTML, CSS, JavaScript: Frontend for designing the webpage.


## Example 2: Improved Django Page with MVT Pattern
This example builds on Example 1 by introducing the Model-View-Template (MVT) pattern. It includes animations, theme switching, and a fun cat gallery.

Features:

Dynamic animations and theme switching
Cat gallery with hover effects
Random fun facts about cats displayed dynamically
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


