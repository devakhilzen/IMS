##  Inventory Management System (IMS)

The Inventory Management System (IMS) is a cloud-native application designed to manage inventory efficiently. It consists of a backend built with FastAPI, a frontend developed using Streamlit, and a MongoDB Atlas database. The application is containerized using Docker and deployed on Kubernetes clusters with disaster recovery capabilities.

## Features

Add, Update, and Delete Inventory Items

User Management

Transaction Management

Disaster Recovery using Velero

High Availability with Multi-Cluster Setup


## Architecture

Frontend: Streamlit for a user-friendly interface.

Backend: FastAPI for API endpoints.

Database: MongoDB Atlas for inventory, user, and transaction data.

Kubernetes: Deployment with primary and secondary clusters.

Disaster Recovery: Velero for backup and restore functionality.

## Prerequisites

Docker

Kubernetes Cluster (Primary and Secondary)

Velero

Git

MongoDB Atlas

## CI/CD Pipeline

** Stages **

Deploy Application to Primary Cluster

Trigger Velero Backup

Simulate Disaster and Failover to Secondary Cluster

Validate Application Functionality Post-Recovery