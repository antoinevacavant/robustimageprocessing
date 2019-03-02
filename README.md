# RIP - Robust image processing 
This project provides a Python code permitting to calculate measures of robustness of image processing algorithms. 

It is supported by 2 research publications:
* A. Vacavant: A Novel Definition of Robustness for Image Processing Algorithm. In IEEE RRPR@ICPR 2016, LNCS 10214, pages 75–87, Cancún, Mexico, 2016.
* A. Vacavant et al.: New Definition of Image Processing Robustness Combining Quality Variation and Noise Scale, with Generalized Uncertainty Modeling, Applied to Denoising and Segmentation. In IEEE RRPR@ICPR 2018, to appear. 
The program calculates the (alpha,sigma)-robustness from the second publication. 

## Input and outputs
You may get inspiration from the .dat files provided in this repository. To evaluate robustness, you must give in the input file:
* as many comments as you want, starting by '#'
* 1 line with name of quality studied (SSIM, Dice, etc.)
* 1 line with name of noise/uncertainty studied, followed by values of scales of noise/uncertainty (e.g. std of Gaussian noise) separated by tabs
* for each algorithm evaluated: 1 line with name of algorithm, followed by values of quality for each scale of noise, separated by tabs

To run the code:
```
python measure_robustness.py <file_name.dat>
```

The program will then:
* display and save a figure to inspect visually robustness (fig_rob.pdf)
* save a table presenting the (alpha,sigma) values for each algorithm, in decreasing order of alpha
* print these values in the console

