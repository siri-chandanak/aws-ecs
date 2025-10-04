# Containerized Application Deployment on AWS ECS with Fargate

This project demonstrates how to deploy a containerized Python Flask application on AWS ECS using Fargate. The deployment is automated using GitHub Actions and AWS CDK.

## Features

- Dockerized Flask app for portability and consistency
- AWS ECS Fargate for serverless container orchestration
- Infrastructure as Code (IaC) using AWS CDK (Python)
- Application Load Balancer (ALB) for traffic routing
- CloudWatch Monitoring for logs and metrics
- Auto Scaling based on CPU utilization
- CI/CD with GitHub Actions (Builds & pushes Docker image to DockerHub + ECR. Deploys ECS Fargate service via CDK)

## Tech Stack
- AWS ECS (Fargate) – Serverless container orchestration
- AWS CDK (Python) – Infrastructure as Code
- Docker – Containerization
- Flask – Python web application framework
- Amazon ECR – Container registry (backup copy of images)
- DockerHub – Primary registry for ECS task definition
- GitHub Actions – CI/CD automation
- CloudWatch – Logging & monitoring

## Project Structure

```
/aws-ecs
|-- .github
|   |-- workflows
|   |   |-- ecs_deploy.yml
|-- app
|   |-- app.py
|-- cdk
|   |-- cdk
|   |   |-- cdk_stack.py
|   |-- requirements.txt
|-- Dockerfile
|-- README.md
``` 

## Setup & Deployment

### 1. Prerequisites
- AWS Account with ECS, ECR, and IAM permissions
- Docker installed locally
- AWS CDK installed (npm install -g aws-cdk)
- GitHub repository with Secrets configured: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DOCKERHUB_USERNAME, DOCKERHUB_TOKEN

### 2. Local Deployment
1. Clone the repository:
   ```bash
   git clone https://github.com/siri-chandanak/aws-ecs.git
   cd aws-ecs
   ```
2. Build the Docker image:
   ```bash
   docker build -t siri019/aws-ecs:latest .
   ```
3. Run the Docker container locally:
   ```bash
   docker run -p 5000:5000 siri019/aws-ecs:latest
   ```  
4. Access the application at `http://localhost:5000`

### 3. AWS CDK Deployment
1. Navigate to the CDK directory:
   ```bash
   cd cdk
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Bootstrap the CDK environment:
   ```bash
   cdk bootstrap
   ```
4. Deploy the CDK stack:
   ```bash
   cdk deploy
   ```  
5. Access the application using the Load Balancer DNS output from the CDK deployment.

### 4. CI/CD with GitHub Actions
- The GitHub Actions workflow (`.github/workflows/ecs_deploy.yml`) automates the following on every push to the `main` branch:
  1. Build and push the Docker image to DockerHub and ECR.
  2. Deploy the updated ECS Fargate service using AWS CDK.

## Monitoring & Scaling
- The application is monitored using CloudWatch Logs and Metrics.
- Auto Scaling is configured to adjust the number of running tasks based on CPU utilization.

## Cleanup
To avoid incurring charges, remember to delete the AWS resources created by this project when they are no longer needed:
```bash
cdk destroy
```

## Future Enhancements
- Implement HTTPS using AWS Certificate Manager and ALB
- Add a database backend (e.g., RDS or DynamoDB)
- Implement blue/green deployments for zero-downtime updates

## Demo

- **Docker image build:**
    ```bash
    docker build -t siri019/aws-ecs:latest .
    ```

- **Running image in localhost:**
    ```bash
    docker run -p 5000:5000 siri019/aws-ecs:latest
    ```
  <img src="/Screenshots/local_cmd.png" alt="Alt Text" width="500" height="500">
  <img src="/Screenshots/local_app.png" alt="Alt Text" width="500" height="500">

- **Pushing image to DockerHub: Optional step if you want to keep a backup copy of your image**
    ```bash
    docker login
    docker push siri019/aws-ecs:latest
    ```

- **AWS account setup:**
    ```bash
    aws configure
    ```

- **Upload to ECR using following command:**
    ```bash
    aws ecr create-repository --repository-name python_flask
    aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
    docker tag python_flask:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/python_flask:latest
    docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/python_flask:latest
    ```
- **CDK deploy:**
<img src="/Screenshots/image.png" alt="Alt Text" width="500" height="500">
You can use the image stored in ECR or DockerHub in your CDK stack. Make sure to update the image URL in `cdk_stack.py` accordingly.
    ```bash
    cdk bootstrap
    cdk deploy
    ```
<img src="/Screenshots/cdk.png" alt="Alt Text" width="500" height="500">

- **Accessing the application using Load Balancer DNS:**
<img src="/Screenshots/lb_app.png" alt="Alt Text" width="500" height="500">

- **Monitoring the application using CloudWatch:**
<img src="/Screenshots/cloudWatch.png" alt="Alt Text" width="500" height="500">

- **CI/CD using GitHub Actions:**
The GitHub Actions workflow will automatically build and push the Docker image to DockerHub and ECR, and deploy the updated ECS Fargate service using AWS CDK on every push to the `main` branch.

Make sure to set the following secrets in your GitHub repository:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `DOCKERHUB_USERNAME`
  - `DOCKERHUB_TOKEN`
You can set secrets in your GitHub repository by navigating to `Settings` > `Secrets and variables` > `Actions` > `New repository secret`.

The `ecs_deploy.yml` file is located in `.github/workflows/ecs_deploy.yml` helps to automate the deployment process.
Workflow:
- Trigger: On push to the `main` branch.
- Jobs:
  - `build_and_push`: Builds the Docker image and pushes it to DockerHub and ECR.
  - `deploy`: Deploys the ECS Fargate service using AWS CDK.
- Ensure that the image URL in `cdk_stack.py` matches the image you pushed to DockerHub or ECR.
In Github, navigate to the `Actions` tab to monitor the workflow runs and check for any errors or issues.
<img src="/Screenshots/git.png" alt="Alt Text" width="500" height="500">

After the workflow completes successfully, your application will be deployed and accessible via the Load Balancer DNS.

<img src="/Screenshots/app2.png" alt="Alt Text" width="500" height="500">

If you don't want run pipeline on every push to main branch, you can add ""[skip ci]"" in your commit message. This will prevent the GitHub Actions workflow from being triggered for that specific commit.

## Summary
This project provides a comprehensive example of deploying a containerized Python Flask application on AWS ECS using Fargate. It covers everything from Dockerization to infrastructure provisioning with AWS CDK, and CI/CD automation with GitHub Actions. You can further enhance this project by adding features like HTTPS, database integration, and advanced deployment strategies.
