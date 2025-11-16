# Dokku FastAPI React

This is a template for a FastAPI backend and a React frontend, configured for deployment on Dokku.

## Local Development

### Backend

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the backend server:
    ```bash
    uvicorn main:app --reload
    ```
    The backend will be running at `http://localhost:8000`.

### Frontend

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Run the frontend development server:
    ```bash
    npm start
    ```
    The frontend will be running at `http://localhost:3000`.

## Dokku Deployment

1.  Create a Dokku app:
    ```bash
    ssh dokku@{HOST-SERVER-IP-OR-DOMAIN} -i {PATH-TO-SSH-FILE} apps:create my-app
    ```
2.  Add a remote for your Dokku server:
    ```bash
    git remote add dokku dokku@{HOST-SERVER-IP-OR-DOMAIN}:my-app
    ```
3.  Push to deploy:
    ```bash
    git push dokku main
    ```