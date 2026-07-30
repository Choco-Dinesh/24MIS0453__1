records = [
    {"name": "Asha", "vaccine": "Covaxin", "age": 65, "doses": 2},
    {"name": "Ravi", "vaccine": "Covishield", "age": 45, "doses": 1},
    {"name": "Meera", "vaccine": "Covaxin", "age": 59, "doses": 2},
    {"name": "Suresh", "vaccine": "Sputnik", "age": 70, "doses": 2},
    {"name": "Priya", "vaccine": "Covishield", "age": 62, "doses": 2},
    {"name": "Kiran", "vaccine": "Covaxin", "age": 30, "doses": 1},
]

FULL_VACCINE_DOSES = 2

for record in records:
    record["full_vaccinated"] = record["doses"] >= FULL_VACCINE_DOSES

full_vaccinated_count = sum(1 for record in records if record["full_vaccinated"])
total_count = len(records)
full_vaccinated_percent = (full_vaccinated_count / total_count) * 100 if total_count else 0

senior_citizens = [record for record in records if record["age"] >= 60]

vaccine_usage = {}
for record in records:
    vaccine_usage[record["vaccine"]] = vaccine_usage.get(record["vaccine"], 0) + 1

most_used_vaccine = max(vaccine_usage, key=vaccine_usage.get)

sorted_by_age = sorted(records, key=lambda r: r["age"], reverse=True)

print("Vaccination Records:")
for record in records:
    status = "Full" if record["full_vaccinated"] else "Partial"
    print(f"- {record['name']} | {record['vaccine']} | age {record['age']} | doses {record['doses']} | {status}")

print(f"\nCount of fully vaccinated individuals: {full_vaccinated_count}")
print(f"Percentage of fully vaccinated people: {full_vaccinated_percent:.1f}%")
print(f"Most used vaccine: {most_used_vaccine}")

print("\nSenior citizens (age >= 60):")
if senior_citizens:
    for record in senior_citizens:
        print(f"- {record['name']} | {record['vaccine']} | age {record['age']} | doses {record['doses']}")
else:
    print("- None")

print("\nRecords sorted by age (descending):")
for record in sorted_by_age:
    print(f"- {record['name']} | {record['vaccine']} | age {record['age']} | doses {record['doses']}")
