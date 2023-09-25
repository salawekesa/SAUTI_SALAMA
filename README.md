# SAUTI_SALAMA

SAUTI SALAMA is a Django web application designed to address and manage cases of Sexual and Gender-Based Violence (SGBV). The app provides a platform for reporting SGBV incidents, accessing legal counsel, and connecting with mental health practitioners.

## Getting Started

Follow these instructions to set up and run the SAUTI SALAMA Django app on your local machine for development and testing purposes.

### Prerequisites

- Python (3.x)
- Django (4.x)
- [Other dependencies]

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sauti_salama.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sauti_salama
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

9. Access the application in your web browser at `http://localhost:8000`.

### Usage

- SAUTI SALAMA is designed to address and manage cases of Sexual and Gender-Based Violence (SGBV). It provides different user roles, including SGBV survivors, legal counsel, and mental health practitioners, with access to specific views and functionalities.

- The admin panel at `http://localhost:8000/admin/` allows administrators to manage users, reports, and other app data. Use the superuser credentials created in step 7 to access this panel.

- Create user accounts through the admin panel and assign the appropriate role (SGBV survivor, legal counsel, or mental health practitioner) to each user.

### Screenshots

[Insert screenshots of your app here]

## Contributing

[Explain how others can contribute to your project, if applicable]

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [Acknowledgments, if any]

```

This updated README provides a clear explanation that the SAUTI SALAMA app is specifically designed to address and manage cases of Sexual and Gender-Based Violence (SGBV).
