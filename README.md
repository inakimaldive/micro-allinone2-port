# Micro-Allinone2-Port: A Flask-Based Micro-Blogging Platform

This project is a lightweight and straightforward micro-blogging platform built with Flask. It's designed for easy deployment on Vercel and uses a simple file-based approach for managing blog posts.

## Features

*   **Flask-Powered:** A robust and popular micro-framework for Python.
*   **Markdown-Based Content:** Blog posts are written in Markdown, making them easy to create and edit.
*   **Dynamic Post Listing:** The homepage automatically lists all available blog posts, sorted by date.
*   **Vercel-Ready:** Includes a `vercel.json` file for seamless deployment to the Vercel platform.
*   **Automated Content Creation:** A GitHub Actions workflow can be triggered to automatically create new, dated Markdown files for blog posts.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.12 or higher
*   pip for installing Python packages

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/inakimaldive/micro-allinone2-port.git
    cd micro-allinone2-port
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv myenv
    source myenv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

The `start.sh` script is provided to simplify the process of running the application. It will automatically handle any conflicting processes on port 5000, activate the virtual environment, and start the Flask development server.

```bash
./start.sh
```

The application will be available at `http://127.0.0.1:5000`.

## Deployment

This project is configured for easy deployment to [Vercel](https://vercel.com/). The `vercel.json` file contains the necessary rewrite rules to ensure that all incoming requests are correctly routed to the Flask application.

## API Endpoints

*   `GET /`: The main page, which displays a list of all blog posts.
*   `GET /post/<filename>`: Displays a single blog post. The `<filename>` should be the name of the Markdown file in the `contents` directory (e.g., `2025-07-21-11-10-49.md`).
*   `POST /trigger`: A webhook endpoint that triggers a GitHub Actions workflow to create a new, dated Markdown file in the `contents` directory.

## Content Management

To add a new blog post, simply create a new Markdown file in the `contents` directory. The filename should follow the format `YYYY-MM-DD-HH-MM-SS.md`. The title of the post is derived from the filename.

## GitHub Actions Integration

The project includes a GitHub Actions workflow defined in `.github/workflows/create-file.yml`. This workflow is triggered by a `repository_dispatch` event with the `event_type` of `create-dated-file`. When triggered, it creates a new Markdown file in the `contents` directory with the current date and time as the filename.

The `POST /trigger` endpoint can be used to trigger this workflow. You will need to provide a GitHub personal access token with the `repo` scope as the `GHTOKEN` environment variable for the request to be authenticated.