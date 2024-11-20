# Point of Sale Shoppers Drug Mart DBMS
Simon Lin (501103322), Dylan Ha (501056670) and Enes Polat (501061594)

This is a Point of Sale (POS) System for Shoppers Drug Mart UI, developed for CPS510 - Database Systems Assignment 9. The system allows for management of products, inventory, transactions, customers, receipts, and employees in a retail environment. 
It is built with Python using Tkinter for the UI, and connects through Oracle SQL for database operations.

Requirements: 
- Python 3
- tkinter (run pip install tk)
- cx_Oracle (run pip install cx_Oracle)
- PIL (Pillow, run pip install pillow)

Once installed, start CS VPN connection and run main.py and login with your proper cs credentials to access the DB.

Below are some sample queries you can run using the custom query input (note: cx_oracle syntax does not require semicolons at the end of statements):

INSERT INTO product (product_id, category, product_name, price, shelf_quantity) VALUES (1, 'Fruit', 'Apple', 0.99, 10)

SELECT * FROM product WHERE price > 5

SELECT * FROM customer

SELECT payment_method AS "Payment_Method", SUM(total_price) AS "Total Sales" FROM receipt GROUP BY payment_method

SELECT name, 'Works as a ' || position || ' for Shoppers Drug Mart' AS "Job Description" FROM employee
