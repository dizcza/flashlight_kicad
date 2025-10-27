# sed -i '1 s/^.*$/Designator,Val,Package,MidX,MidY,Rotation,Layer/' *-pos.csv

from pathlib import Path

import pandas as pd

PATH = Path(__file__).with_name("flashlight-all-pos.csv")
lines = PATH.read_text().splitlines()
lines[0] = "Designator,Val,Package,MidX,MidY,Rotation,Layer"
PATH.write_text('\n'.join(lines))

df = pd.read_csv(PATH, index_col=0)
df.loc[["D1"], "Rotation"] += 180
df.loc[["U2"], "Rotation"] += 90
df.loc[:, "Rotation"] %= 360
df.to_csv(PATH)
