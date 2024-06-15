# MailMaster

MailMaster is a Django-based application designed for sending and scheduling emails using Celery. This project includes features such as email templates, scheduling, and efficient management of email tasks.

## Features

- **Email Templates**: Create and manage reusable email templates.
- **Scheduling**: Schedule emails to be sent at a later time.
- **Task Management**: Efficiently handle email sending tasks using Celery.

## Installation

To get started with the MailMaster project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/onurcatik/MailMaster.git
    cd mailmaster
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Node.js dependencies:**
    ```bash
    npm install
    ```

5. **Run the Tailwind installation script:**
    ```bash
    ./install-tailwind.sh
    ```

6. **Configure the `.env` file:**

   Create a `.env` file in the root directory of the project and configure the necessary environment variables. Here is an example of what might be included:
    ```env
    DEBUG=True
    SECRET_KEY=your_secret_key
    EMAIL_HOST=smtp.your-email-provider.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=your_email@example.com
    EMAIL_HOST_PASSWORD=your_password
    CELERY_BROKER_URL=redis://localhost:6379/0
    ```

   Make sure to replace `your_secret_key`, `your-email-provider.com`, `your_email@example.com`, and `your_password` with your actual values.

7. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

8. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

To use MailMaster, follow these steps:

1. **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```

2. **Start the Redis server:**
    ```bash
    redis-server
    ```

3. **Start the Celery worker:**
    ```bash
    celery -A MailMaster worker --loglevel=info
    ```

Navigate to the web interface at `http://127.0.0.1:8000/` and use the provided features to create and schedule email campaigns.

