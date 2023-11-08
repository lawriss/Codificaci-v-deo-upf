# -*- coding: utf-8 -*-
"""P1_240445.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iOTdotd-7I4STkcHVGwI9SHf0BdcUuXK

# Video: P1 - JPEG & MPEG

Laura Ruiz Soler

NIA: 240445

laura.ruiz17@estudiant.upf.edu
"""

import numpy as np
import subprocess
# TASK 1
# Create a translator from 3 values in RGB into the 3 YUV values, plus the opposite operation.
# You can choose the 3 values, or open them from a text file, receive it from command line… feel free.
# Put it in a method.

def rgb_to_yuv(r,g,b):
  y = 0.299*r + 0.587*g + 0.114*b
  u = 0.492*(b-y)
  v = 0.877*(r-y)
  return (y,u,v)

def yuv_to_rgb(y,u,v):
  r = y + 1.140*v
  g = y - 0.395*u - 0.581*v
  b = y + 2.032*u
  return (r,g,b)


# TESTING TASK 1
c = [0.2,0.4,0.6]
(y,u,v) = rgb_to_yuv(c[0], c[1], c[2])
if __name__ == "__main__":
  print("(Y,U,V) = ",y,u,v)
(r,g,b) = yuv_to_rgb(y,u,v)
if __name__ == "__main__":
  print("(R,G,B) = ",r,g,b)

# TASK 2
# Use ffmpeg to resize images into lower quality. Use any image you like
# Now, create a method in previous script to automatise this order.

# We install ffmpeg
#!apt-get install ffmpeg
'''
def resize_and_reduce_quality(input_image, output_image, width, height, quality):
  ffmpeg_command = f'ffmpeg -i {input_image} -vf "scale={new_width}:{new_height}" -q:v {quality} {output_image}'
  subprocess.run(ffmpeg_command, shell=True, check=True)


# TESTING TASK 2
input_image = '/content/sea.JPG' # original size: 5472 × 3072
output_image = '/content/task2_im.jpg' #will have
new_width = 547
new_height = 307
quality = 5
resize_and_reduce_quality(input_image, output_image, new_width, new_height, quality)
'''

# TASK 3
# Create a method called serpentine which should be able to read the bytes of a JPEG file in the serpentine way we saw.
def serpentine(w,h,m):
  output = []
  i=0
  j=0
  output.append(m[j,i])

  while (i!=w-1 and j!=h-1):
    if (j==0):
      if (i+1<w):
        i+=1
      output.append(m[j,i])
      while (i!=0):
        i-=1
        j+=1
        output.append(m[j,i])
    if (i==0):
      if (j+1<h):
        j+=1
      output.append(m[j,i])
      while (j!=0):
        i+=1
        j-=1
        output.append(m[j,i])

  while(i!=w-1 or j!=h-1):
    j+=1
    output.append(m[j,i])
    while(j<h-1):
        i-=1
        j+=1
        output.append(m[j,i])
    i+=1
    output.append(m[j,i])
    if (i==w-1 and j==h-1):
      break;
    while(i<w-1):
      j-=1
      i+=1
      output.append(m[j,i])

  return output


# TESTING TASK 3
# *It only works for square matrices!!

w,h = 3,3 # We set the size of the matrix
m = np.zeros((w,h)) # Create the matrix
a=0
for i in range(0,h): # Generate a matrix with ascendent sorted numbers in order to see at the end more easily the serpentine effect
  for j in range(0,w):
    m[i,j]=a
    a+=1
if __name__ == "__main__":
  print("Original matrix: \n", m)
o = serpentine(w,h,m)
if __name__ == "__main__":
  print("\nSerpentine reading: \n", o)

# TASK 4
# Use FFMPEG to transform the previous image into b/w. Do the hardest compression you can.
# Add everything into a new method and comment the results
'''
def compress_b_w(input_image, output_image, width, height, quality):
  ffmpeg_command = f'ffmpeg -i {input_image} -vf "format=gray" -q:v 1 {output_image}'
  subprocess.run(ffmpeg_command, shell=True, check=True)

# TESTING TASK 4
input_image = '/content/task2_im.jpg'
output_image = '/content/task4_im.jpg'

compress_b_w(input_image, output_image, new_width, new_height, quality)

"""With the "format=gray" parameter, we transform our image into black and white. Then, with the "video-quality" parameter (q:v) we set the lowest value, which is 1. For the image created on task 2, we set this value to 5, and now we reduced to 1. We can see as a consequence, that the quality of our new image is reduced, having more artifacts, because the information it contains is more compressed, so we cannot see smaller details."""
'''

# TASK 5
# Create a method which applies a run-lenght encoding from a series of bytes given.

def run_len_encoding(input):
  output = []
  matches = 0
  current_byte = input[0]

  for i in input:
    if (i==current_byte):
      matches+=1
    else:
      output.append(current_byte)
      output.append(matches)
      current_byte = i
      matches = 1

  output.append(current_byte)
  output.append(matches)
  return output

# TESTING TASK 5
input_bytes = 'LLAAAURRAA'
encoded_bytes = run_len_encoding(input_bytes)
if __name__ == "__main__":
  print(encoded_bytes)

# TASK 6
# Create a class which can convert, can decode (or both) an input using the DCT. Not necessary a
# JPG encoder or decoder. A class only about DCT is OK too

class dct_conversion:

    # general formula (obatined from class' slides, but for general square matrices, of size NxN)
    def dct(input):
      N = np.size(input, axis=0)
      output = np.zeros((N, N))

      for u in range(N):
        for v in range(N):
          sum=0
          if u==0:
            alpha1 = np.sqrt(1/N)
          else:
            alpha1 = np.sqrt(2/N)

          if v==0:
            alpha2 = np.sqrt(1/N)
          else:
            alpha2 = np.sqrt(2/N)

          for x in range(N-1):
            for y in range(N-1):
              sum += input[x,y]*np.cos((np.pi/N)*(x+0.5)*u)*np.cos((np.pi/N)*(y+0.5)*v)

          total = alpha1*alpha2*sum
          output[u,v]=total
      return output

    def encode(self, input_data):
        # Apply DCT encoding to the input data
        return self.dct2(input_data)

    def decode(self, encoded_data):
        # Apply inverse DCT decoding to the encoded data
        return self.idct2(encoded_data)


# TESTING TASK 6
input_data = np.array([
        [255, 128, 128, 255],
        [255, 255, 255, 255],
        [255, 128, 128, 255],
        [255, 128, 128, 255]
    ], dtype=np.float32)

converted_data = dct_conversion.dct(input_data)
if __name__ == "__main__":
  print(converted_data)