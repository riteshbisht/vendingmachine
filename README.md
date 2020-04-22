# Vending Machine

##### create virtual environment

###### Install Dependency
     pip install -r requirement.txt

###### RUN Migration
     python manage.py migrate
     
###### Load Data
     python manage.py load_data

- Create VendingMachine, Items , User, and Attach Vending Machinne to User

###### Run server
     python manage.py runserver

###### Features
- Can Add items in vending Machine
- Can upadte value of items attached to veding machine
- Can Buy on item at a time from Vending Machine.


###### Models
- ITems
      - All the Items

- VendingMachine
       - All the Machine

- Inventory
       Items to vending Machine attachement with curr count of items.

- VendingMAchineUser
      User Attached To VendingMachine who can update add item to vending machine

- Buy User
      User mobile number ot buy the items.

- User
     django User for login/logout
