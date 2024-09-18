# TeamSix_SoftArch

## Overview
This project is a web application developed by TeamSix as part of a software architecture course. The application consists of a client-side part and a server-side part that communicate with each other.

## Project Structure
TeamSix_SoftArch/
│
├── client.py                # Client-Side Code
│
├── server.py                # Server-Side Code
│
├── fitness.py               # Fitness Module Code
│
├── README.md              # Project documentation
│
└── requirements.txt         # Python dependencies

## Client
Location: client.py
The client is responsible for sending requests to the server and handling user interactions. It can communicate with the backend to send and receive data.

## Server
Location: server.py
The server handles requests from the client, processes data, and responds to requests. It contains all the backend logic and manages the connection between the client and fitness module.

## Fitness Module
Location: fitness.py
The fitness module contains functionality related to fitness tracking and workout plans. It processes fitness-related data and supports integration with the server.

## Setup Instructions
To get started with the project, follow these steps:

1. Clone the repository:
**git clone https://github.com/nikolaevaElizaveta/TeamSix_SoftArch.git**

2. Install necessary Python dependencies:
**pip install -r requirements.txt**

3. Run the server:
**python server.py**

4. Run the client:
**python client.py**

5. The fitness module will be called automatically from the server when needed.
