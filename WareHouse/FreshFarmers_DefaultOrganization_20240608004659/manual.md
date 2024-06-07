```markdown
# FreshFarmers

Connecting consumers with local farmers for fresh, locally-sourced agricultural products.

## Overview

FreshFarmers is a web and mobile application designed to connect consumers with local farmers within a 50km radius. The platform allows users to browse and order fresh agricultural products directly from local producers. The application includes features such as user-friendly interfaces, secure authentication, real-time inventory management, payment processing, and more.

## Main Functions

### User Functions

1. **Browse Products**: Users can browse a variety of agricultural products categorized by type, price, and dietary preferences.
2. **Place Orders**: Users can place orders for products from multiple farms.
3. **Manage Orders**: Users can view, modify, and cancel their orders.
4. **Search and Filter**: Users can search for products and filter them based on categories, price, and dietary preferences.
5. **Interactive Map**: Users can view an interactive map showing farms within a 50km radius.
6. **Profile Management**: Users can manage their profiles, including bio, order history, and delivery preferences.
7. **Cart Management**: Users can manage their cart and receive alerts for multi-farm orders.
8. **Gamification**: Users can view simulated savings, CO2 reduction, and health benefits compared to traditional shopping.

### Farmer Functions

1. **Profile Pages**: Farmers can create and manage their profiles, including bio, products, images, and availability.
2. **Order Management**: Farmers can manage orders, update order status, and handle cancellations.
3. **Inventory Management**: Farmers can manage their product inventory in real-time.
4. **Wallet Management**: Farmers can manage their earnings and transactions.

## Installation

### Environment Setup

To set up the environment for FreshFarmers, you need to install the required dependencies. Follow the steps below:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Black-Wonka/Freshtest.git
   cd Freshtest
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

The `requirements.txt` file includes the following dependencies:

- **Flask**: The main web framework used for building the web application.
- **Flask-Session**: Used for session management in Flask.
- **Flask-SQLAlchemy**: Provides SQLAlchemy support for Flask applications.
- **Flask-WTF**: Integrates WTForms with Flask for form handling.
- **geopy**: Used for geolocation services, such as calculating distances between coordinates.
- **Werkzeug**: A comprehensive WSGI web application library used by Flask.
- **WTForms**: A flexible forms validation and rendering library for Python web development.
- **email-validator**: Used for validating email addresses in forms.

To install these dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Running the Application

1. **Initialize the Database**

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

2. **Run the Application**

   ```bash
   python main.py
   ```

   The application will be available at `http://127.0.0.1:5000`.

## Usage

### Landing Page

- **Login as Farmer or Customer**: Users can choose to log in as either a farmer or a customer.

### Home Page

- **Map and List View**: Users can toggle between map and list views to see nearby farms.
- **Search and Filter**: Users can search for products and apply filters.

### Profile Page

- **Farmer Profile**: Farmers can manage their bio, products, images, and availability.
- **Customer Profile**: Customers can manage their bio, order history, and delivery preferences.

### Cart Page

- **Cart Management**: Users can manage their cart, view multi-farm order alerts, and proceed to checkout.

### Order Management

- **Order Lifecycle**: Users can create, modify, cancel, and track orders.

### Notifications

- **Email/SMS Updates**: Users receive notifications for order updates via email or SMS.

### Gamification

- **Savings Simulation**: Users can view simulated savings, CO2 reduction, and health benefits compared to traditional shopping.

## Contributing

To contribute to the FreshFarmers project, follow these steps:

1. **Fork the Repository**

   ```bash
   git fork https://github.com/Black-Wonka/Freshtest.git
   ```

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature-branch
   ```

3. **Commit Changes**

   ```bash
   git commit -m "Add new feature"
   ```

4. **Push to GitHub**

   ```bash
   git push origin feature-branch
   ```

5. **Create a Pull Request**

   Go to the repository on GitHub and create a pull request.

## Support

For any issues or questions, please contact our support team at support@freshfarmers.com.

## License

FreshFarmers is licensed under the MIT License. See the LICENSE file for more details.

```
```