# entrapeer-solution

---

## Step 1: Install Prerequites

Make sure you have the following installed on your system:

- [Install](https://www.python.org/downloads/) Python 3.10 or higher.
- [Install](https://www.docker.com/products/docker-desktop/) Docker.

---

**In the terminal navigate to the root directory of the repository.**

## Step 2: Create airflow docker image using the command below.

```
docker build . -t airflow
```

<details>
  <summary>Step Notes</summary>

- This step might take some time on the first run depending on the existing python packages in the system.

- **An admin airflow user is created by default. It is added for convenience of testing. It should be excluded from the Dockerfile in production environments.**

</details>

## Step 3: Create the mongodb images & run alongside with airflow using docker compose.

```
docker-compose -f docker-compose.yml up
```
