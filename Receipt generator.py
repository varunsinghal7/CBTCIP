from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

def create_receipt(customer_name, items, total_amount):
    # Create a new PDF document
    c = canvas.Canvas("receipt.pdf", pagesize=letter)

    # Set font
    c.setFont("Helvetica", 12)

    # Add title
    c.drawString(inch, 10.5 * inch, "Receipt")

    # Add customer information
    c.drawString(inch, 10 * inch, f"Customer: {customer_name}")

    # Add items list
    y_position = 9.5 * inch
    for item in items:
        c.drawString(inch, y_position, f"{item['name']}: ${item['price']:.2f}")
        y_position -= 0.2 * inch

    # Add total amount
    c.drawString(inch, y_position - 0.5 * inch, f"Total: ${total_amount:.2f}")

    # Save the PDF
    c.save()

# Example usage
customer_name = "Jane Doe"
items = [
    {"name": "Product 1", "price": 10.99},
    {"name": "Product 2", "price": 25.50},
]
total_amount = sum([item['price'] for item in items])

create_receipt(customer_name, items, total_amount)  