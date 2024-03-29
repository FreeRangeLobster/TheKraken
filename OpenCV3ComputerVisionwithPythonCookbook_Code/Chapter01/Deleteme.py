{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import cv2, numpy as np\n",
    "\n",
    "cv2.namedWindow('window')\n",
    "\n",
    "fill_val = np.array([255, 255, 255], np.uint8)\n",
    "\n",
    "def trackbar_callback(idx, value):\n",
    "    fill_val[idx] = value\n",
    "    \n",
    "cv2.createTrackbar('R', 'window', 255, 255, lambda v: trackbar_callback(2, v))\n",
    "cv2.createTrackbar('G', 'window', 255, 255, lambda v: trackbar_callback(1, v))\n",
    "cv2.createTrackbar('B', 'window', 255, 255, lambda v: trackbar_callback(0, v))\n",
    "\n",
    "while True:\n",
    "    image = np.full((500, 500, 3), fill_val)\n",
    "    cv2.imshow('window', image)\n",
    "    key = cv2.waitKey(3)\n",
    "    if key == 27: \n",
    "        break\n",
    "\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
