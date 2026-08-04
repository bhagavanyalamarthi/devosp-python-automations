import shutil

total, usage, free = shutil.disk_usage("/")

print("Printing disk usage")

print(f"Total disk: {total // (1024**3)} GB")
print(f"Used disk: {usage // (1024**3)} GB")
print(f"Free disk: {free // (1024**3)} GB")

used = (usage / total) * 100

print(f"Disk usage: {used:.2f}%")

if used > 80:
    print("Alert: Disk usage is above 80%")
else:
    print("Disk usage is normal")
