# Online clothing store

T120B165 Saityno taikomųjų programų projektavimas modulio projektas

A clothing store mockup page.

## Turinys
- [Sprendžiamo uždavinio aprašymas](#sprendžiamo-uždavinio-aprašymas)
- [Sistemos Architektūra](#sistemos-architektūra)
- [Naudotojo sąsajos projektas](#naudotojo-sąsajos-projektas)
- [API Specifikacija](#api-specifikacija)
- [Išvados](#išvados)

## Sprendžiamo uždavinio aprašymas

An online clothing store website mockup page.

### Objects

**• Collection** - a collection of different clothing garments. (Winter collection, Summer collection, etc.)

**• Product** - a certain piece of clothing being sold. (Black T-Shirt, Jeans, Leather jacket, etc.)

**• Review** - a review of a piece of clothing left by a client.

### Object hierarchy:

**Collection** -> **Product** -> **Review**

### Functionality

Account login and registration. Authentication using JWT.
By role:

**• Administrator** - create, edit, delete collections and products.

**• Member** - post and delete reviews.

**• Guest** - view collections and products.


### Stack

• **Frontend**: React.js

• **Backend**: Django

• **Authentication**: JWT

• **Database**: PostgreSQL

## Sistemos Architektūra

## Naudotojo sąsajos projektas

### Login

Wireframe
![login_frame](https://github.com/user-attachments/assets/f0553771-7772-4cb9-a5d0-4c3e1f2e0e0f)

Realization
![login](https://github.com/user-attachments/assets/14735d67-4da6-4f25-9090-5f7afd70059d)

### Register

Wireframe
![register_frame](https://github.com/user-attachments/assets/a4654cd4-98e7-44e7-bc40-62f20f277adf)

Realization
![register](https://github.com/user-attachments/assets/333cf4da-0ef9-4943-8099-7877b0066878)

### Home

Wireframe
![home_frame](https://github.com/user-attachments/assets/d48c3ba0-b76d-4101-b658-c5a79c288221)

Realization
![home](https://github.com/user-attachments/assets/07aea16f-f493-4a9f-9b55-dbd276b53d80)

### View Collection

Wireframe
![collection_frame](https://github.com/user-attachments/assets/bff54357-f611-4b4a-9ec2-c077b1f11aa6)

Realization
![collection](https://github.com/user-attachments/assets/a29dd46f-0d98-4352-9e31-79c737515a2d)

### View Product

Wireframe
![product_frame](https://github.com/user-attachments/assets/4b83981e-2bf4-40bc-8547-aa3bbd801893)

Realization
![product](https://github.com/user-attachments/assets/28d4c666-8d5a-45c8-9cbb-0e760c9f9459)
![reviews](https://github.com/user-attachments/assets/4c000cd5-b50f-4d74-8a24-b1e2928f1889)

### Manager

Wireframe
![manage_frame](https://github.com/user-attachments/assets/5c51bffa-9f1c-49c0-bfe4-e3d8386e10ab)

Realization
![manage](https://github.com/user-attachments/assets/eab98799-4b6f-4379-ba66-4214ca9f82e3)

### Add Collection

Wireframe
![addcollection_frame](https://github.com/user-attachments/assets/dbe5061b-4322-4176-b6a2-f357a84beaac)

Realization
![addcollection](https://github.com/user-attachments/assets/94a283c4-b472-42d6-8174-26e2012366bc)

### Add Product

Wireframe
![addproduct_frame](https://github.com/user-attachments/assets/a37a6243-49b8-41bf-82ec-81d438f777e5)

Realization
![addproduct](https://github.com/user-attachments/assets/ed37c272-5c3b-4d5d-80a8-13287325eec1)

---

## API Specifikacija

[OpenAPI Documentation](https://deirasshop-asa8ezhxd3befmg6.northeurope-01.azurewebsites.net/swagger/?format=openapi)

### Collections

#### List All Collections

**GET** `/api/collections/`

- **Description**: Retrieves a list of all collections.
- **Response Codes**:
  - `200 OK`: Successfully retrieved the list.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
[
  {
    "id": 1,
    "name": "Winter Collection",
    "description": "Warm and cozy clothing for winter.",
    "image": "winter.jpg"
  },
  {
    "id": 2,
    "name": "Summer Collection",
    "description": "Light and breathable clothing for summer.",
    "image": "summer.jpg"
  }
]
```

---

#### Create a New Collection

**POST** `/api/collections/`

- **Description**: Creates a new collection.
- **Request Body**:
```json
{
  "name": "Fall Collection",
  "description": "Stylish and colorful clothing for fall.",
  "image": "fall.jpg"
}
```
- **Response Codes**:
  - `201 Created`: Successfully created the collection.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
{
  "id": 3,
  "name": "Fall Collection",
  "description": "Stylish and colorful clothing for fall.",
  "image": "fall.jpg"
}
```

---

#### Retrieve a Specific Collection

**GET** `/api/collections/{id}/`

- **Description**: Retrieves details of a specific collection by ID.
- **Response Codes**:
  - `200 OK`: Successfully retrieved the collection.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
{
  "id": 1,
  "name": "Winter Collection",
  "description": "Warm and cozy clothing for winter.",
  "image": "winter.jpg"
}
```

---

#### Update a Collection

**PUT** `/api/collections/{id}`

- **Description**: Updates a collection.
- **Request Body**:
```json
{
  "name": "Updated Fall Collection",
  "description": "Stylish and colorful clothing for fall.",
  "image": "fall.jpg"
}
```
- **Response Codes**:
  - `200 OK`: Successfully updated the collection.
  - `400 Bad request`: Missing fields.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
{
  "id": 3,
  "name": "Updated Fall Collection",
  "description": "Stylish and colorful clothing for fall.",
  "image": "fall.jpg"
}
```

---

#### Delete a Collection

**DELETE** `/api/collections/{id}`

- **Description**: Deletes a collection.

- **Response Codes**:
  - `204 Deleted`: Successfully deleted the collection.
  - `401 Unauthorized`: Don't have permissions.

---

### Products

#### List Products in a Collection

**GET** `/api/collections/{collection_pk}/products/`

- **Description**: Retrieves a list of products within a specific collection.
- **Response Codes**:
  - `200 OK`: Successfully retrieved the products.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
[
  {
    "id": 1,
    "name": "Winter Jacket",
    "price": "89.99",
    "description": "A warm jacket for cold weather.",
    "image": "jacket.jpg",
    "collection": 1
  },
  {
    "id": 2,
    "name": "Woolen Scarf",
    "price": "19.99",
    "description": "A soft scarf to keep you warm.",
    "image": "scarf.jpg",
    "collection": 1
  }
]
```

---

#### Create a Product in a Collection

**POST** `/api/collections/{collection_pk}/products/`

- **Description**: Creates a new product within a specific collection.
- **Request Body**:
```json
{
  "name": "Beanie Hat",
  "price": "14.99",
  "description": "A stylish and warm hat.",
  "image": "beanie.jpg",
  "collection": 1
}
```
- **Response Codes**:
  - `201 Created`: Successfully created the product.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
{
  "id": 3,
  "name": "Beanie Hat",
  "price": "14.99",
  "description": "A stylish and warm hat.",
  "image": "beanie.jpg",
  "collection": 1
}
```

---

#### Retrieve a Specific Product

**GET** `/api/collections/{collection_pk}/products/{id}/`

- **Description**: Retrieves details of a specific product by ID.
- **Response Codes**:
  - `200 OK`: Successfully retrieved the product.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
{
  "id": 1,
  "name": "Winter Jacket",
  "price": "89.99",
  "description": "A warm jacket for cold weather.",
  "image": "jacket.jpg",
  "collection": 1
}
```

---

#### Update a Product in a Collection

**PUT** `/api/collections/{collection_pk}/products/{id}`

- **Description**: Updates a product within a specific collection.
- **Request Body**:
```json
{
  "name": "Updated Beanie Hat",
  "price": "14.99",
  "description": "A stylish and warm hat.",
  "image": "beanie.jpg",
  "collection": 1
}
```
- **Response Codes**:
  - `200 OK`: Successfully updated the product.
  - `400 Bad request`: Missing fields.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
{
  "id": 3,
  "name": "Updated Beanie Hat",
  "price": "14.99",
  "description": "A stylish and warm hat.",
  "image": "beanie.jpg",
  "collection": 1
}
```

---

#### Delete a Product in a Collection

**DELETE** `/api/collections/{collection_pk}/products/{id}`

- **Description**: Deletes a product within a specific collection.

- **Response Codes**:
  - `204 Deleted`: Successfully Deleted the product.
  - `401 Unauthorized`: Don't have permissions.

---

### Reviews

#### List Reviews for a Product

**GET** `/api/collections/{collection_pk}/products/{product_pk}/reviews/`

- **Description**: Retrieves a list of reviews for a specific product.
- **Response Codes**:
  - `200 OK`: Successfully retrieved the reviews.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
[
  {
    "id": 1,
    "rating": 5,
    "comment": "Excellent quality!",
    "product": 1,
    "user": 10
  },
  {
    "id": 2,
    "rating": 4,
    "comment": "Very warm, but a bit tight.",
    "product": 1,
    "user": 12
  }
]
```

---

#### Create a Review for a Product

**POST** `/api/collections/{collection_pk}/products/{product_pk}/reviews/`

- **Description**: Creates a new review for a specific product.
- **Request Body**:
```json
{
  "rating": 4,
  "comment": "Comfortable and well-made.",
  "product": 1,
  "user": 15
}
```
- **Response Codes**:
  - `201 Created`: Successfully created the review.
  - `400 Bad request`: Missing fields.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
{
  "id": 3,
  "rating": 4,
  "comment": "Comfortable and well-made.",
  "product": 1,
  "user": 15
}
```
---

#### Retrieve a Review for a Product

**PUT** `/api/collections/{collection_pk}/products/{product_pk}/reviews/{id}`

- **Description**: Retrieves a specific review for a specific product.
- **Response Codes**:
  - `200 OK`: Successfully retrieved the review.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
{
  "id": 3,
  "rating": 4,
  "comment": "Comfortable and well-made.",
  "product": 1,
  "user": 15
}
```

---

#### Update a Review for a Product

**PUT** `/api/collections/{collection_pk}/products/{product_pk}/reviews/{id}`

- **Description**: Updates a review for a specific product.
- **Request Body**:
```json
{
  "rating": 4,
  "comment": "Updated review.",
  "product": 1,
  "user": 15
}
```
- **Response Codes**:
  - `200 OK`: Successfully updated the review.
  - `400 Bad request`: Missing fields.
  - `401 Unauthorized`: Don't have permissions.

**Example Response:**
```json
{
  "id": 3,
  "rating": 4,
  "comment": "Updated review.",
  "product": 1,
  "user": 15
}
```

---

#### Delete a Review for a Product

**DELETE** `/api/collections/{collection_pk}/products/{product_pk}/reviews/{id}`

- **Description**: Deletes a review for a specific product.

- **Response Codes**:
  - `204 Deleted`: Successfully deleted the review.
  - `401 Unauthorized`: Don't have permissions.



---

### Authentication

#### Register

**POST** `/api/register/`

- **Description**: Registers a new user.
- **Response Codes**:
  - `201 Created`: Successfully registered the user.
  - `400 Bad request`: Username already exists.

---

#### Obtain Token

**POST** `/api/token/`

- **Description**: Obtains an access and refresh token.
- **Request Body**:
```json
{
  "username": "exampleuser",
  "password": "examplepassword"
}
```
- **Response Codes**:
  - `200 OK`: Successfully obtained tokens.
  - `401 Unauthorized`: No active account found with the given credentials.

**Example Response:**
```json
{
  "refresh": "refresh_token_string",
  "access": "access_token_string"
}
```

---

#### Refresh Token

**POST** `/api/token/refresh/`

- **Description**: Refreshes the access token using a refresh token.
- **Request Body**:
```json
{
  "refresh": "refresh_token_string"
}
```
- **Response Codes**:
  - `200 OK`: Successfully refreshed the token.
  - `401 Unauthorized`: Token not valid.

**Example Response:**
```json
{
  "access": "new_access_token_string"
}
```

---

### Logout

**POST** `/logout/`

- **Description**: Logs out the user.
- **Response Codes**:
  - `200 OK`: Successfully logged out.
  - `400 Bad Request`: Invalid token or logout failed.
  
**Example Response:**
```json
{
  "message": "Logged out successfully."
}
```
---

## Išvados

- All required API requests have been successfully implemented using the Django framework
- User Interface has been successfully implemented using React and connected to the backend functions.
- The projects was successfully deployed to a Azure WebApp and connected to a PostgreSQL database on an Azure server.
