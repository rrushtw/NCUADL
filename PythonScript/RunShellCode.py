import subprocess

command = "whoami"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Print the output
print(result.stdout.decode())
