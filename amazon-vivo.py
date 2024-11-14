import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for the Amazon search page
base_url = 'https://www.amazon.in/s?k=vivo&page={}'

# Headers to simulate a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

# Loop through pages, adjust the range to control the number of pages to scrape
for page in range(1, 6):  # Scraping pages 1 to 5
    url = base_url.format(page)
    
    # Send a GET request to the Amazon URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # List to store product details for each page
        products = []
        
        # Find all product sections on the page
        product_sections = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        # Loop through each product section and extract details
        for product_section in product_sections:
            # Extract product name
            name_tag = product_section.find('span', class_='a-size-medium a-color-base a-text-normal')
            product_name = name_tag.text.strip() if name_tag else "N/A"
            
            # Extract rating (stars)
            rating_tag = product_section.find('span', class_='a-icon-alt')
            product_rating = rating_tag.text.split()[0] if rating_tag else "N/A"  # e.g., '4.5 out of 5 stars'
            
            # Extract number of reviews
            reviews_tag = product_section.find('span', class_='a-size-base s-underline-text')
            product_reviews = reviews_tag.text.strip() if reviews_tag else "N/A"
            
            # Extract 'Bought last month' text (if available)
            bought_last_month_tag = product_section.find('span', class_='a-size-base a-color-secondary')
            bought_last_month = bought_last_month_tag.text.strip() if bought_last_month_tag else "N/A"
            
            # Extract current MRP (price)
            current_price_tag = product_section.find('span', class_='a-price-whole')
            current_price = current_price_tag.text.replace(',', '').strip() if current_price_tag else "N/A"
            
            # Extract dashed (original) MRP
            original_price_tag = product_section.find('span', class_='a-price a-text-price')
            dashed_mrp = original_price_tag.find('span', class_='a-offscreen').text.replace(',', '').strip() if original_price_tag else "N/A"
            
            # Extract discount percentage
            discount_tag = product_section.find('span', string=lambda text: text and '(' in text and '%' in text)
            discount_percentage = discount_tag.text if discount_tag else "N/A"

            # Check for free delivery status
            free_delivery_tag = product_section.find('span', string=lambda x: x and 'free delivery' in x.lower())
            free_delivery = "Yes" if free_delivery_tag else "No"

            # Append all product details to the list
            products.append({
                'Product Name': product_name,
                'Rating (Stars)': product_rating,
                'Number of Reviews': product_reviews,
                'Bought Last Month': bought_last_month,
                'Current MRP': current_price,
                'Dashed MRP': dashed_mrp,
                'Discount (%)': discount_percentage,
                'Free Delivery': free_delivery
            })
        
        # Convert list of products to DataFrame
        df = pd.DataFrame(products)
        
        # Save each page's data to a separate CSV file
        file_name = f'Amazon-Vivo-csvs/amazon_page_{page}.csv'
        df.to_csv(file_name, index=False)
        print(f"Data exported to {file_name}")
    else:
        print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
