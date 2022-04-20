#!/usr/bin/env python3
import pygimli as pg

print("pygimli version:", pg.__version__)

pkgs = ["gempy", "gemgis", "pymc3"]

for pkg in pkgs:
    try:
        mod = pg.optImport(pkg)
        print(pkg, "version:", " " * (6-len(pkg)), mod.__version__)
    except:
        print("Problem with", pkg)
