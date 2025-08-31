
# E-commerce Product API

## A RESTful API built with Django and Django REST Framework (DRF) for managing users and products in an e-commerce platform.

### Features

* User registration & JWT authentication
* CRUD for products
* Product categories & tags
* Search products by name, category or tag
* Pagination & filtering
* Permissions:
  * Authenticated users can add/update/delete products
  * Anyone can view/search products
* Deployable on Heroku or PythonAnywhere

### Tech Stack

* Django
* Django REST Framework
* djangorestframework-simplejwt (JWT Authentication)
* django-filter
* PostgreSQL / SQLite

### Installation

```python
# Clone repo
git clone https://github.com/your-username/ecommerce-api.git
cd ecommerce-api

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

### API Endpoints

```graphql
Method	        Endpoint	                Description
------          --------                    -----------

POST	        /api/register/	            Register a new user
POST	        /api/login/	                Login and get JWT token
GET	            /api/products/	            List all products
POST	        /api/products/	            Create new product
GET	            /api/products/<id>/	        Get product details
PUT	            /api/products/<id>/	        Update a product
DELETE	        /api/products/<id>/	        Delete a product
GET	            /api/products/search/	    Search products by name/category/tag
GET	            /api/categories/	        List all categories
POST	        /api/categories/	        Create a new category
GET	            /api/tags/	                List all tags
POST	        /api/tags/	                Create a new tag 
```

### Usage

#### Example request with JWT token:
```bash
# Register a new user
curl -X POST http://127.0.0.1:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "password123"
}'
```
#### Example Create Product with Category & Tags
```bash
curl -X POST http://127.0.0.1:8000/api/products/ \
-H "Authorization: Bearer <your_token>" \
-H "Content-Type: application/json" \
-d '{
  "name": "iPhone 14",
  "description": "Latest iPhone",
  "price": "999.99",
  "category_id": 1,
  "tag_ids": [1, 2]
}'
```

### Deployment

* Configure environment variables (SECRET_KEY, DATABASE_URL, etc.)
* Collect static files:
```bash
python manage.py collectstatic
```
* Deploy to Heroku or PythonAnywhere

### Postman Testing Guide

#### 1. Setup

* Open Postman
* Start your Django server:
```bash
python manage.py runserver
```
* Base URL:
```cpp
http://127.0.0.1:8000
```

#### 2. Authentication

##### Register a user
* POST http://127.0.0.1:8000/api/users/register/
* Body → raw → JSON:
```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "mypassword123"
}
```
##### Login with Djoser
* POST http://127.0.0.1:8000/api/auth/token/login/
* Body → raw → JSON:
```json
{
  "username": "zubeir",
  "password": "mypassword123"
}
```
* Copy the access token for authorization in other requests.

#### 3. Products

##### Get all products
* GET http://127.0.0.1:8000/api/products/
* 
##### Create a product
* POST http://127.0.0.1:8000/api/products/
* Headers:
```pgsql
Authorization: Bearer <your_token>
Content-Type: application/json
```
* Body:
```json
{
  "name": "MacBook Pro",
  "description": "16-inch, 32GB RAM",
  "price": "2500.00",
  "category": 1,
  "tags": [1, 2]
}
```

##### Update a product
* PUT http://127.0.0.1:8000/api/products/1/
* Body:
```json
{
  "name": "MacBook Pro 2025",
  "description": "Upgraded 64GB RAM",
  "price": "3000.00",
  "category": 1,
  "tags": [2]
}
```

##### Delete a product
* DELETE http://127.0.0.1:8000/api/products/1/

#### 4. Categories & Tags

##### List categories
* GET http://127.0.0.1:8000/api/categories/

##### Create category
* POST http://127.0.0.1:8000/api/categories/
* Body:
```json
{
  "name": "Laptops"
}
```

##### List tags
* GET http://127.0.0.1:8000/api/tags/

##### Create tag
* POST http://127.0.0.1:8000/api/tags/
* Body:
```json
{
  "name": "Electronics"
}
```

#### 5. Search Products

* GET http://127.0.0.1:8000/api/products/search/?name=MacBook
* Or by category:
```arduino
http://127.0.0.1:8000/api/products/search/?category=Laptops
```
* Or by tag:
```arduino
http://127.0.0.1:8000/api/products/search/?tag=Electronics
```