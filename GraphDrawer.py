import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("mix_hand_and_screw_data.csv")

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.plot(df["timestamp_mills_ms"], df["GX"], label="GX")
plt.plot(df["timestamp_mills_ms"], df["GY"], label="GY")
plt.plot(df["timestamp_mills_ms"], df["GZ"], label="GZ")
plt.xlabel("Time (milliseconds)")
plt.ylabel("Acceleration")
plt.title("Acceleration over Time")
plt.legend()
plt.grid(True)
plt.show()
