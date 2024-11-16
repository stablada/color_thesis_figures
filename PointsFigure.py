import matplotlib.pyplot as plt
from matplotlib import ticker

import GenreProcessing as gp

# SEARCH HERE #
query = "edm"
data = gp.seek(query)
# SEARCH HERE #

# import backdrop image
img = plt.imread("colorback.jpg")

fig, ax = plt.subplots()

# Add data to plot with o marker and a black and white marker coloring for better visibility
ax.scatter(data.h_val, data.l_val, marker='o', edgecolors="black", color="white", alpha=0.7)

# Set axis limits to x:360 and y:100 for hue values and lightness values
ax.set_xlim([0,360])
ax.set_ylim([0,100])

# Make ticks more visible and use requested TNR fontfamily
ax.tick_params(axis='both', which='major', labelsize=12, labelfontfamily="Times New Roman", labelcolor='black')

# X-axis tick increment set to 30
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=30))

# add x and y axis labels
ax.set_ylabel("Lightness", fontsize=15, labelpad=20, font="Times New Roman")
ax.set_xlabel("Hue", fontsize=15, labelpad=20, font="Times New Roman")

# add image to background for color representation
ax.imshow(img, extent=[0,360,0,100])

# header text in TNR font slightly lowered for better visibility
fig.suptitle("%s" % data.name.capitalize(), fontsize=20, font="Times New Roman", y=0.87)

# make figure longer to support the color-spectrum width without honestly just looking odd
fig.set_size_inches(10, 5, forward=True)

#show
plt.show()

plt.savefig("figures/plot_%s.png" % query)