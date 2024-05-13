# Phase 3 CLI+ORM Project Template

## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

---

## Introduction

For this project I have for you a program that creates a database with 2 tables, Suppliers and Items, this is meant to act as an inventory manager for a warehouse that needs to keep track of the items and that items supplier. To mimic this the 2 classes have a one-many relationship, the items must keep track of there supplier in this case. This program uses CLI to take in user input to list, create, update or delete either from the items table or the suppliers table.

## TO RUN
You will need open your terminal and navigate to the place you have this project stored.

1. Run pip install to install dependencies and run pipenv shell.
2. run "python lib/cli.py" to be propmted with questions regarding the databases


## Description
This is a CLI run application that is made to replicate an inventory management system between a supplier and the item that they produce. the design of this project is to make sure that the items keep track of their suppliers that they are attached too. To ensure this there is a one-to-many relationship between the 2 classes. As you will see whenever you run this program you will be presented with 10 choices from a list like prompt to choose from to search by id, create, update or delete from either table. 


## Conclusion
I got the idea for this project from knowledge of how warehouse or distribution plants control their knowledge of their inventory throughout the plant and warehouses keeping track of where certain items come from and how many of that item that there is. 