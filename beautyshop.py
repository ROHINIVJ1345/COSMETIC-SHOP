#AGENDA:

#DATABASE = beautyshop
#TABLE = beauty_products,review

# 1. BEAUTY_PRODUCTS= product_id,product_name,brand,unit_price
   # *add_product
   # *view_poduct
   # *update_product 
   # *delete_product

# 2. REVIEW = customer_name,product_name,mobile_number,review
   # *add_review
   # *view_review



# 1.BEAUTY_PRODUCTS

    # add_product

import pymysql
import tabulate
try:
    db=pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Beautyshop"
    )
except pymysql.error as err:
        print("ERROR",err)
    
cursor=db.cursor()

def add_product():
      
      try:
            Product_id=input("ENTER THE PRODUCT ID:");
            Product_name=input("ENTER THE PRODUCT NAME:");
            Brand=input("ENTER THE BRAND:");
            Unit_price=float(input("ENTER THE UNIT PRICE:"));
            
            cursor.execute('''
            insert into beauty_products(product_id,product_name,brand,unit_price)
            values (%s,%s,%s,%s)
            ''',(Product_id,Product_name,Brand,Unit_price))
            
            db.commit()
            print("product added successfully")
      except Exception as err:
            print("ERROR",err)



add_product()



db.close()

       




      #view_product

import pymysql
import tabulate
try:
    db=pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Beautyshop"
    )
except pymysql.error as err:
        print("ERROR",err)
    
cursor=db.cursor()

def view_product():
    '''view all products in the beauty_products table'''
      
    try:
        cursor.execute("select * from beauty_products")
        result=cursor.fetchall()
        headers=[desc[0] for desc in cursor.description]
        print(tabulate.tabulate(result,headers=headers,tablefmt="grid"))
    except Exception as err:
        print("Error",err)
    



view_product()
   


db.close()






       #update_product

import pymysql
from pymysql import MySQLError

def update_product():
    connection = None
    try:
        
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="Beautyshop"
        )
        
        
        with connection.cursor() as cursor:
            
            product_name = input("Enter the product name to update: ");
            unit_price = float(input("Enter the new unit price: "));
            brand = input("Enter the new brand: ");
            
            
            check_query = "SELECT unit_price,brand FROM beauty_products WHERE product_name=%s"
            cursor.execute(check_query, (product_name,))
            result = cursor.fetchone()
            
            if result:
                
                update_query = """
                UPDATE beauty_products
                SET unit_price=%s, brand=%s
                WHERE product_name=%s
                """
                cursor.execute(update_query, (unit_price, brand, product_name))
                connection.commit()
                print(f"Product '{product_name}' updated successfully.")
            else:
                print(f"Product '{product_name}' not found.")
    
    except MySQLError as err:
        print(f"Error: {err}")
    
    connection.close()


update_product()








      #delete_product

import pymysql
from pymysql import MySQLError

def delete_product():
    try:
        
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="Beautyshop"
        )
        
        
        with connection.cursor() as cursor:
            product_name = input("Enter the product name: ")
            
            
            check_query = "SELECT unit_price FROM beauty_products WHERE product_name=%s"
            cursor.execute(check_query, (product_name,))
            result = cursor.fetchone()
            
            if result:
                
                delete_query = "DELETE FROM beauty_products WHERE product_name=%s"
                cursor.execute(delete_query, (product_name,))
                connection.commit()
                print(f"Product '{product_name}' deleted successfully.")
            else:
                print(f"Product '{product_name}' is unavailable.")
    
    except MySQLError as err:
        print(f"Error: {err}")
    
    
        
        connection.close()



delete_product()








# 2.REVIEW

     #add_review

import pymysql
import tabulate
try:
    db=pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Beautyshop"
    )
except pymysql.error as err:
        print("ERROR",err)
    
cursor=db.cursor()

def add_review():
      
      try:
            Customer_name=input("ENTER THE CUSTOMER_NAME:");
            Product_name=input("ENTER THE PRODUCT_NAME:");
            Mobile_number=input("ENTER THE MOBILE_NUMBER:");
            Review=input("ENTER THE REVIEW:");
            
            cursor.execute('''
            insert into review(customer_name,product_name,mobile_number,review)
            values (%s,%s,%s,%s)
            ''',(Customer_name,Product_name,Mobile_number,Review))
            
            db.commit()
            print("product added successfully")
      except Exception as err:
            print("ERROR",err)



add_review()


db.close()








   #view_review

import pymysql
import tabulate
try:
    db=pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="Beautyshop"
    )
except pymysql.error as err:
        print("ERROR",err)
    
cursor=db.cursor()

def view_review():
    '''view all products in the review table'''
      
    try:
        cursor.execute("select * from review")
        result=cursor.fetchall()
        headers=[desc[0] for desc in cursor.description]
        print(tabulate.tabulate(result,headers=headers,tablefmt="grid"))
    except Exception as err:
        print("Error",err)
    



view_review()
   


db.close()




#COMBINE FUNCTIONS

while True:
     
    try:
         print("\n WELCOME TO PYTHON COSMETIC SHOP")
         print()
         print("1.add_product")
         print("2.view_product")
         print("3.update_product")
         print("4.delete_product")
         print("5.add_review")
         print("6.view_review")
         print("7.Exit")
         choice=int(input("ENTER YOUR CHOICE(1-7):"))
         print()

         if choice==1:
              add_product()
         elif choice==2:
              view_product()
         elif choice==3:
              update_product() 
         elif choice==4:
              delete_product()
         elif choice==5:
              add_review()
         elif choice==6:
              view_review() 
         elif choice==7:
              print("THANK YOU...") 
              exit()
         elif choice <0:
              print("POSITIVE")  
         else:
              print("INVALID CHOICE.PLEASE SELECT A VALID OPTION(1-7).") 
    except Exception as err:
         print("\n PLEASE ENTER THE NUMERIC VALUE") 




db.close()                         
        
         



    
                            
                  
              
     
 
     
     
          

       

