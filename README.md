# 📚 Bookstore API – Cloud-Native Deployment

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![MongoDB](https://img.shields.io/badge/Azure%20CosmosDB-MongoAPI-green?logo=mongodb)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/AKS-Deployed-326ce5?logo=kubernetes)
![Azure](https://img.shields.io/badge/Cloud-Microsoft%20Azure-0089D6?logo=microsoftazure)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A **cloud-native Bookstore application** that demonstrates how to integrate:

* 📦 **Flask + MongoDB (CosmosDB API)**
* 🐳 **Containerization with Docker**
* ☸️ **Orchestration with Azure Kubernetes Service (AKS)**
* 🔐 **Service Discovery & Networking Policies**

---

## 📑 Table of Contents

* [✨ Features](#-features)
* [🛠 Technologies Used](#-technologies-used)
* [🏗️ Architecture](#️-architecture)
* [📂 Project Structure](#-project-structure)
* [🚀 Getting Started](#-getting-started)

  * [⚡ Prerequisites](#-prerequisites)
  * [📥 Installation](#-installation)
* [▶️ Usage](#️-usage)

  * [💻 Running Locally](#-running-locally)
  * [🌐 API Endpoints](#-api-endpoints)
* [☸️ Cloud Deployment](#️-cloud-deployment)

  * [1️⃣ Task-1: Setup MongoDB on Azure](#1️⃣-task-1-setup-mongodb-on-azure)
  * [2️⃣ Task-2: Python Application](#2️⃣-task-2-python-application)
  * [3️⃣ Task-3: Azure Kubernetes Service (aks)](#3️⃣-task-3-azure-kubernetes-service-aks)
  * [4️⃣ Task-4: Python Application Deployment](#4️⃣-task-4-python-application-deployment)
  * [5️⃣ Task-5: Service Discovery & Networking](#5️⃣-task-5-service-discovery--networking)

---

## ✨ Features

* ⚙️ **RESTful API** for book management.
* 📚 **CRUD Operations** with endpoints for retrieving, adding, updating, and deleting books.
* 🖥 **Web UI** for retrieving book details by ISBN.
* ☁️ **Azure-Integrated** using Cosmos DB (Mongo API) and Azure Container Registry (ACR).
* 🐳 **Dockerized Application** for portability.
* ☸️ **Deployed on AKS** with scalability (replicas).
* 🔐 **Secure Networking** with Kubernetes Network Policies and service discovery.

---

## 🛠 Technologies Used

* **Backend:** 🐍 Python (Flask)
* **Database:** 🍃 Azure Cosmos DB (Mongo API)
* **Containerization:** 🐳 Docker
* **Orchestration:** ☸️ Azure Kubernetes Service (AKS)
* **Registry:** 📦 Azure Container Registry (ACR)
* **Networking & Security:** 🔐 Kubernetes Network Policies
* **Frontend:** 🌐 HTML, CSS, JavaScript
* **Server:** 🔥 Gunicorn

---

## 🏗️ Architecture  


---

## 📂 Project Structure

```bash
.
├── app.py                 # Flask API logic
├── index.html             # Web UI
├── requirements.txt       # Python dependencies
├── Dockerfile             # Build instructions
├── gunicorn.conf.py       # WSGI config
├── bookstore.json         # Sample data
├── .dockerignore
├── app-deployment.yaml    # Flask app deployment
├── app-service.yaml       # Flask app service
├── app-configmap.yaml     # Optional ConfigMap
├── mongodb-deployment.yaml
├── mongodb-service.yaml
├── network-policy.yaml    # Security & networking
└── Report.pdf             # Project documentation
```

---

## 🚀 Getting Started

### ⚡ Prerequisites

* Python 3.11+
* Docker
* `kubectl` & Azure CLI
* Azure subscription (with student credits)
* MongoDB Compass (for DB access)

### 📥 Installation

```sh
git clone https://github.com/Briksam/Cloud.git
cd Cloud
pip install -r requirements.txt
```

---

## ▶️ Usage

### 💻 Running Locally

```sh
docker build -t flask-mongo-app .
docker run -p 5005:5005 flask-mongo-app
```

👉 Accessible at: `http://localhost:5005`

### 🌐 API Endpoints

| Method | Endpoint            | Description          |
| ------ | ------------------- | -------------------- |
| GET    | `/api/allbooks`     | Fetch all books      |
| GET    | `/api/books/<isbn>` | Fetch a book by ISBN |
| POST   | `/api/books`        | Add a new book       |
| PUT    | `/api/books/<isbn>` | Update a book        |
| DELETE | `/api/books/<isbn>` | Delete a book        |

---

## ☸️ Cloud Deployment

### 1️⃣ Task-1: Setup MongoDB on Azure

* Created a **CosmosDB instance** (Mongo API).
* Imported `bookstore.json` into CosmosDB via MongoDB Compass.

### 2️⃣ Task-2: Python Application

* Built Flask API with Docker.
* Verified CRUD operations via **Thunder Client** in VS Code.

### 3️⃣ Task-3: Azure Kubernetes Service (AKS)

* Created AKS cluster via Azure Portal.
* Applied `mongodb-deployment.yaml` & `mongodb-service.yaml` for DB pods.

### 4️⃣ Task-4: Python Application Deployment

* Pushed Flask app image to **Azure Container Registry (ACR)**.
* Deployed `app-deployment.yaml` with **3 replicas** for scalability.
* Exposed with `app-service.yaml` → retrieved external IP for access.

### 5️⃣ Task-5: Service Discovery & Networking

* Applied **`network-policy.yaml`** for secure communication between pods.
* Verified service discovery with socket connection test.
* Confirmed blocked access from unauthorized pods.

---

✅ With this setup, the **Bookstore API** runs locally and in the **cloud (AKS + CosmosDB)** with proper scalability, networking, and security.
