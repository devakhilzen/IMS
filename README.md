##   Kubernetes Disaster Recovery System with Velero and CI/CD Pipeline

The Kubernetes Application Disaster Recovery System is designed to ensure high availability and fault tolerance for applications running on Kubernetes. This system automates backups, enables failover, and ensures that applications and their associated data can recover seamlessly during outages or disasters. The project involves using tools like Velero for backup/restore, Terraform for infrastructure provisioning, and CI/CD pipelines for automated testing and validation.

## Features

- Automated deployment of Kubernetes resources.
- Integration with **Velero** for disaster recovery.
- Chaos testing with **Chaos Mesh** for simulating disaster scenarios.
- Validation of application health after failover.
- Environment-specific configurations using `envsubst`.
- Multi-cluster failover setup.


## Prerequisites

- [GitLab](https://about.gitlab.com/) for CI/CD.
- [Google Cloud SDK](https://cloud.google.com/sdk) installed locally.
- Kubernetes clusters (Primary and Secondary) set up in **GKE**.
- Velero installed on both clusters.
- Helm package manager.
- A service account key for authentication (`AUTH_GITLAB` and `VELERO_AUTH`).

## CI/CD Pipeline

** Stages **

Deploy Application to Primary Cluster

Trigger Velero Backup

Simulate Disaster and Failover to Secondary Cluster

Validate Application Functionality Post-Recovery
