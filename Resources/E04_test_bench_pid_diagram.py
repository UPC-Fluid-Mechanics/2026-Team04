"""
Auxiliary Script 04: ISO 5801 Test Bench & Instrumentation Layout (P&ID Schematic)
Generates a high-resolution schematic ('test_bench_pid.png') for PROJECT.md.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(14, 7.2))
ax.set_xlim(0, 14)
ax.set_ylim(0, 7.5)
ax.axis("off")

# Title Header
ax.text(7.0, 7.15, "UNE-EN ISO 5801:2019 (Category A) — Test Bench & Instrumentation P&ID",
        ha="center", va="center", fontsize=14, fontweight="bold", color="#111111")
ax.text(7.0, 6.80, "Test Specimen: Soler & Palau HCFB/4-630/H (D1 = 0.630 m)  |  Inlet Settling Chamber (3.50 m × 1.60 m × 1.60 m)",
        ha="center", va="center", fontsize=10, color="#444444")

# ==============================================================================
# 1. AERODYNAMIC FLOW PATH (TOP / MIDDLE BAND: y = 3.2 to 5.4)
# ==============================================================================
# Ambient Inlet Arrow
ax.annotate("", xy=(0.9, 4.3), xytext=(0.15, 4.3),
            arrowprops=dict(arrowstyle="->", lw=2.5, color="#0277bd"))
ax.text(0.5, 4.65, "Ambient\nAir", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#0277bd")

# Motorized Throttling Damper
ax.add_patch(patches.Rectangle((0.95, 3.85), 0.75, 0.9, facecolor="#e1f5fe", edgecolor="#01579b", lw=1.8))
ax.plot([1.05, 1.60], [3.95, 4.65], color="#01579b", lw=2)
ax.text(1.32, 3.55, "Throttling\nDamper", ha="center", va="top", fontsize=8.5, fontweight="bold")

# Duct connector
ax.plot([1.70, 2.05], [4.55, 4.55], color="black", lw=1.5)
ax.plot([1.70, 2.05], [4.05, 4.05], color="black", lw=1.5)

# Auxiliary VFD Booster Fan
ax.add_patch(patches.Rectangle((2.05, 3.75), 1.05, 1.1, facecolor="#e1f5fe", edgecolor="#01579b", lw=1.8))
ax.text(2.57, 4.30, "Auxiliary\nBooster\nFan", ha="center", va="center", fontsize=8.5, fontweight="bold")
ax.text(2.57, 3.55, "VFD (0–50 Hz)", ha="center", va="top", fontsize=8, color="#01579b")

# Conical transition to chamber
ax.plot([3.10, 3.55], [4.85, 5.35], color="black", lw=1.8)
ax.plot([3.10, 3.55], [3.75, 3.25], color="black", lw=1.8)

# Main Settling Chamber Outer Box (x = 3.55 to 10.55, y = 3.25 to 5.35)
ax.add_patch(patches.Rectangle((3.55, 3.25), 7.00, 2.10, facecolor="#fafafa", edgecolor="#222222", lw=2.2))

# Upstream Screen (60%)
ax.plot([4.35, 4.35], [3.25, 5.35], color="#757575", ls=":", lw=1.6)
ax.text(4.35, 5.50, "Screen\n(60%)", ha="center", va="bottom", fontsize=7.5, color="#555555")

# Multi-Nozzle Bulkhead at x = 5.35
ax.plot([5.35, 5.35], [3.25, 5.35], color="#0d47a1", lw=3.5)
for ny in [4.75, 3.85]:
    ax.add_patch(patches.Rectangle((5.35, ny - 0.22), 0.35, 0.44, facecolor="#bbdefb", edgecolor="#0d47a1", lw=1.5))
ax.text(5.35, 5.55, "Multi-Nozzle Bulkhead\n(2×Ø315, Ø224, Ø160)", ha="center", va="bottom", fontsize=8, fontweight="bold", color="#0d47a1")

# 3 Settling Screens (60%, 50%, 45%)
for sx, lbl in [(7.35, "60%"), (7.80, "50%"), (8.25, "45%")]:
    ax.plot([sx, sx], [3.25, 5.35], color="#616161", ls="--", lw=1.6)
ax.text(7.80, 5.50, "Settling Screens\n(60% / 50% / 45%)", ha="center", va="bottom", fontsize=8, color="#424242")

# Piezometric Ring Plane (x = 9.90, 0.5*D1 upstream of fan)
ax.plot([9.90, 9.90], [3.25, 5.35], color="#c62828", ls="-.", lw=1.4)
ax.plot([9.90, 9.90], [3.25, 5.35], "o", color="#c62828", markersize=6)
ax.text(9.85, 5.50, "4-Tap Piezometric\nRing (0.5·D1)", ha="center", va="bottom", fontsize=8, fontweight="bold", color="#c62828")

# Tested Axial Fan (S&P HCFB/4-630/H) at x = 10.55
ax.add_patch(patches.Rectangle((10.55, 3.65), 0.55, 1.30, facecolor="#c8e6c9", edgecolor="#1b5e20", lw=2.2))
ax.text(10.82, 4.30, "S&P\nFan", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#1b5e20")

# Inline Rotary Torque & Speed Sensor + Motor on Shaft
ax.plot([11.10, 12.25], [4.30, 4.30], color="#333333", lw=3.0)  # Shaft
ax.add_patch(patches.Rectangle((11.30, 4.02), 0.55, 0.56, facecolor="#fff9c4", edgecolor="#f57f17", lw=1.8))
ax.text(11.57, 4.30, "M / N", ha="center", va="center", fontsize=8, fontweight="bold")
ax.text(11.57, 4.72, "Torque & Speed\nTransducer", ha="center", va="bottom", fontsize=7.5, fontweight="bold", color="#e65100")

ax.add_patch(patches.Rectangle((12.00, 3.85), 0.85, 0.90, facecolor="#eceff1", edgecolor="#37474f", lw=1.8))
ax.text(12.42, 4.30, "3~ Motor\n400 V", ha="center", va="center", fontsize=8, fontweight="bold")

# Free Outlet Discharge Arrow
ax.annotate("", xy=(13.85, 4.30), xytext=(13.00, 4.30),
            arrowprops=dict(arrowstyle="->", lw=2.5, color="#2e7d32"))
ax.text(13.42, 4.65, "Free Outlet\n(Cat. A)", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#2e7d32")

# ==============================================================================
# 2. INSTRUMENTATION & NI cDAQ-9174 LAYER (BOTTOM BAND: y = 0.4 to 2.7)
# ==============================================================================
def draw_sensor_box(x, y, tag, desc):
    ax.add_patch(patches.FancyBboxPatch((x - 0.85, y - 0.35), 1.70, 0.70,
                                        boxstyle="round,pad=0.06", facecolor="#fffde7", edgecolor="#fbc02d", lw=1.6))
    ax.text(x, y + 0.12, tag, ha="center", va="center", fontsize=8.5, fontweight="bold", color="#111111")
    ax.text(x, y - 0.14, desc, ha="center", va="center", fontsize=7.2, color="#444444")

# Sensor Nodes
draw_sensor_box(2.00, 2.15, "Ambient Sensors", "pa, Ta, RH (Pt100)")
draw_sensor_box(5.35, 2.15, "Δp Transmitter", "0–1000 Pa (±0.1% FS)")
draw_sensor_box(8.80, 2.15, "pe3 & T3 Sensors", "±500 Pa + Pt100")
draw_sensor_box(11.65, 2.15, "HBM T22 + Encoder", "0–20 N·m / 360 ppr")

# Pneumatic impulse lines to pressure transmitters
ax.plot([5.10, 5.10, 5.20], [3.25, 2.55, 2.55], color="#0d47a1", ls=":", lw=1.3)
ax.plot([5.85, 5.85, 5.50], [3.25, 2.55, 2.55], color="#0d47a1", ls=":", lw=1.3)
ax.plot([9.90, 9.90, 9.35], [3.25, 2.55, 2.55], color="#c62828", ls=":", lw=1.3)
ax.plot([11.57, 11.57], [4.02, 2.55], color="#e65100", ls=":", lw=1.3)

# Central DAQ Chassis (NI cDAQ-9174)
ax.add_patch(patches.FancyBboxPatch((4.60, 0.45), 4.80, 0.80,
                                    boxstyle="round,pad=0.08", facecolor="#e8eaf6", edgecolor="#283593", lw=2.0))
ax.text(7.00, 0.96, "NI cDAQ-9174 Data Acquisition Chassis (100 Hz, 30 s/point)",
        ha="center", va="center", fontsize=9, fontweight="bold", color="#1a237e")
ax.text(7.00, 0.65, "NI-9205 (16-bit Analog V)   |   NI-9217 (24-bit 4-Wire RTD)   |   NI-9401 (TTL Counter)",
        ha="center", va="center", fontsize=7.8, color="#283593")

# Signal lines from sensors to DAQ
for sx in [2.00, 5.35, 8.80, 11.65]:
    ax.annotate("", xy=(7.00 + (sx - 7.00) * 0.45, 1.30), xytext=(sx, 1.78),
                arrowprops=dict(arrowstyle="->", lw=1.3, color="#3949ab"))

# Workstation PC
ax.add_patch(patches.FancyBboxPatch((10.60, 0.45), 2.50, 0.80,
                                    boxstyle="round,pad=0.08", facecolor="#e0f2f1", edgecolor="#00695c", lw=2.0))
ax.text(11.85, 0.96, "Lab Workstation (Python)", ha="center", va="center", fontsize=8.8, fontweight="bold", color="#004d40")
ax.text(11.85, 0.65, "ISO 5801 & GUM Post-Processing", ha="center", va="center", fontsize=7.5, color="#00695c")

ax.annotate("", xy=(10.55, 0.85), xytext=(9.45, 0.85),
            arrowprops=dict(arrowstyle="<->", lw=1.8, color="#00695c"))

plt.tight_layout()
plt.savefig("test_bench_pid.png", dpi=300, bbox_inches="tight")
plt.show()