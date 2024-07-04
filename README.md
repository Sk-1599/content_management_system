# Django CMS Project

This is a Django-based Content Management System (CMS) with APIs for user roles (admin and author) and content management.

## Setup

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework
- Coverage.py

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/cms_project.git
    cd cms_project
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (admin):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

### Running Tests

To run the tests and generate a coverage report:

1. Run the tests with coverage:

    ```bash
    coverage run --source='.' manage.py test
    ```

2. Generate the HTML coverage report:

    ```bash
    coverage html
    ```

3. Open `htmlcov/index.html` to view the coverage report.

### API Endpoints

- **User registration**: `/api/users/`
- **User login**: `/api/auth/login/`
- **Content management**: `/api/contents/`
- **Categories management**: `/api/categories/`

### Code Coverage

The code coverage report is included in the `htmlcov` directory. It provides insights into how much of the code is covered by the tests. 

### Directory Structure

    cms_project/
    ├── cms_app/
    │   ├── migrations/
    │   ├── templates/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── cms_project/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── requirements.txt
    └── README.md
