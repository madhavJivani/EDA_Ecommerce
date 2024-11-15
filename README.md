# EDA_Ecommerce
# Optimal Price and Options Predictor

## Overview
The goal of this model is to predict the optimal price, discount percentage, and whether to offer free delivery for a product based on its features. The model is designed to maximize sales and profit by recommending the price you should sell at, as well as predicting the discount percentage and the "Free Delivery" option based on the product details.

### Features:
- **Product Name**: This will be parsed to extract the brand and category of the product.
- **Ratings (Stars)**: The rating the product has received from customers.
- **Number of Reviews**: The total number of reviews the product has received, providing insight into its popularity.
- **Bought Last Month**: The number of units bought last month, which gives us an indicator of recent sales performance.
- **Current Price (MRP)**: The price at which the product is being sold currently.
- **Discount Percentage**: The percentage discount that should be offered to maximize sales.
- **Free Delivery**: Whether or not free delivery should be offered.

---

## Data Preprocessing and Feature Engineering

### 1. **Parsing Product Name**
We extract useful information from the `Product Name`:
- **Brand**: Derived from the first part of the product name (e.g., Samsung).
- **Category/Model**: The product name, minus the brand name.
- **Color**: Extracted from product name, with a fallback to "Black" if no color is specified.
- **RAM**: Extracted from the product name (e.g., 6GB, 8GB).
- **Storage**: Extracted from the product name (e.g., 128GB, 256GB).
  
A regular expression is used to capture these details. Here is the example pattern:
- For "Samsung Galaxy S23 Ultra 5G AI Smartphone (Green, 12GB, 256GB Storage)", we extract the following:
  - **Brand**: Samsung
  - **Product**: Samsung Galaxy S23 Ultra 5G
  - **Color**: Green
  - **RAM**: 12GB
  - **Storage**: 256GB

### 2. **Converting `Bought Last Month` to Numeric**
The `Bought Last Month` column contains various formats like:
- "50+ bought in past month" → Extract `50` as numeric.
- "5K" → Convert `5K` to `5000`.
- Non-relevant or invalid data is treated as `0`.

### 3. **Handling Missing Values for MRP**
For the `Dashed MRP` column, if it contains missing or `NaN` values, we assign the `Current MRP` value instead.

### 4. **Extracting Discount Percentage**
The `Discount (%)` column may contain text like:
- "(20% off)"
- "60% off"
- We extract the numeric discount percentage and handle any missing or malformed data by setting it to `0`.

---

## Model Prediction

### Target Variables:
- **Optimal Price**: The price that should be set to maximize profit, which is influenced by current market conditions, reviews, sales history, and product attributes.
- **Discount Percentage**: The percentage discount that should be applied to maximize sales while maintaining a profitable margin.
- **Free Delivery Option**: Whether to offer free delivery, which can influence purchase decisions.

### Input Features:
- **Brand**: Extracted from product name.
- **Category/Model**: Derived from product name.
- **Ratings**: Product ratings.
- **Number of Reviews**: Total number of reviews.
- **Bought Last Month**: Extracted numeric value from `Bought Last Month`.
- **Current MRP**: The current price of the product.
- **Dashed MRP**: If available, the original price (or fallback to current MRP).
- **Discount Percentage**: The discount provided.

### Preprocessing:
- We normalize or standardize numeric features (such as the number of reviews, bought last month, and price) to avoid any scaling issues.
- Categorical features like `Brand`, `Category/Model`, and `Color` are encoded using label encoding or one-hot encoding.

### Machine Learning Model:
The following models can be employed to predict the target variables:
- **Linear Regression** for price prediction.
- **Decision Tree or Random Forest** for predicting the discount percentage and free delivery option.
- **Gradient Boosting Models** (e.g., XGBoost, LightGBM) for optimizing performance, considering interactions between features like ratings, reviews, and price.

We can train separate models for each target:
1. **Optimal Price Prediction**: Using features like ratings, number of reviews, and current MRP.
2. **Discount Percentage Prediction**: Using features such as sales data (Bought Last Month) and price.
3. **Free Delivery Prediction**: Using sales data and product category/brand information.

---

## Model Evaluation
Once the models are trained, we can evaluate their performance based on:
- **Mean Absolute Error (MAE)**: For price prediction accuracy.
- **Accuracy** or **F1-Score**: For classification tasks like predicting free delivery.
- **Cross-validation**: To ensure that the model generalizes well.

---

## Conclusion
This predictor provides valuable insights into how to set an optimal price, the ideal discount percentage, and whether free delivery should be offered. By utilizing historical sales data, product features, and reviews, the model is designed to maximize sales while optimizing profitability.
