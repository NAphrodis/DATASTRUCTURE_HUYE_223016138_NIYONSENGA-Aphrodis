# 7.	Store the monthly expenses for each category (e.g., rent, food, utilities) for 6 months in a 2D list and calculate the average monthly expense per category.
expenses = [
    [1200, 300, 150],  
    [1200, 350, 100],  
    [1200, 400, 200],  
    [1200, 320, 180],  
    [1200, 330, 150],  
    [1200, 310, 170]   
]
average_expenses = [sum(x) / len(expenses) for x in zip(*expenses)]
print(average_expenses)  # Output: [1200.0, 335.0, 158.33333333333334]
