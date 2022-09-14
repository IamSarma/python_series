import subprocess

# Launching Microsoft Paint
# paint_process = subprocess.Popen(
#     "C:\Program Files\WindowsApps\Microsoft.Paint_11.2206.6.0_x64__8wekyb3d8bbwe\PaintApp\mspaint.exe")


# Checking if the Paint application is still open using poll() method
# print(paint_process.poll() == None)


# Block until the Paint application is closed/quit
# paint_process.wait()
# print(paint_process.poll() != None)


# Passing argument(s) to Popen() method
# subprocess.Popen([r"C:\Windows\System32\notepad.exe",
#                  r"D:\Projects\python_series\open_with_Popen.txt"])


# Opening file(s) with default application(s)
subprocess.Popen(["start", "open_me.txt"], shell=True)
