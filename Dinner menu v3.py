print("Welcome to My Restaurant!")
print("="*25) 

ordered_items = []
total_cook_time = 0

while True:
    print("\nOur menu:")
    
    with open("menu.txt") as f:
        for line in f:
            item_code, item_name, cook_time = line.strip().split(",")
            print(f"{item_code} - {item_name} ({cook_time} mins)")

    code = input("\nEnter item code (X to finish): ").upper()
    
    if code == "X":
        break
    
    with open("menu.txt") as f: 
        for line in f:
            data = line.strip().split(",")
            if data[0] == code:
                item_name = data[1]
                cook_time = int(data[2])
                
                print(f"\nAdding {item_name} - {cook_time} mins cook time")
                
                ordered_items.append(item_name)
                total_cook_time += cook_time
                
print("\nYour order:")
for item in ordered_items:
    print(f"- {item}")
    
print(f"\nTotal cook time: {total_cook_time} mins")
print("Thank you for your order!")