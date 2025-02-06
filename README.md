# Airflow Deployment on AWS EC2

## Project Overview

This project involves setting up an Airflow service on an Amazon Web Services (AWS) EC2 instance. The goal was to automate the deployment of Airflow Directed Acyclic Graphs (DAGs) using GitHub Actions, and to ensure reliable execution within the deployment environment.

## Key Features

- **Airflow Service Setup**: Configured and established Airflow on an AWS EC2 instance.
- **CI/CD Integration**: Implemented GitHub Actions to automate the deployment of Airflow DAGs to the Airflow server.
- **Execution Verification**: Verified the proper execution of DAGs in the deployment environment, ensuring operational integrity and performance.

## Deployment Process

1. **Setting Up AWS EC2**: Provisioned an EC2 instance suitable for hosting the Airflow service.
2. **Airflow Installation**: Installed and configured Airflow on the EC2 instance, setting up necessary dependencies and environment variables.
3. **GitHub Actions Workflow**: Developed a GitHub Actions workflow that automatically deploys newly pushed DAGs to the Airflow server.
4. **Verification**: Conducted tests to confirm that DAGs execute correctly post-deployment, monitoring performance and troubleshooting issues as needed.

## Conclusion

This project successfully demonstrates the capability to automate the deployment and management of Airflow workflows using GitHub Actions, facilitating continuous integration and deployment in a cloud environment.
