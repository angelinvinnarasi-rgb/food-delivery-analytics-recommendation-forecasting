# Food Delivery Analytics, Recommendation & Forecasting

## 1. Project Overview

This project analyzes food delivery data to understand customer ordering behavior, identify popular food combinations, recommend relevant food items, and forecast future sales.

The project combines:

- Exploratory Data Analysis (EDA)
- Association Rule Learning
- Recommendation System
- Time Series Forecasting
- Flask API
- Docker Deployment

---

## 2. Problem Statement

A food delivery company wants to analyze customer ordering behavior, identify popular food combinations, recommend relevant food items, and forecast future order demand.

The analysis can help the business understand customer preferences, improve recommendations, and plan future demand.

---

## 3. Dataset

**Dataset:** `food_delivery_analytics_3000.xlsx`

The dataset contains 3000 food delivery records.

### Main Features

- OrderID
- CustomerID
- Restaurant
- FoodItem
- Quantity
- OrderValue
- TotalAmount
- DeliveryTime_Minutes
- CustomerRating
- City
- PaymentMethod
- OrderDate

Additional time-based features were created:

- Year
- Month
- Weekday

---

## 4. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Mlxtend
- Statsmodels
- Flask
- Docker
- Jupyter Notebook

---

## 5. Project Workflow

The project follows these major steps:

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis
4. Association Rule Learning
5. Recommendation System
6. Time Series Forecasting
7. Flask API Development
8. Docker Deployment

---

## 6. Exploratory Data Analysis

The dataset was analyzed to understand:

- Food item revenue
- Restaurant revenue
- Customer revenue
- City-wise revenue
- Payment method distribution
- Customer rating distribution
- Monthly order trends
- Monthly sales trends

The dataset contains 3000 records and 12 original columns.

Missing values and duplicate records were checked and handled during preprocessing.

---

## 7. Association Rule Learning

Association Rule Learning was implemented using the **Apriori algorithm**.

The dataset did not contain multiple food items within the same OrderID. Therefore, CustomerID was used to create customer-level food baskets.

### Apriori Configuration

- Minimum Support: 0.05
- Minimum Confidence: 0.30
- Ranking metric: Lift

### Results

64 association rules were generated.

Some frequently occurring food combinations include:

- Biryani + Wrap
- Biryani + Sandwich
- Biryani + Sushi
- Biryani + Salad
- Coffee + Wrap

One of the stronger rules identified was:

**Biryani + Sushi → Sandwich**

with a lift of approximately **1.36**.

---

## 8. Recommendation System

A recommendation function was created using the association rules.

Example recommendations:

| Food Item | Recommendations |
|---|---|
| Burger | Coffee, Sandwich, Wrap |
| Biryani | Sandwich, Sushi, Salad |
| Pizza | Salad, Sushi, Sandwich |
| Sushi | Sandwich, Biryani, Taco |

The recommendations are generated based on association rules and ranked using lift.

---

## 9. Time Series Forecasting

Monthly order and sales trends were analyzed.

An **ARIMA (1,1,1)** model was used to forecast future sales.

### Forecast

The model forecasted approximately:

| Month | Forecasted Sales |
|---|---:|
| January 2025 | ₹2.28 lakh |
| February 2025 | ₹2.29 lakh |
| March 2025 | ₹2.29 lakh |

The forecast indicates relatively stable sales during the forecast period.

> Note: The dataset contains only one year of monthly data, so long-term seasonal patterns cannot be established reliably.

---

## 10. Flask Recommendation API

A Flask API was developed to provide food recommendations.

### Home Endpoint

```text
GET /


### Response

```json
{
    "message": "Food Recommendation API is running"
}
```

### Recommendation Endpoint

```text
GET /recommend?food_item=Burger
```

### Response

```json
{
    "food_item": "Burger",
    "recommendations": [
        "Coffee",
        "Sandwich",
        "Wrap"
    ]
}
```

---

## 11. Docker Deployment

The Flask application was containerized using Docker.

### Build Docker Image

```bash
docker build -t food-delivery-api .
```

### Run Docker Container

```bash
docker run -p 5000:5000 food-delivery-api
```

### Access the API

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

For food recommendations:

```text
http://127.0.0.1:5000/recommend?food_item=Burger
```

---

## 12. Project Structure

```text
Food_Delivery_Analytics_Recommendation_Forecasting/
│
├── data/
│   └── food_delivery_analytics_3000.xlsx
│
├── notebook/
│   └── Food_Delivery_Analytics_Recommendation_Forecasting.ipynb
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 13. How to Run the Project

### Run the Notebook

Open the notebook:

```text
notebook/Food_Delivery_Analytics_Recommendation_Forecasting.ipynb
```

Run the cells in order to perform:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Association rule mining
- Food recommendations
- Sales forecasting

### Run the Flask API

Install the required package:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

### Run Using Docker

Build the Docker image:

```bash
docker build -t food-delivery-api .
```

Run the Docker container:

```bash
docker run -p 5000:5000 food-delivery-api
```

Then access the API:

```text
http://127.0.0.1:5000
```

---

## 14. Conclusion

This project demonstrates how food delivery data can be used for business analytics and machine learning applications.

The project provides:

- Customer and sales analysis through EDA
- Food combination discovery using Apriori
- Food recommendations using association rules
- Future sales forecasting using ARIMA
- A Flask-based recommendation API
- Docker-based application deployment

These techniques can support data-driven decision-making in food delivery businesses.