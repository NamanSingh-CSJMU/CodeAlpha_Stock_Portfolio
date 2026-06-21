# TASK 2: Stock Portfolio Tracker
# This program tracks a user's stock portfolio using a hardcoded dictionary
# and saves a summary report to a text file upon exit.

def main():
    # 1. Hardcoded dictionary for stock prices (No live API required)
    STOCK_PRICES = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "MSFT": 420.0,
        "AMZN": 175.0,
        "GOOG": 160.0
    }
    
    # Dictionary to keep track of the user's owned stocks and quantities
    portfolio = {}
    
    print("Welcome to the Stock Portfolio Tracker!")
    
    # 2. Main interactive console loop
    while True:
        print("\n--- Main Menu ---")
        print("1. Add / Update Stock")
        print("2. View Portfolio Summary")
        print("3. Exit and Save Report")
        
        choice = input("Please select an option (1-3): ").strip()
        
        if choice == "1":
            print(f"\nAvailable stocks: {', '.join(STOCK_PRICES.keys())}")
            # Ensure case-insensitivity by converting input to uppercase
            ticker = input("Enter stock ticker name: ").strip().upper()
            
            # Validation: Check for invalid stock names
            if ticker not in STOCK_PRICES:
                print("Error: Invalid stock. Please choose from the available list.")
                continue
                
            qty_str = input(f"Enter the number of shares for {ticker}: ").strip()
            
            # Validation: Check for non-numeric or negative inputs
            try:
                quantity = int(qty_str)
                if quantity < 0:
                    print("Error: Quantity cannot be a negative number.")
                    continue
                
                # Update the portfolio (adds to existing quantity if already owned)
                portfolio[ticker] = portfolio.get(ticker, 0) + quantity
                print(f"Success! {quantity} shares of {ticker} added to your portfolio.")
                
            except ValueError:
                print("Error: Invalid input. Please enter a whole number.")
                
        elif choice == "2":
            print("\n--- Current Portfolio ---")
            if not portfolio:
                print("Your portfolio is currently empty.")
            else:
                total_investment = 0.0
                # 3. Calculation of individual and total values
                for stock, qty in portfolio.items():
                    price = STOCK_PRICES[stock]
                    value = price * qty
                    total_investment += value
                    print(f"{stock}: {qty} shares @ ${price:.2f} = ${value:.2f}")
                    
                print("-" * 25)
                print(f"Total Investment Value: ${total_investment:.2f}")
                
        elif choice == "3":
            # 4. File Handling: Save report on exit
            if not portfolio:
                print("\nPortfolio is empty. Exiting without saving a report.")
                break
                
            try:
                with open("portfolio_report.txt", "w") as file:
                    file.write("=== Final Portfolio Summary ===\n")
                    total_investment = 0.0
                    
                    for stock, qty in portfolio.items():
                        price = STOCK_PRICES[stock]
                        value = price * qty
                        total_investment += value
                        file.write(f"{stock}: {qty} shares @ ${price:.2f} = ${value:.2f}\n")
                        
                    file.write("-" * 31 + "\n")
                    file.write(f"Total Investment Value: ${total_investment:.2f}\n")
                    
                print("\nSuccess: 'portfolio_report.txt' has been saved.")
                print("Exiting tracker. Have a great day!")
                
            except Exception as e:
                print(f"\nAn error occurred while saving the file: {e}")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Standard Python boilerplate to call the main function
if __name__ == "__main__":
    main()