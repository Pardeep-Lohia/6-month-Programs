import random
from datetime import datetime, timedelta

ACTIONS = ["LOGIN", "LOGOUT", "UPLOAD", "DOWNLOAD", "DELETE"]
STATUS = ["SUCCESS", "FAIL"]

def generate_log_line(ts):
    user_id = random.randint(1, 5000)
    action = random.choice(ACTIONS)
    status = random.choice(STATUS)

    return f"{ts} | USER_ID={user_id} | ACTION={action} | STATUS={status}"

def generate_file(filename="logs.txt", n=100000):
    start_time = datetime(2026, 1, 8, 12, 0, 0)

    with open(filename, "w") as f:
        for i in range(n):
            ts = start_time + timedelta(seconds=i)

            # Inject some corrupted lines (5%)
            if random.random() < 0.05:
                f.write("corrupted line without proper format\n")
            else:
                f.write(generate_log_line(ts) + "\n")

    print(f"Generated {n} lines in {filename}")

if __name__ == "__main__":
    generate_file(n=200000)   # change size here
