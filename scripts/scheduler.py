import schedule
import time
import subprocess

def run_pipeline():
    subprocess.run(["python", "ingest.py"])
    subprocess.run(["python", "process.py"])

schedule.every().day.at("07:00").do(run_pipeline)

if __name__ == "__main__":
    print("Scheduler started...")
    while True:
        schedule.run_pending()
        time.sleep(60)

