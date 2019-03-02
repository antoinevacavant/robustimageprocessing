'''
File measureRobustness.py
Created on Feb. 20 2019
@author: Antoine Vacavant, Universite Clermont Auvergne / Institut Pascal, antoine.vacavant_AT_uca.fr, http://antoine-vacavant.eu
'''

'''
Copyright (c) 2019 Antoine Vacavant

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

#!/usr/bin/python

# imports
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as ftm
from pylab import * 
import itertools
import sys

if __name__ == "__main__":
	'''
	not enough parameters
	'''
	if len(sys.argv) == 1:
		print "Please use this code as python measure_robustness.py <file-name.dat>"
	'''
	import data and init variables
	filename is given as the first argument of main function
	'''
	if len(sys.argv) > 1:
		# read data file with genfromtxt
		# mat_in= genfromtxt(sys.argv[1], delimiter="\t", comments='#', dtype="|U20")
		file= open(sys.argv[1], "r")
		file_lines = [line.rstrip('\n') for line in file]

		# skip comments
		i= 0
		while file_lines[i][0] == "#":
			i= i+1
		# read quality name and scales of noise
		quality_name= file_lines[i]
		i= i+1
		data= file_lines[i].split('\t')
		noise_name= data[0]
		
		# store values of noise scales and qualities of algorithms
		mat_in= []
		while i < len(file_lines):			
			if file_lines[i] != '':
				mat_in.append(file_lines[i].split('\t'))
			i= i+1
		# scales of noise are stored in the 1st line (after possible comments)
		scales= mat_in[0][1:]
		number_scales= len(scales)
		# number of methods
		number_methods= len(mat_in)-1
		# values to generate line colors
		color_map= linspace(0.0, 0.9, number_methods) 
		# generate colors
		colors = [ cm.hsv(x) for x in color_map ]
		# possible markers
		markers = itertools.cycle(('o', 's', '8', 'v', '<', 'd', 'h', '>')) 

		'''
		create fig and save it into a pdf file
		'''

		# init fig
		fig = plt.figure(figsize=plt.figaspect(0.75))
		# latex style
		plt.rc('font', family='serif')
		plt.rc('text', usetex=True)
		# 1 plot
		ax = fig.add_subplot(1, 1, 1)

		# plot the lines
		for m in range(0,number_methods):
			ax.plot(scales, 
					mat_in[1+m][1:number_scales+1], 
					marker=markers.next(), 
					ms=10, 
					lw=2.5, 
					mew=1.5, 
					alpha=0.7, 
					color=colors[m], 
					label=str(mat_in[1+m][0]) )

		# some margins
		plt.margins(0.1)
		# increase fonts in ticks
		for tick in ax.xaxis.get_major_ticks():
		    tick.label.set_fontsize(16) 
		for tick in ax.yaxis.get_major_ticks():
		    tick.label.set_fontsize(16) 
		# labels of axes
		ax.set_xlabel(noise_name, fontsize="20")
		ax.set_ylabel(quality_name, fontsize="20")
		# legend
		ax.legend(loc=3, prop=ftm.FontProperties(size=18), fancybox=True, framealpha=0.5)
		plt.grid(True)

		# save and show
		plt.savefig("fig_rob.pdf")
		plt.show()
		fig.tight_layout()

		'''
		calculate robustness values and create a table in latex
		'''

		# store values of (alpha,sigma) for each method
		rob_alpha= [-float("inf")]*number_methods
		rob_sigma= [0]*number_methods
		# calculate alpha and the scale sigma where this value has been reached
		for m in range(0,number_methods):
			for k in range(1,number_scales):
				dy= float(mat_in[1+m][1+k-1])-float(mat_in[1+m][1+k])		
				dx= abs(float(scales[k])-float(scales[k-1]))
				rob_alpha_prev= rob_alpha[m]
				# compute alpha
				rob_alpha[m]= max(rob_alpha[m], dy/dx)
				# store sigma when it has been reached
				if rob_alpha_prev != rob_alpha[m]:
					rob_sigma[m]= float(scales[k-1])

		# sort in descending order, and get indices only with argsort
		ind_sorted_rob= np.argsort(rob_alpha)[::-1]

		# open and write the latex file as standalone document
		file= open("tab_rob.tex", "w+")
		file.write("\\documentclass{standalone}\n")
		file.write("\\begin{document}\n")
		file.write("\\begin{tabular}{c|c}\n")
		file.write("\\hline\n")
		file.write("\\bf Name & \\bf $(\\alpha,\\sigma)$ \\\\ \n")
		file.write("\\hline\n")
		file.write("\\hline\n")
		# write the name and values (alpha,sigma) for all methods in desceding order of alpha
		# printed in console
		print "(alpha, sigma) value for each method"
		for m in range(0,number_methods):
			file.write(str(mat_in[1+ind_sorted_rob[m]][0])+ # name
						" & ("+str(round(rob_alpha[ind_sorted_rob[m]],3))+","+str(rob_sigma[ind_sorted_rob[m]])+ # alpha,sigma
						") \\\\ \n")
			print (str(mat_in[1+ind_sorted_rob[m]][0])+ # name
					"\t("+str(round(rob_alpha[ind_sorted_rob[m]],3))+","+str(rob_sigma[ind_sorted_rob[m]])+")" #alpha, sigma
					)
		file.write("\\end{tabular}\n")

		# end the document and save
		file.write("\\end{document}")
		file.close()




