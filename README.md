```markdown

# E-commerce Product API

## A RESTful API built with Django and Django REST Framework (DRF) for managing users and products in an e-commerce platform.

### Features

* User registration & JWT authentication
* CRUD for products
* Search products by name or category
* Pagination & filtering
* Permissions:
  * Authenticated users can add/update/delete products
  * Anyone can view/search products
* Deployable on Heroku or PythonAnywhere

### Tech Stack

* Django
* Django REST Framework
* djangorestframework-simplejwt (JWT Authentication)
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
POST	        /api/register/	            Register a new user
POST	        /api/login/	                Login and get JWT token
GET	            /api/products/	            List all products
POST	        /api/products/	            Create new product
GET	            /api/products/<id>/	        Get product details
PUT	            /api/products/<id>/	        Update a product
DELETE	        /api/products/<id>/	        Delete a product
GET	            /api/products/search/	    Search products by name/category 
```

### Usage

#### Example request with JWT token:
```bash
curl -X GET http://127.0.0.1:8000/api/products/ \
-H "Authorization: Bearer <your_token>"
```

### Deployment

* Configure environment variables (SECRET_KEY, DATABASE_URL, etc.)
* Collect static files:
```bash
python manage.py collectstatic
```
* Deploy to Heroku or PythonAnywhere

### Testing

```bash
python manage.py test
```
```