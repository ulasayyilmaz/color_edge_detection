# color_edge_detection
Colored Edge Detection
We were curious about the edge detection capabilities of humans in colored images. We first developed an experimental pipeline where we presented individuals with simple images containing two distinct contrasts of the same color for 200 ms, preceded and followed by a white screen. We repeated this experiment for 20 different examples, with each trial image having an RGB difference between the two colors in a trial ranging from 0 to 50.

Side note: CIELAB color space is a virtual color space with three axes different from the RGB axes: Red/Green, Yellow/Blue, and White/Black. CIELAB color space was created, inspired by human perception of color.

We then used the CIELAB color space and built a color edge detection algorithm. The edge detection algorithm had a parameter, “threshold,” that determines the existence of an edge if the color contrast value is above the threshold. There were different threshold values for each of the three axes of the CIELAB space, and humans had different “thresholds” for perceiving blue, red, yellow, and white. We compared the threshold values for computers and humans and drew conclusions about humans’ partiality to certain colors and whether CIELAB mirrors humans’ color perception mechanisms.
