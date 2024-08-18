# Import required libraries
import csv
import os

# Define function to create a new invoice
def create_invoice(invoice_number, date, customer_name, address, phone, email, items):
    # Set file path
    file_path = f"Invoice_{invoice_number}.csv"
    
    # Check if file already exists
    if os.path.exists(file_path):
        print("Invoice already exists!")
    else:
        # Write invoice details to CSV file
        with open(file_path, mode='w', newline='') as invoice_file:
            fieldnames = ['Item', 'Quantity', 'Price']
            writer = csv.DictWriter(invoice_file, fieldnames=fieldnames)
            
            # Write header row
            writer.writeheader()
            
            # Write item details
            for item in items:
                writer.writerow({'Item': item[0], 'Quantity': item[1], 'Price': item[2]})
            
            # Write footer rows for subtotal, taxes, and total
            subtotal = sum([item[1] * item[2] for item in items])
            taxes = 0.1 * subtotal
            total = subtotal + taxes
            
            writer.writerow({})
            writer.writerow({'Item': 'Subtotal', 'Quantity': '', 'Price': subtotal})
            writer.writerow({'Item': 'Taxes', 'Quantity': '', 'Price': taxes})
            writer.writerow({'Item': 'Total', 'Quantity': '', 'Price': total})
            
            # Write customer details
            writer.writerow({})
            writer.writerow({'Item': 'Customer Name:', 'Quantity': '', 'Price': customer_name})
            writer.writerow({'Item': 'Address:', 'Quantity': '', 'Price': address})
            writer.writerow({'Item': 'Phone:', 'Quantity': '', 'Price': phone})
            writer.writerow({'Item': 'Email:', 'Quantity': '', 'Price': email})
            
            print(f"Invoice {invoice_number} created successfully!")
        
# Example usage
create_invoice(1001, '2022-01-01', 'John Doe', '123 Main St', '555-1234', 'john.doe@example.com', [('Product A', 2, 10.99), ('Product B', 3, 5.99)])
