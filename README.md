# entrapeer-solution

---

## Step 1: Install Prerequites

Make sure you have the following installed on your system:

- [Install](https://www.python.org/downloads/) Python 3.8 or higher.
- [Install](https://www.docker.com/products/docker-desktop/) Docker.

---

**In the terminal navigate to the root directory of the repository.**

## Step2: Create airflow docker image using the command below.

```
docker build . -t airflow
```

<details>
  <summary>Step Notes</summary>
  
  - **An admin airflow user is created by default. It is added for convenience of testing. It should be excluded from the Dockerfile in production environments.**

</details>
