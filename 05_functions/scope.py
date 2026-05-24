loyalty_points=0
transactions = [100,300, 550,530,900]
def process_transactions(transactions: list[int]) -> int:
    total =0
    def apply_bonus():
        nonlocal total
        for transaction in transactions:
            total += transaction
        if total > 1000:
            total += 50
    apply_bonus()
    global loyalty_points 
    loyalty_points = total // 100
    return total

total_returned = process_transactions(transactions)
print(f"total amount: {total_returned}")
print(f"Loyalty points: {loyalty_points}")

