# 🎬 Movie API (IMDB Clone)  

A RESTful API built using Django REST Framework (DRF) that allows users to perform CRUD operations on movies. It includes authentication with JWT, and follows best practices in API development.  

## 🚀 Features  

- **Django REST Framework** for building RESTful APIs  
- **JWT Authentication** for secure user access  
- **CRUD Operations**: Create, Read, Update, Delete movies  
- **Pagination & Filtering** for better data management  
- **Swagger API Documentation** for easy endpoint testing  
- **Docker Support** for easy deployment  

## 🛠️ Tech Stack  

- **Backend**: Django, Django REST Framework (DRF)  
- **Authentication**: JWT (JSON Web Token)  
- **Database**: SQLite  
- **Deployment**: Docker, AWS / Heroku  

## 📂 API Endpoints  

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/register/` | Register a new user |
| `POST` | `/api/login/` | Get JWT token |
| `GET`  | `/api/movies/` | List all movies |
| `POST` | `/api/movies/` | Add a new movie |
| `GET`  | `/api/movies/{id}/` | Get movie details |
| `PUT`  | `/api/movies/{id}/` | Update a movie |
| `DELETE` | `/api/movies/{id}/` | Delete a movie |

## 🔑 Authentication  

To access protected endpoints, users need to include a JWT token in the request headers:  

```http
Authorization: Bearer <your_token>
