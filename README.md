# no-bs_URL_shortner

a minimalist URL shortner , no bullshit only the shortened URL

## Project Structure

The project is divided into multiple phases for better organization and development flow:

| Phase   | Objective                                       |
| ------- | ----------------------------------------------- |
| Phase 0 | Project setup & environment                     |
| Phase 1 | Basic FastAPI app + health check                |
| Phase 2 | Database setup & URL model                      |
| Phase 3 | URL shortening logic                            |
| Phase 4 | Redirect logic                                  |
| Phase 5 | Validation & error handling                     |
| Phase 6 | Configuration & environment management          |
| Phase 7 | Scalability & design discussion (no heavy code) |

Two separate folders for frontend and backend code:

>frontend

>app

USe the following command to create the virtual environment:

>`python -m venv .venv`

then install FastAPI using :

>`pip install "fastapi[standard]"`

To run the backend server, use the command:

>`uvicorn app.main:app --reload`

Install SQLAlchemy using:

>`pip install SQLAlchemy`

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. SQLAlchemy provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

Install psycopg2 using:

>`pip install psycopg2`

Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent “INSERT”s or “UPDATE”s.


> `pip install pydantic-settings`

