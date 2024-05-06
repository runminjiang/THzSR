from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy.fftpack import fft2, ifft2, fftshift, ifftshift

# Load the image
image_path = 'sample.png'
img = Image.open(image_path)
img_gray = img.convert("L")  # Convert to grayscale

# Convert the image to an array
data = np.array(img_gray)

# Function to apply Gaussian low-pass and high-pass filters
def low_high_pass_filters(image, sigma_low, sigma_high):
    # Fourier transform of the image
    f_transform = fft2(image)
    f_transform = fftshift(f_transform)  # Shift the zero frequency component to the center of the spectrum
    
    # Create grids for the image
    x = np.linspace(-0.5, 0.5, image.shape[0])
    y = np.linspace(-0.5, 0.5, image.shape[1])
    X, Y = np.meshgrid(x, y)
    radius = np.sqrt(X**2 + Y**2)
    
    # Low pass filter: Gaussian
    low_pass = np.exp(-radius**2 / (2 * sigma_low**2))
    low_passed = ifftshift(f_transform * low_pass)
    low_passed = np.abs(ifft2(low_passed))
    
    # High pass filter: 1 - Gaussian
    high_pass = 1 - np.exp(-radius**2 / (2 * sigma_high**2))
    high_passed = ifftshift(f_transform * high_pass)
    high_passed = np.abs(ifft2(high_passed))
    
    return low_passed, high_passed

# Parameters for the Gaussian function
sigma_low = 0.02  # For low frequency
sigma_high = 0.02  # For high frequency

# Applying the filters
low_freq_img, high_freq_img = low_high_pass_filters(data, sigma_low, sigma_high)

# Plotting the images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(data, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(low_freq_img, cmap='gray')
axes[1].set_title('Low Frequency Image')
axes[1].axis('off')

axes[2].imshow(high_freq_img, cmap='gray')
axes[2].set_title('High Frequency Image')
axes[2].axis('off')

plt.tight_layout()
plt.show()