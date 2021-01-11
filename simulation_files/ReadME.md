# Stratified Flow over Rough Bottom Topography
Code to generate the simulations reported in "Near-inertial dissipation due to stratified flow over abyssal topography" by Zemskova, V.E. and Grisouard, N.

## Files within each folder:
* contain all Nek5000 files necessary to run a simulation for a given topographical width (\chi) and topographical height (J) parameters;
* labeled in terms of \chi and J, such that chi_016_J06 corresponds to a simulation described in the paper as \chi=0.16, J=0.6

## To run a simulation:
* Compile:
`$ $nekpath$/Nek5000/bin/makenek strat`
where $nekpath$ is the path to Nek5000 source code folder.
* Partition domain: `$ $nekpath$/Nek5000/bin/genmap`
* Run simulation: `$ $nekpath$/Nek5000/bin/nekbmpi strat ncores` where ncores is the number of cores to be used.

## Parameters that can be changed:
* Endtime of the simulation (either non-dimensional time or number of steps can be changed in strat.par file via stopAt, endTime, and numSteps parameters.
* To restart the simulation, uncomment the 'startFrom' line and change the name of the file.
* The topographical width and height parameters can be changed in strat.usr file in usrdat2() subroutine via chi and J parameters.
* Simulation domain size can be changed in strat.box file.
