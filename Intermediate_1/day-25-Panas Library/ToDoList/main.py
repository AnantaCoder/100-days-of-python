import pandas 
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os
database = pandas.read_csv(r'database.csv')
print(database.head())

def addtask():
    task = input("Enter your task: ")
    date = datetime.datetime.now()
    done = False
    database.loc[len(database)] = [task, date, done]
    
    print("Task added successfully")
    print(database.describe())
    
def viewtask():
    print(database.head())

def markdone():
    task = input("Enter the task you want to mark as done: ")
    for i in range(len(database)):
        if database['task'][i] == task:
            database.loc[i, 'done'] = True
            print("Task marked as done")
            print(database.head())
            break
    else:
        print("Task not found")
        
def delete():
    task = input("Enter the task you want to delete: ")
    for i in range(len(database)):
        if database['task'][i] == task:
            database.drop(i, inplace=True)
            print("Task deleted successfully")
            print(database.head())
            break
    else:
        print("Task not found")
        
def save():
    database.to_csv('database.csv', index=False)
    print("Data saved successfully")

def main():
    while True:
        print("1. Add task")
        print("2. View task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Save and exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            addtask()
        elif choice == '2':
            viewtask()
        elif choice == '3':
            markdone()
        elif choice == '4':
            delete()
        elif choice == '5':
            save()
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            
# if __name__ == '__main__':
main()
    