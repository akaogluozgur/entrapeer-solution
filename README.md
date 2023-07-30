# entrapeer-solution

## Step 1: Install Prerequites

Make sure you have the following installed on your system:

-   [Install](https://www.python.org/downloads/) Python 3.10 or higher.
-   [Install](https://www.docker.com/products/docker-desktop/) Docker.
-   Manually [install](https://www.kaggle.com/datasets/justinas/startup-investments) startup investment data from the link & extract the content of the **arhieve.zip** to the folder named **data/startup-investments**.

```
pip install -r requirements.txt
```

<details>
  <summary>or Download the data via setup.py by providing your Kaggle api token.</summary>

-   Login to your Kaggle Account.
-   Locate your username and api key. Credentials can be obtained from [account settings](https://www.kaggle.com/settings)

```
pip install -r requirements.txt
python setup.py
```

-   Enter the credentials from terminal.

</details>

---

**In the terminal navigate to the root directory of the repository.**

## Step 2: Create airflow docker image using the command below.

```
docker build . -t airflow
```

<details>
  <summary>Step Notes</summary>

-   This step might take some time on the first run depending on the existing python packages in the system.

-   **An admin airflow user is created by default. It is added for convenience of testing. It should be excluded from the Dockerfile in production environments.**

</details>

## Step 3: Create the mongodb images & run alongside with airflow using docker compose.

```
docker-compose -f docker-compose.yml up
```

<details>
  <summary>Step Notes</summary>

-   You can reach Airflow webserver at: http://localhost:8080. Login to the default account. (Username: admin, Password: admin)
-   You can reach mongodb instance at: http://localhost:8081.
</details>

## Additional Steps

Navigate root directory of the repo via terminal.

-   You can check the compliance of the google python code style by

```
pylint setup.py
pylint dags
pylint src
```

-   You can see test coverage using

```
coverage run -m pytest
coverage report --fail-under=100
```
