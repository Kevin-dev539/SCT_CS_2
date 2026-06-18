# 🔐 Image Encryption Tool Using Pixel Manipulation

## 📌 Project Overview
This project is a simple **Image Encryption and Decryption Tool** developed using Python. The tool encrypts images by manipulating pixel values and rearranging pixel positions, making the original image unreadable without the correct key.
The primary goal of this project is to demonstrate the fundamental concepts of **cryptography**, **image processing**, and **data protection** in a practical way.

This project is intended for educational purposes and helps beginners understand how encryption works at a basic level before moving on to advanced cryptographic algorithms such as AES and RSA.

---

# 🎯 Objectives
* Learn how digital images are represented as pixel data.
* Understand the basic principles of encryption and decryption.
* Explore pixel manipulation techniques.
* Gain hands-on experience with Python image processing libraries.
* Demonstrate the concept of symmetric-key encryption.

---

# 📖 What is Image Encryption?
Image encryption is the process of converting an image into an unreadable format so that unauthorized users cannot access its contents.
The encrypted image appears as random noise or distorted data. Only users possessing the correct decryption key can restore the original image.
### Original Image

```text
Readable Image
```

### Encrypted Image
```text
Random Noise
```

### Decrypted Image

```text
Readable Image Restored
```

Image encryption is commonly used in:

* Secure image transmission
* Military communication systems
* Medical image protection
* Cloud storage security
* Digital forensics
* Confidential document sharing

---

# ⚙️ How the Project Works

The encryption process consists of two major steps:

## Step 1: Pixel Value Manipulation

Each pixel value is modified using a secret key.

### Formula

```text
Encrypted Pixel = (Original Pixel + Key) mod 256
```

### Example

Assume:

```text
Original Pixel = 100
Key = 5
```

Calculation:

```text
(100 + 5) mod 256 = 105
```

Result:

```text
Encrypted Pixel = 105
```

This changes the color information of every pixel in the image.

---

## Step 2: Pixel Position Shuffling

After changing pixel values, the pixels are randomly rearranged.

Example:

Before:

```text
A B C D
```

After:

```text
C A D B
```

This destroys the visual structure of the image and makes it appear as random noise.

The shuffle pattern is generated using:

```python
np.random.seed(key)
```

The same key always produces the same shuffle pattern.

---

# 🔓 Decryption Process

The decryption process reverses the encryption steps.

## Step 1: Reverse Pixel Shuffling

The original pixel positions are restored.

```text
C A D B
```

becomes

```text
A B C D
```

---

## Step 2: Reverse Pixel Manipulation

### Formula

```text
Original Pixel = (Encrypted Pixel - Key) mod 256
```

Example:

```text
Encrypted Pixel = 105
Key = 5

(105 - 5) mod 256 = 100
```

Result:

```text
Original Pixel = 100
```

The original image is successfully recovered.

---

# 🔑 Why the Key is Important

The key controls:

1. Pixel value transformation
2. Pixel shuffling pattern

Without the correct key:

* Pixel positions cannot be restored.
* Pixel values cannot be recovered.

As a result, the image remains unreadable.

---

# 🧠 Concepts Used

## 1. Cryptography
Cryptography is the science of protecting information by transforming it into a secure format.
The project demonstrates:

### Encryption
Converting readable data into unreadable data.

### Decryption
Converting encrypted data back into readable data.

---
## 2. Symmetric Key Encryption
This project uses a symmetric encryption model.

### Definition
The same key is used for:
* Encryption
* Decryption

Example:
```text
Encryption Key = 5
Decryption Key = 5
```
If different keys are used, the image cannot be recovered.
---

## 3. Pixel Manipulation
A digital image consists of pixels.
Each pixel stores color information.

For RGB images:
```text
Red   : 0–255
Green : 0–255
Blue  : 0–255
```

Example:
```text
(255,0,0)
```
represents a red pixel.
The project modifies these pixel values during encryption.
---

## 4. Modular Arithmetic
The project uses:
```python
% 256
```
### Why?
Pixel values must remain between:
```text
0 and 255
```

Example:
```text
250 + 20 = 270
270 mod 256 = 14
```
This keeps values within the valid pixel range.

---

## 5. Randomization
Randomization is used to shuffle pixel positions.

```python
np.random.shuffle()
```
The random pattern depends on the encryption key.
This adds an additional layer of security.

---

## 6. NumPy Arrays
Images are converted into NumPy arrays for efficient processing.

Example:
```python
img_array = np.array(img)
```

Advantages:
* Faster computation
* Easy pixel manipulation
* Efficient memory usage

---

## 7. Image Processing
The project uses the Pillow library.

### Features Used
* Loading images
* Converting images to arrays
* Saving encrypted images
* Saving decrypted images

---

# 📚 Python Libraries Used

## Pillow (PIL)
Used for image processing.

Installation:
```bash
pip install pillow
```

Functions used:
```python
Image.open()
Image.fromarray()
```

---

## NumPy
Used for numerical operations and pixel manipulation.

Installation:
```bash
pip install numpy
```

Functions used:
```python
np.array()
np.random.shuffle()
np.arange()
np.mod()
```

---

# 🛠️ Project Structure

```text
Image Encryption Tool
│
├── Image.py
├── Original Image
├── Encrypted Image
├── Decrypted Image
└── README.md
```

---
# 🚀 How to Run the Project
## Install Dependencies
```bash
pip install pillow numpy
```
---

## Run the Program
```bash
python Image.py
```

---

## Encrypt an Image
```text
1. Encrypt Image
Enter image path
Enter output file name
Enter encryption key
```
---

## Decrypt an Image
```text
2. Decrypt Image
Enter encrypted image path
Enter output file name
Enter decryption key
```
---

# 🔒 Security Analysis
### Advantages
✔ Demonstrates encryption concepts
✔ Uses both confusion and diffusion
✔ Simple and easy to understand
✔ Good educational cybersecurity project
--

### Limitations
❌ Small key space
❌ Not resistant to brute-force attacks
❌ Not suitable for real-world security
❌ Uses predictable pseudo-random generation
❌ Does not provide cryptographic-level protection
---
# 🔮 Future Improvements
Possible enhancements include:
* Password-based encryption
* AES image encryption
* GUI using Tkinter
* Drag-and-drop image support
* Random key generation
* Key file storage
* Support for multiple encryption rounds
* Histogram analysis
* Image integrity verification
* Secure cryptographic random number generation
---

# 🎓 Learning Outcomes
Through this project, I gained practical experience in:

* Python Programming
* Image Processing
* NumPy Arrays
* Pillow Library
* Cryptography Fundamentals
* Symmetric Encryption
* Pixel Manipulation Techniques
* Randomization Methods
* Encryption and Decryption Workflows
* Cybersecurity Concepts
---

*"Understanding how encryption works at a fundamental level is the first step toward building secure systems."* 🔐
