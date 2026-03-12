# Simple Social — FastAPI Image & Video Upload App

A **full-stack social media style application** built with **FastAPI, Streamlit, SQLite, and ImageKit**.

Users can:

- Register and login
- Upload images and videos
- Store media using ImageKit
- View a public feed
- Delete their own posts

This project demonstrates how to build a **production-style backend API with authentication, database integration, and media handling**.

---

##  Features

- JWT Authentication
- Image & Video Upload
- Cloud Storage with ImageKit
- SQLite Database
- FastAPI REST API
- Streamlit Frontend
- Auto API Documentation
- Media transformation with ImageKit

---

## Tech Stack

| Technology | Purpose |
|------------|--------|
| FastAPI | Backend API |
| FastAPI Users | Authentication |
| SQLite + SQLAlchemy | Database |
| ImageKit | Image & video storage |
| Streamlit | Frontend |
| UV | Python dependency manager |
| Pydantic | Data validation |

---

## ImageKit Integration

ImageKit is an **image and video API plus AI-Powered DAM** that we use in this project to handle all of our image and video operations.

ImageKit allows us to:

- Upload images and videos
- Transform media
- Add overlays
- Optimize delivery
- Store media in the cloud

ImageKit Documentation:

https://imagekit.io/docs

---

## Project Architecture

project-root
│

├── app

│ ├── app.py
│ ├── db.py

│ ├── schemas.py

│ ├── images.py

│ └── auth.py

│

├── frontend.py

├── .env

├── pyproject.toml

└── README.md

