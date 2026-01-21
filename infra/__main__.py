# import pulumi
# from pulumi_kubernetes.apps.v1 import Deployment
# from pulumi_kubernetes.core.v1 import Service

# labels = {"app": "pulumi-demo"}

# Deployment(
#     "demo-app",
#     spec={
#         "replicas": 1,
#         "selector": {"matchLabels": labels},
#         "template": {
#             "metadata": {"labels": labels},
#             "spec": {
#                 "containers": [{
#                     "name": "app",
#                     "image": "pulumi-demo:latest",
#                     "ports": [{"containerPort": 5000}]
#                 }]
#             }
#         }
#     }
# )

# Service(
#     "demo-svc",
#     spec={
#         "type": "NodePort",
#         "selector": labels,
#         "ports": [{"port": 80, "targetPort": 5000}]
#     }
# )
import pulumi
from pulumi_kubernetes.core.v1 import Namespace

Namespace("demo-ns")
