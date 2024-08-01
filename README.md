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

3. **Create Topic SNS**:

    In AWS, create a topic

4. **Configure variable**
 Use the file envExample, create .env file and put the values of each variable:

    ```bash
    poetry install
    ```

5. **Apply migrations**:

    ```bash
    poetry run python manage.py migrate
    ```

6. **Create a superuser** (for Django admin):

    ```bash
    poetry run python manage.py createsuperuser
    ```

7. **Run the development server**:

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


6. **Access to AWS**:

    - Install aws cli
    
    - After configure the aws cli with these command:

    ```bash
    aws configure
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


## Contact

For questions or issues, please contact [yazanenator@gmail.com](mailto:yazanenator@gmail.com).

### Presentation of project

    ```bash
    https://docs.google.com/presentation/d/1jw5r4SSRENpjsEJjc_IFpAhqg4kaQrg4jporqiLqlZc/edit?hl=es#slide=id.g2efb191e0f4_0_40
    ```



