'''
Designers: Robert Navarro and Robert Saucedo
Project: Data Project
Sources for code: Code was based off of pltw 3.1.1 and heavily custmized using the documentation provided
                  by matplotlib 
Data Sources: http://www.disastercenter.com/crime/uscrime.htm
              https://ucr.fbi.gov/crime-in-the-u.s/2012/crime-in-the-u.s.-2012/tables/1tabledatadecoverviewpdf/table_1_crime_
              in_the_united_states_
              by_volume_and_rate_per_100000_inhabitants_1993-2012.xls
'''
#imports libraries
#gets the path
import os.path
import matplotlib.pyplot as plt
#these make is so exponents don't show
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
from matplotlib.lines import Line2D
#imports the font manager
import matplotlib.font_manager
matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
#imports numpy and scipy for rsquared
from scipy import stats
import numpy as np
from scipy.stats import linregress

# Get the directory name for data files
directory = os.path.dirname(os.path.abspath(__file__))  
plt.style.use('fivethirtyeight')

#initialize the aggregators
years=[]
crimes=[]
x=[]
y=[]


# Open the file
filename = os.path.join(directory, 'crime_data.csv')
datafile = open(filename,'r')
    # Go through all the crimes per year
for line in datafile:
    year, amount = line.split(',')
#adds the year and amount of crimes committed to the lists
    years += [year]
    crimes += [amount]   
    x.append(int(year[0:]))
    y.append(int(amount[0:-1]))
#closes the file 
datafile.close()
  

#makes the graphs display in one window
fig, ax = plt.subplots(1,2)

  
#makes the time plot
#makes the ugly gray background of behind the plots into any color
fig.patch.set_facecolor('#ffc6a9')
fig.patch.set_alpha(0.7)
#makes it so exponents aren't used
ax[0].yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
plt.sca(ax[0])
#rotates the years
plt.xticks(rotation=45, fontsize=12)
#limits the years
ax[0].set_ylim(1000000,16000000)
ax[0].set_xlim(1960,2016)
#chooses x and y axeses and changes the line size, marker for data points, marker colors, and marker width 
#P.S. Those are thick astrics not flowers
ax[0].plot(years, crimes,'#cea6e6',linewidth=10.0, marker ='*', markersize=15, markerfacecolor = '#8b81d9', markeredgecolor= 'white', markeredgewidth= 5)
#changes the axis background
ax[0].set_axis_bgcolor('#19b5de')
#creates the labels
ax[0].set_ylabel('Number of Crimes')
ax[0].set_xlabel('Time(Years)', fontsize=15)
ax[0].set_title('Time Plot of the Number of Crimes in America From 1960 to 2015', fontstyle='italic', color='black', fontname="Tw Cen MT")

#makes the bar graph

#creates the labels
ax[1].set_xlabel('Time(Years)', fontsize=15)
ax[1].set_ylabel('Number of Crimes')
#changes the axis background
ax[1].set_axis_bgcolor('#19b5de')
plt.sca(ax[1])
#rotates the years
plt.xticks(rotation=45, fontsize=12)
#makes it so exponents aren't used
ax[1].yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
#chooses x and y axeses and changes the bar color
plt.bar(years, crimes, color = '#8b81d9')
ax[1].set_title('Bar Graph of the Number of Crimes in America From 1960 to 2015', fontstyle='italic', color='black', fontname="Tw Cen MT")
#opens the window as fullscreen because we all know it's annoying to have to open up the minimized screen over and over again
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

#figure 2
fig_2, ax = plt.subplots(1,2)
#sets the background color (changes the ugly gray one)
fig_2.patch.set_facecolor('#f9ffe2')
fig_2.patch.set_alpha(0.7)

#scatter plot
plt.sca(ax[0])
#makes it so exponents don't get used
ax[0].yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
#rotates the years
plt.xticks(rotation=45)
#limits the years
ax[0].set_ylim(1000000,16000000)
ax[0].set_xlim(1960,2016)
#chooses x and y axeses and changes the marker size/color
plt.scatter(years, crimes, color = '#cea6e6', s= 150)
plt.xticks(fontsize=12)
#changes the axis background
ax[0].set_axis_bgcolor('#19b5de')
#creates the labels
ax[0].set_ylabel('Number of Crimes')
ax[0].set_xlabel('Time(Years)', fontsize=15)
ax[0].set_title('Time Plot of the Number of Crimes in America From 1960 to 2015', fontstyle='italic', color='black', fontname="Tw Cen MT")
#creates line of best fit
m,b = np.polyfit(x,y,1)
plt.scatter( x, np.array(x) * m +b, color = '#e1f7d5') 
#annotates
ax[0].annotate('RSquared=0.32019463594237152', xy=(1970, 2000000), xytext=(1970, 2000000))
            
            
#boxplot
#changes the axis background
ax[1].set_axis_bgcolor('#f69f95')
plt.sca(ax[1])
#makes it so exponents aren't used
ax[1].yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
#chooses x and y axeses and changes the box color
box= plt.boxplot(y, patch_artist=True, notch=True)
color = ['#dcffe5']
for patch, color in zip(box['boxes'], color):
    patch.set_facecolor(color)
#changes the color of the lines
ax[1].grid(True, 'major', color='#c47f77', linestyle='-', linewidth=2.5)
#adds a title
ax[1].set_title('Boxplot of Crimes Commited', fontstyle='italic', color='black', fontname="Tw Cen MT")
#Adds the labels 
ax[1].set_ylabel('Number of Crimes')
ax[1].set_xlabel('Time(Years)', fontsize=15)
ax[1].set_xticklabels(['1960-2015'])
#opens the window as fullscreen because we all know it's annoying to have to open up the minimized screen over and over again
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
#displays our beautiful creation
fig_2.show()
fig.show()

#creates and prints the rsquared value
np.array(x).astype(np.float)
np.array(y).astype(np.float)
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("r-squared:", r_value**2)
