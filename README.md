# RIP - Robust image processing 
This project provides a Python code permitting to calculate measures of robustness of image processing algorithms. 

It is supported by 2 research publications:
* A. Vacavant: A Novel Definition of Robustness for Image Processing Algorithm. In IEEE RRPR@ICPR 2016, LNCS 10214, pages 75–87, Cancún, Mexico, 2016.
* A. Vacavant et al.: New Definition of Quality-Scale Robustness for Image Processing Algorithms, with Generalized Uncertainty Modeling, Applied to Denoising and Segmentation. In IEEE RRPR@ICPR 2018, to appear. 

The program calculates the (alpha,sigma)-robustness introduced in the second publication. 

## How to use the code?
You may get inspiration from the .dat files provided in this repository. To evaluate robustness, you must give in the input file:
* as many comments as you want, starting by '#'
* 1 line with name of quality studied (SSIM, Dice, etc.)
* 1 line with name of noise/uncertainty studied, followed by values of scales of noise/uncertainty (e.g. std of Gaussian noise) separated by tabs
* for each algorithm evaluated: 1 line with name of algorithm, followed by values of quality for each scale of noise, separated by tabs

A first synthetic example is given in the file rip_test_first_example.dat:
```
# Quality measures for 5 virtual scales of noise
# First line always refers to the name of quality measured
# Second line stores the values of scales of noise (with name at the first pos)
# Then, algorithms' quality measures are enumerated following these scales (no limit on numbers) 
# Important: values are seperated by tabs (\t)
Quality
Uncertainty scale 	0.25	0.5	0.75	1
Algorithm 1	94	90	92.1	91.7
Algorithm 2	93	92.5	90	91
```

To run the code, give th input .dat file as parameter:
```
python measure_robustness.py <file_name.dat>
```

The program will then automatically:
* display and save a figure to inspect visually robustness (fig_rob.pdf)
* save a table presenting the (alpha,sigma) values for each algorithm, in decreasing order of alpha
* print these values in the console

