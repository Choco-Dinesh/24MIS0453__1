records = [
    {"vehicle": "TN01AB1234", "type": "car", "hours": 6},
    {"vehicle": "TN02XY5678", "type": "bike", "hours": 3},
    {"vehicle": "TN03CD9012", "type": "car", "hours": 2},
    {"vehicle": "TN04EF3456", "type": "bike", "hours": 8},
    {"vehicle": "TN05GH7890", "type": "car", "hours": 5},
]

CAR_RATE = 5
BIKE_RATE = 2

for record in records:
    if record["type"] == "car":
        record["fee"] = record["hours"] * CAR_RATE
    elif record["type"] == "bike":
        record["fee"] = record["hours"] * BIKE_RATE
    else:
        record["fee"] = 0

total_revenue = sum(record["fee"] for record in records)

highest_fee_record = max(records, key=lambda r: r["fee"])

more_than_5_hours = [record for record in records if record["hours"] > 5]

sorted_records = sorted(records, key=lambda r: r["fee"], reverse=True)

print("Parking Records:")
for record in records:
    print(f"- {record['vehicle']} | {record['type']} | {record['hours']} hours | fee: ${record['fee']}")

print(f"\nTotal revenue: ${total_revenue}")
print(f"Vehicle with highest parking fee: {highest_fee_record['vehicle']} (${highest_fee_record['fee']})")

print("\nVehicles parked more than 5 hours:")
if more_than_5_hours:
    for record in more_than_5_hours:
        print(f"- {record['vehicle']} | {record['type']} | {record['hours']} hours | fee: ${record['fee']}")
else:
    print("- None")

print("\nRecords sorted by parking fee (descending):")
for record in sorted_records:
    print(f"- {record['vehicle']} | {record['type']} | {record['hours']} hours | fee: ${record['fee']}")
