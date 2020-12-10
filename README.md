# Cofi code challenge

Test development for Cofi company. This code simulate a physical store who
sells products. A discount may or may not have been applied to these products.

#### Products file
All the products of the store are saved in a json file called **"products.json"**
You can edit this file to add, modified or remove whatever product.

#### Config file
To config the application we can do it through **"config.py"** file. We have
a constat called *URL.JSON_PRODUCTS* where you can find the route to the **"products.json"**
file.

Right now its value is:

*URL.JSON_PRODUCTS* = "./products.json"

Other constants with their values are:

* *DISCOUNT_ACTIVE.VOUCHER* = True
* *DISCOUNT_ACTIVE.TSHIRT* = True
* *DISCOUNT_ACTIVE.MUG* = False

They have the default configuration which are the requirements asked.

#### Libraries
No any special library added. 

Python version: 3.6.5

#### Extra functionalities
I have added some extra functionalities who rich the development
* Possibility to apply or not the discounts creating the constants before mentioned
    *DISCOUNT_ACTIVE.VOUCHER*, *DISCOUNT_ACTIVE.TSHIRT*, *DISCOUNT_ACTIVE.MUG*

* Control about products which are not in the catalog of products of the store.
If you try to introduce a product which are not in the store you will get a message
about it

#### How to run the tests
Test files you can find them in *test* folder. You can run tests from
application folder whith this code:

````
python3 -m unittest /route_to_application/test/test_application.py
````

#### How to run the application
You can do it in two different ways:
1. Executing the application from console with this command:
    ````
    $python3 main.py
    ````
    If you edit main.py you can modify the products modifying the list with name *products* 

2. Run code python interactively:

    To do this, you have to open a shell and call to python with this
    command: 
    ````
    >>>python3
    ````
    After this command you will import the object which we are going to 
    use after with this command: 
    ````
    >>>from checkout import CheckOut
    ````
    Now, you can create an instance of the object:
    ````
    >>>c = CheckOut()
    ````
    
    After create the instance you will be able to scan products:
    ````
    >>>c.scan("VOUCHER")
    ````
    
    And finally, you can get the total ammount of the cart with: 
    ````
    >>>print(f"Total: {c.total()})
    ````
   
