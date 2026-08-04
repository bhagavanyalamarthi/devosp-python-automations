import subprocess
result = subprocess.run(
         ["free", "-m"],
         capture_output=True,
         text = True)
print(result.stdout)

if result.returncode == 0:
  print ("commend excuted sucessfully")
else:
  print("command excuted failed")

if "mem" in result.stdout:
    print ("memory info found")
else:
    print ("not found")

