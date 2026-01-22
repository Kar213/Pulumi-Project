import pulumi
from pulumi_kubernetes.core.v1 import Namespace, Service
from pulumi_kubernetes.apps.v1 import Deployment

# Create Namespace
ns = Namespace(
    "demo-ns",
    metadata={
        "name": "demo-ns"
    }
)

labels = {
    "app": "pulumi-demo"
}

# Deployment
Deployment(
    "pulumi-demo-deployment",
    metadata={
        "namespace": ns.metadata["name"]
    },
    spec={
        "replicas": 1,
        "selector": {
            "matchLabels": labels
        },
        "template": {
            "metadata": {
                "labels": labels
            },
            "spec": {
                "containers": [
                    {
                        "name": "app",
                        "image": "pulumi-demo:latest",

                        # 🔴 THIS LINE FIXES ImagePullBackOff
                        "imagePullPolicy": "IfNotPresent",

                        "ports": [
                            {"containerPort": 5000}
                        ]
                    }
                ]
            }
        }
    }
)

# Service
Service(
    "pulumi-demo-service",
    metadata={
        "namespace": ns.metadata["name"]
    },
    spec={
        "type": "NodePort",
        "selector": labels,
        "ports": [
            {
                "port": 80,
                "targetPort": 5000
            }
        ]
    }
)
