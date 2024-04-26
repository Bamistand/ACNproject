import time
import math
from fastapi import FastAPI
import threading

app = FastAPI()

def generate_cpu_load(interval, utilization):
    "Generate a utilization % for a duration of interval seconds"
    while True:  #  loop 
        start_time = time.time()
        while time.time() - start_time < interval:
            print("About to do some arithmetic")
            end_time = time.time() + (utilization / 100.0)
            while time.time() < end_time:
                a = math.sqrt(64 * 64 * 64 * 64 * 64)
        print("About to sleep")
        time.sleep(60)  # Pause for 1 minute

@app.get("/")
def read_root():
    return {"message": "CPU load generation started"}

# Start the CPU load generation in a new thread as soon as the server is run
threading.Thread(target=generate_cpu_load, args=(60, 100)).start()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
