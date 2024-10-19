"""1. Any authenticated user can post antique products (with title, image, description, and
starting price) in the portal.
2. Home page should list all products posted by the other users. User shouldn’t see the product
which is posted by him in the listing.
3. User can click the listed item and could see the detail page of the posted product. Detail
page should also allow user to post their price(bidding/auction).
a. Bidding price should be greater than starting price or last bidding price (whichever is
higher)

4. Every user should have page called “my listing” where he can see his own postings and also
view biddings placed for their posting. Provide option to close bidding. At closing the
product should be allotted to last bidding price (highest price)."""



users = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}  
      
def login():  
    username = input("Enter your username: ")  
    password = input("Enter your password: ")  
      
    if username in users and users[username] == password:  
        print("Login successful. Now post your products with title, image, description, and starting price in the portal!")
        product_dict1= {}
        
        warning = input("Enter c to continue and q to exit: ")  
        
        while warning =="c":
            title = input("Enter title: ")  
            image = input("Enter image: ")  
            description = input("Enter description: ")  
            startingPrice = input("Enter starting price: ") 
        
            product_dict = {'title':title,'image':image,'Description':description,'StartingPrice':startingPrice}
            
            if product_dict not in product_dict1.values():
                product_dict1.update(product_dict)
                print(product_dict1)
                warning = input("Enter c to continue and q to exit: ")  
                
                if warning =="q":
                    print("Thank You!")
                    
                    listings = input("do you wanna see your own listings? (Yes or No): ") 
                    if listings == "Yes":
                        print(f"Below are your listings {product_dict1} and {product_dict}")
                    else:
                        print("ok!")
                    break
    else:  
        print("Invalid username or password. Please try again.")  
        
      
login() 






