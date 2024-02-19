def calculate_tax(bill, tax_rate):
    total_tax = round((bill * tax_rate) / 100.00,2)
    print('Total tax:', total_tax)
    return total_tax
    

calculate_tax(175,15)
