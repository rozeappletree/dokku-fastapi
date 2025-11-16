# Dokku FastAPI React

This is a template for a FastAPI backend and a React frontend, configured for deployment on Dokku.


**Status:** 🟢 working as of 16/11/2025 _(send PR with new date if it works for you today!)_

Before deploying (your commit with gh actions), make sure you 

- Change the host and ssh key values in gh secrets
- Change the app name
- Install dokku in the server and set it up [(see here)](https://dokku.com/docs/getting-started/installation/).
    
    ```bash
    # As of 16/11/2025
    # ----

    sudo apt update && sudo apt upgrade

    wget -NP . https://dokku.com/install/v0.36.10/bootstrap.sh
    sudo DOKKU_TAG=v0.36.10 bash bootstrap.sh

    cat ~/.ssh/authorized_keys | sudo dokku ssh-keys:add admin
    ```

    ```bash
    # you can use any domain you already have access to
    # this domain should have an A record or CNAME pointing at your server's IP
    dokku domains:set-global {your-domain-here-which-maps-to-ip}
    ```

    ```
    # SSL
    dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git
    dokku letsencrypt:set --global email rozeappletree.dev@gmail.com
    dokku letsencrypt:cron-job --add
    ```


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
    ssh dokku@{HOST-SERVER-IP-OR-DOMAIN} -i {PATH-TO-SERVER-SSH-FILE} apps:create my-app
    ```
2.  Add a remote for your Dokku server:
    ```bash
    git remote add dokku dokku@{HOST-SERVER-IP-OR-DOMAIN}:my-app
    ```
3.  Push to deploy:
    ```bash
    eval "$(ssh-agent -s)" && ssh-add {PATH-TO-SERVER-SSH-FILE}
    git push dokku main
    ```

# CI/CD

Uses https://github.com/dokku/github-action
