import pcbnew
from collections import defaultdict

board = pcbnew.GetBoard()
sizes = defaultdict(int)
flagged = 0

for track in board.GetTracks():
    if track.GetClass() == "PCB_VIA":
        drill = pcbnew.ToMM(track.GetDrillValue())
        diam = pcbnew.ToMM(track.GetWidth())
        sizes[(drill, diam)] += 1
        if drill < 0.3:
            flagged += 1

print("=== Via size audit ===")
print(f"{'Drill':>8}  {'Diameter':>8}  {'Ring':>8}  {'Count':>6}  {'Cost'}")
print("-" * 52)
for (drill, diam), count in sorted(sizes.items()):
    ring = (diam - drill) / 2
    # 2-layer rule: any drill < 0.3mm triggers surcharge
    cost = "SURCHARGE" if drill < 0.3 else "free"
    print(f"{drill:>7.2f}mm  {diam:>7.2f}mm  {ring:>7.3f}mm  {count:>5}   {cost}")

print("-" * 52)
print(f"Total vias: {sum(sizes.values())}")
print(f"Vias triggering surcharge: {flagged}")
if flagged == 0:
    print("All clear - no extra charges for drilling")
#exec(open('../script.py').read())