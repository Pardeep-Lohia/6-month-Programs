from collections import defaultdict
import heapq

FILE_NAME = "logs.txt"
TOP_K = 3

user_count = defaultdict(int)
actions = set()
total_events = 0
failed_events = 0

# Read file line by line
with open(FILE_NAME, "r") as file:
    for line in file:
        try:
            parts = line.strip().split("|")
            if len(parts) != 4:
                continue

            user_id = int(parts[1].split("=")[1])
            action = parts[2].split("=")[1]
            status = parts[3].split("=")[1]

            # Update stats
            total_events += 1
            user_count[user_id] += 1
            actions.add(action)

            if status == "FAIL":
                failed_events += 1

        except:
            # Ignore broken lines
            continue


# Get top K users
top_users = heapq.nlargest(TOP_K, user_count.items(), key=lambda x: x[1])

print("Top Users:")
for user, count in top_users:
    print(user, count)

print("\nStats:")
print("Total Users    :", len(user_count))
print("Total Events   :", total_events)
print("Failed Events  :", failed_events)
print("Unique Actions :", len(actions))
