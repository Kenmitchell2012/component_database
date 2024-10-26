# Component Database

A Django-based application for managing and tracking components, including features for adding, updating, deleting, and searching components.

## Features

- **List Components**: View a list of all components with their details.
- **Add Components**: Easily add new components to the database.
- **Update Components**: Modify existing component details.
- **Delete Components**: Remove components from the database.
- **Search Functionality**: Implement AJAX-based search for quick access to components by name, lot number, or part number.
- **Responsive Design**: The application is designed to be user-friendly across various devices.

## Technologies Used

- **Django**: Web framework for building the application.
- **HTML/CSS**: For the frontend.
- **AJAX**: For dynamic searching and updating of component lists.

## Installation

### Prerequisites

- Python 3.x
- Django

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/component-database.git
   cd component-database
   ```

2. **Install Dependencies**:

   Create a virtual environment and install Django:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install django
   ```

3. **Run Migrations**:

   Initialize the database:

   ```bash
   python manage.py migrate
   ```

4. **Create a Superuser** (optional, for admin access):

   ```bash
   python manage.py createsuperuser
   ```

5. **Start the Development Server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the App**:

   Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- Navigate to the main page to view the list of components.
- Use the search bar to filter components by name, lot number, or part number.
- Click on the "Add Component" button to add a new component.
- Use the edit and delete options available for each component to manage your entries.

## AJAX Search

The app features an AJAX search function that allows users to filter components without refreshing the page. The search results will update dynamically based on user input.

