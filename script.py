import csv
from datetime import datetime

def generate_csv():
    data = [
        ["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 24, "San Francisco"],
        ["Charlie", 29, "Boston"],
        ["Chaplin", 39, "Koston"]
    ]

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')  # Current date and time
    filename = f"data_{timestamp}.csv"  # Use timestamp in the filename

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    return filename

if __name__ == "__main__":
    filename = generate_csv()
    print(f"CSV file generated: {filename}")
