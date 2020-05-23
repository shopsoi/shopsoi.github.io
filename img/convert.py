import os
import subprocess
import sys
import shlex

# sizes = [
#     (400, 172),
#     (600, 257),
#     (800, 343),
#     (1000, 429),
#     (1200, 515),
#     (1400, 601),
#     (1578, 677)]
sizes = [(400, 176),
(600, 264),
(800, 352),
(1000, 439),
(1200, 527),
(1400, 615),
(1600, 703)],
(1800, 791)]

directory = r'/mnt/c/Users/Naums/shopsoi.github.io/img'
filename = "group-photo-1578.png"
# for filename in os.listdir(directory):
#     if filename.endswith(".jpg") and not filename.startswith("header-bg"):
for size in sizes:
    path = os.path.join(directory, filename)
    cmd = ['cwebp.exe', '-q', '90', '-resize', str(size[0]), str(size[1]), filename, '-o', 
        filename.replace(".png", ".webp").replace("1578", str(size[0]))]
    print(filename)
    print(cmd)
    process = subprocess.Popen(cmd,
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    for output in process.stdout.readlines():
        print(output.strip().decode())
    for output in process.stderr.readlines():
        print(output.strip().decode())
    # else:
    #     continue