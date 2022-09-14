import subprocess

# Launching Microsoft Paint
paint_process = subprocess.Popen("C:\Program Files\WindowsApps\Microsoft.Paint_11.2206.6.0_x64__8wekyb3d8bbwe\PaintApp\mspaint.exe")


# Checking if the Paint application is still open using poll() method
print(paint_process.poll() == None)
