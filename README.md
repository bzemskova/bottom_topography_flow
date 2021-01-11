# Stratified Flow over Rough Bottom Topography
Code to generate the simulations reported in "Near-inertial dissipation due to stratified flow over abyssal topography" by Zemskova, V.E. and Grisouard, N.

## Pre-requisites
* Code requires Nek5000 software, which can be downloaded here: https://nek5000.mcs.anl.gov/
* Code requires to be run on a large number of cores (~100-300 cores), hence requiring supercomputing resources.
* Output can be post-processed either using the built-in Nek5000 functions or in Python (recommended)

## Contents
* sample_simulation: contains all files necessary to run a Nek5000 simulation
* Post-processing folder: contains all Python files for post-processing a Nek5000 output file, adapted from https://github.com/jcanton/pymech
