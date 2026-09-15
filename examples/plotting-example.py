import pandas as pd
import matplotlib.pyplot as plt

# Expected columns for a reconstructed dataset:
# distance, jamming, throughput_mbps

df = pd.read_csv("results.csv")
df_off = df[df["jamming"] == False]
df_on = df[df["jamming"] == True]

plt.plot(df_off["distance"], df_off["throughput_mbps"], marker="o", label="Interference OFF")
plt.plot(df_on["distance"], df_on["throughput_mbps"], marker="o", label="Interference ON")
plt.xlabel("Distance (m)")
plt.ylabel("Throughput (Mbps)")
plt.title("Throughput vs Distance")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
