from __future__ import print_function
import os

import pyct as ct
import numpy as np
import nibabel as nb
import matplotlib.pyplot as plt

root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':
    print('Loading image...')
    filename = os.path.join(root, 'data', 'brainmask.mgz')
    img = nb.load(filename).get_data().astype(np.float)
    img = img[50:150, 50:150, 50:150]
    print('Image shape: ', img.shape)
    print('Number of elements: ', np.prod(img.shape))

    # Setup curvelet params
    print('Applying Curvelet Transform...')
    A = ct.fdct3(img.shape, nbs=2, nba=360, ac=True, norm=False, vec=True, cpx=False)

    # Apply curvelet to the image
    f = A.fwd(img)

    print('Coefficients array:\n\t', f)
    print('Shape: ', f.shape)

    # Reconstruct the image
    print('Applying Curvelet Transform...')
    y = A.inv(f)

    print('Plotting results')
    fig, ax = plt.subplots(1, 2, sharey='all')
    ax[0].imshow(img[:, :, 50], cmap='gray')
    ax[0].set_title('Original')

    ax[1].imshow(y[:, :, 50], cmap='gray')
    ax[1].set_title('Reconstructed')
    plt.show()
