# Real World Project Practice Personal expense tracker CLI Project

# List of Expenses in the form of Dictionary
expensesList = []

print("Welcome to the Personal Expense Tracker CLI Application: ")

while True:
    print("========MENU========")
    print("1. Add a Expense ")
    print("2. View Expenses ")
    print("3. Update Expenses ")
    print("4. Delete Expenses ")
    print("5. Total Number of Expenses ")
    print("6. Total Amount of Expenses ")
    print("7. Exit ")


    choice = int(input("Enter your choice: "))

    if choice == 1:

        date = input("Enter the Date of Expense : ")
        category = input("Enter the Category of the Expense : ")
        description = input("Enter the Details of the Expense : ")
        amount = input("Enter the Amount of the Expense : ")

        expense = {
            "Date": date,
            "Category": category,
            "Description": description,
            "Amount": amount
        }

        expensesList.append(expense)

        print("\n The Expense is successfully added to the Expenses List ")

    elif choice == 2:

        if len(expensesList)==0:
            print("\n The Expenses List is empty ")
        else:

            print("========THESE ARE YOUR EXPENSES========")
            count = 1
            for expense in expensesList:
                print(f" {count}: {expense["Date"]} , {expense["Category"]} , {expense["Description"]} , {expense["Amount"]} ")
                count += 1

    elif choice == 3:

        if len(expensesList)==0:
            print("\n The expenses list is empty ")
        else:
            print("========UPDATE EXPENSES========")

            for i, expense in enumerate(expensesList, start=1):

                print(f"{i}: {expense["Date"]} , {expense["Category"]} , {expense["Description"]} , {expense["Amount"]} ")

                update_index = int(input("Enter the expense number to update: ")) - 1

                if 0 <= update_index < len(expensesList):
                    print("\nEnter new details : ")

                    new_date = input("New Date : ")
                    new_category = input("New Category : ")
                    new_description = input("New Description : ")
                    new_amount = input("New amount : ")

                    if new_date:
                        expensesList[update_index]["Date"] = new_date
                    if new_category:
                        expensesList[update_index]["Category"] = new_category
                    if new_description:
                        expensesList[update_index]["Description"] = new_description
                    if new_amount:
                        expensesList[update_index]["Amount"] = new_amount

                    print("\n The Expenses List is successfully updated ")

                    print("\n========UPDATED EXPENSE LIST========")

                    for index, expense in enumerate(expensesList, start=1):
                        print(f"{index} : {expense['Date']} | {expense['Category']} | {expense['Description']} | {expense['Amount']} ")

                else:
                    print("\n Invalid expense number ")

    elif choice == 4:

        if len(expensesList) == 0:
            print("\n The Expenses List is empty ")

        else:
            print("========DELETE EXPENSES========")
            for i, expense in enumerate(expensesList, start=1):
                print(f"{i}: {expense["Date"]} , {expense["Category"]} , {expense["Description"]} , {expense["Amount"]} ")

                delete_index = int(input("Enter the expense number to delete: ")) - 1

                if 0 <= delete_index < len(expensesList):
                    deleted_expense = expensesList.pop(delete_index)
                    print("\n The Expense is successfully deleted ")

                    if len(expensesList) == 0:
                        print("\n The Expense List is empty now ")
                    else:
                        print("========UPDATED EXPENSES LIST========")
                        for index, expense in enumerate(expensesList, start=1):
                            print(f"{index} : {expense['Date']} | {expense['Category']} | {expense['Description']} | {expense['Amount']} ")
                else:
                    print("\n Invalid expense number ")

    elif choice == 5:

        print(f"The total number of Expenses you have done are: {len(expensesList)}")

    elif choice == 6:

        if len(expensesList) == 0:
            print("\n  The Expenses List is empty ")
        else:
            total_expenses = 0

            for expense in expensesList:
                total_expenses += int(expense["Amount"])

            print("========TOTAL EXPENSE AMOUNT=======")
            print(f"Total Amount Spent: {total_expenses}")

    elif choice == 7:
        print("\n Thankyou for using this Expense Tracking Application")
        print(" Exiting the program................")
        break

    else:
        print("\n Invalid choice ")








