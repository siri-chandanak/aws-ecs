from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
)
from constructs import Construct

class EcsFargateStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, "MyVpc", max_azs=2)

        # Create ECS Cluster
        cluster = ecs.Cluster(self, "MyCluster", vpc=vpc)

        # Fargate Service with Application Load Balancer
        ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "MyFargateService",
            cluster=cluster,
            cpu=512,
            memory_limit_mib=1024,
            desired_count=2,
            #task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
            #    image=ecs.ContainerImage.from_registry(
            #        "079910999118.dkr.ecr.us-east-1.amazonaws.com/python_flask:v0.1"
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry(
                    "siri019/python_flask:v0.1"
                ),
                container_port=5000,
                enable_logging=True,
            ),
            public_load_balancer=True
        )
        #  AutoScaling can be added here if needed
        #  service.auto_scale_task_count(
        #      min_capacity=2,
        #      max_capacity=4
        #  ).scale_on_cpu_utilization(
        #      "CpuScaling",
        #      target_utilization_percent=50
        #  )
