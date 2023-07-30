# Use the official Python image as the base image
FROM python:3.10-slim

# Environment variables
ENV AIRFLOW_HOME=/usr/local/airflow
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    python-dev-is-python3 \
    && rm -rf /var/lib/apt/lists/*


# Create the AIRFLOW_HOME directory
RUN mkdir -p $AIRFLOW_HOME
WORKDIR $AIRFLOW_HOME

# Install required packages
COPY requirements.txt requirements.txt

RUN pip install apache-airflow
RUN pip install -r requirements.txt

# Initialize the Airflow database
RUN airflow db init

# Expose the Airflow web server port
EXPOSE 8080

# Copy necessary files into the container
COPY data data
COPY dags $AIRFLOW_HOME/dags
COPY src $AIRFLOW_HOME/src

# Create a default user
RUN airflow users create \
    --username admin \
    --firstname Default \
    --lastname User \
    --role Admin \
    --email default_user@example.com \
    --password admin || echo "User 'admin' already exists. Skipping user creation."

# Start the Airflow scheduler and web server
CMD ["bash", "-c", "airflow scheduler & airflow webserver -p 8080"]