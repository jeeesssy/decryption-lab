# run.py - vulnerable example for the lab
import subprocess

def ping_host(ip):
    # unsafe: executes user input as command
    subprocess.run(["ping", ip])

if __name__ == "__main__":
    host = input("Enter host to ping: ")
    ping_host(host)
