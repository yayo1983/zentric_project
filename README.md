# Django RESTful Project

## Overview

This project is a Django-based RESTful application with the following features:

- **Applications**:
  - `inventories`: Manage inventory transactions and products.
  - `notifications`: Handle user notifications.
  - `tickets`: Manage ticketing system.
  - `products`: Manage product information.
  - `shareds`: Shared utilities and base views.

- **Testing**: Unit and integration tests are included for each application.
- **Deployment**: Configured to run with Docker, Docker Compose, and Kubernetes.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Kubernetes](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Poetry](https://python-poetry.org/docs/#installation) (for dependency management)

## Installation

### Setting Up the Development Environment

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yayo1983/zentric_project.git
    cd zentric_project
    ```

2. **Install dependencies**:

    Use Poetry to install Python dependencies:

    ```bash
    poetry install
    ```

3. **Apply migrations**:

    ```bash
    poetry run python manage.py migrate
    ```

4. **Create a superuser** (for Django admin):

    ```bash
    poetry run python manage.py createsuperuser
    ```

5. **Run the development server**:

    ```bash
    poetry run python manage.py runserver
    ```

### Running with Docker and Docker Compose

1. **Build and start containers**:

    ```bash
    docker-compose up --build
    ```

2. **Access the application**:

    The application will be available at `http://localhost:8000`.

3. **Run database migrations in Docker**:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

4. **Create a superuser in Docker**:

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

### Running with Kubernetes

1. **Build Docker images**:

    ```bash
    docker build -t myproject:latest .
    ```

2. **Push Docker images to a registry** (optional):

    ```bash
    docker tag myproject:latest <your-registry>/myproject:latest
    docker push <your-registry>/myproject:latest
    ```

3. **Apply Kubernetes manifests**:

    Ensure you have Kubernetes configured. Apply the manifests:

    ```bash
    kubectl apply -f k8s/
    ```

4. **Check Kubernetes pods**:

    ```bash
    kubectl get pods
    ```

5. **Access the application**:

    Set up port forwarding or use a LoadBalancer service as per your configuration:

    ```bash
    kubectl port-forward svc/myproject-service 8000:80
    ```

    The application will be available at `http://localhost:8000`.

## Testing

### Running Unit and Integration Tests

1. **Run tests with Poetry**:

    ```bash
    poetry run python manage.py test
    ```

2. **Run tests with Docker**:

    ```bash
    docker-compose exec web python manage.py test
    ```

## Project Structure

- `inventories/`: Application for managing inventory transactions.
- `notifications/`: Application for managing notifications.
- `tickets/`: Application for managing tickets.
- `products/`: Application for managing product information.
- `shareds/`: Shared utilities and base views.

## Contributing

1. **Fork the repository**.
2. **Create a feature branch**.
3. **Commit your changes**.
4. **Push to the branch**.
5. **Open a pull request**.


## Contact

For questions or issues, please contact [yazanenator@gmail.com](mailto:yazanenator@gmail.com).

