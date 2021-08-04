import subprocess
import time

while True:
    subprocess.run(["python3","trend_scraping.py"])
    time.sleep(60)
