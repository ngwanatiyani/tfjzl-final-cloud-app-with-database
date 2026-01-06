# Online Course Platform

This is a Django-based web application designed to manage and deliver online courses. It provides a platform for instructors to create courses and lessons, and for students to enroll, take exams, and track their progress.

## Features

*   **Course Management:** Browse a list of available courses with detailed descriptions and instructor information.
*   **Lesson Delivery:** Structured lessons associated with each course.
*   **User Enrollment:** Students can enroll in courses to access content.
*   **Exam System:**
    *   Multiple-choice questions linked to courses.
    *   Automated submission and grading process.
*   **Results:** Instant feedback on exam submissions.

## Tech Stack

*   **Backend:** Python, Django
*   **Frontend:** HTML, Bootstrap
*   **Database:** SQLite (default Django setup)

## Key Models

The application is built around the following data models:
*   `Course` & `Lesson`: Core content structures.
*   `Instructor`: Linked to courses.
*   `Enrollment`: Tracks student participation.
*   `Question` & `Choice`: Components of the assessment system.
*   `Submission`: Records student exam attempts.

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ngwanatiyani/tfjzl-final-cloud-app-with-database.git
    cd tfjzl-final-cloud-app-with-database
    ```

2.  **Install Dependencies:**
    Ensure you have Django installed.
    ```bash
    pip install django
    ```

3.  **Database Setup:**
    Run migrations to create the database schema.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Create Admin User:**
    Access the admin dashboard to manage courses and questions.
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the Server:**
    Start the development server.
    ```bash
    python manage.py runserver
    ```

6.  **Access the App:**
    Open your browser and navigate to `http://127.0.0.1:8000/`.