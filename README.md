PROJECT NAME:
Sissors

OVERVIEW:
This project is a URL shortening project built using FastAPI and SQLAlchemy. It allows users to input a long URL and generates a shortened version of it, along with a QR code for easy sharing. The shortened URLs are stored in a PostgreSQL database.

FILES

- main.py The main.py file contains the FastAPI application and defines the API endpoints for URL shortening, URL redirection, and QR code generation.

- crud.py The crud.py file contains functions for creating and retrieving shortened URLs from the database.

- models.py The models.py file defines the SQLAlchemy database models for storing shortened URLs.

- database.py The database.py file sets up the PostgreSQL database connection and provides a session maker for interacting with the database.

- schemas.py The schemas.py file defines Pydantic models for input and output data validation.

- qr_code_generator.py The qr_code_generator.py file contains a function for generating QR codes from URLs.

USAGE:
- To shorten a URL, send a POST request to the /long_url/ endpoint with the long URL as the request body.
- To access the original URL from a shortened URL, send a GET request to /{shortened_url}.
- To generate a QR code for a shortened URL, send a GET request to /generate_qr/{shortened_url}.

DEPENDENCIES
- FastAPI
- SQLAlchemy
- Pydantic
- psycopg2
- shortuuid
- qrcode
