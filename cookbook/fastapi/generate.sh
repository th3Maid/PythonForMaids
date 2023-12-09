#!/bin/bash

# Create project directory
mkdir project
cd project

# Create app directory
mkdir app
cd app

# Create API directory
mkdir api
cd api

# Create endpoints directory
mkdir endpoints
touch endpoints/__init__.py
touch endpoints/example.py
touch endpoints/another_endpoint.py

# Create dependencies directory
mkdir dependencies
touch dependencies/__init__.py
touch dependencies/auth.py

cd ../..

# Create core directory
mkdir core
cd core

# Create config file
touch config.py

# Create database file
touch database.py

cd ..

# Create models directory
mkdir models
cd models

# Create user model file
touch user.py

cd ..

# Create services directory
mkdir services
cd services

# Create user service file
touch user_service.py

cd ..

# Create tests directory
mkdir tests
touch tests/__init__.py
touch tests/test_example.py

# Output completion message
echo "FastAPI project structure created successfully!"
