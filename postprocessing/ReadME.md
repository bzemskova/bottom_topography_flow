# Stratified Flow over Rough Bottom Topography
Python post-processing codes for simulations reported in "Near-inertial dissipation due to stratified flow over abyssal topography" by Zemskova, V.E. and Grisouard, N.

## Post-processing example
* Found in postprocess_example.py
* Shows how to extract grid, velocity, and buoyancy fields from a Nek5000 output file (.f*)
* Shows how to compute height-above-bottom (HAB) coordinates for a given topographic height and width
* Shows how to compute kinetic energy dissipation in volume
* Shows how to average a field in HAB coordinates for Nek5000 curved grid
