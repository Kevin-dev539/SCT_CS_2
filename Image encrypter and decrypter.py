from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, output_path, key):
    # Open image1
    
    img = Image.open(image_path)
    img_array = np.array(img)

    # Flatten image array
    flat_pixels = img_array.flatten().astype(np.int32)

    # Pixel value manipulation
    encrypted_pixels = np.mod(flat_pixels + key, 256)

    # Pixel swapping
    np.random.seed(key)
    indices = np.arange(len(encrypted_pixels))
    np.random.shuffle(indices)

    encrypted_pixels = encrypted_pixels[indices]

    # Reshape back to image
    encrypted_img = encrypted_pixels.reshape(img_array.shape)

    Image.fromarray(encrypted_img.astype(np.uint8)).save(output_path)
    print(f"Encrypted image saved as {output_path}")


def decrypt_image(image_path, output_path, key):
    # Open encrypted image
    img = Image.open(image_path)
    img_array = np.array(img)

    flat_pixels = img_array.flatten().astype(np.int32)

    # Recreate shuffled indices
    np.random.seed(key)
    indices = np.arange(len(flat_pixels))
    np.random.shuffle(indices)

    # Reverse swapping
    original_order = np.empty_like(indices)
    original_order[indices] = np.arange(len(indices))

    decrypted_pixels = flat_pixels[original_order]

    # Reverse pixel value manipulation
    decrypted_pixels = decrypted_pixels.astype(np.int32)
    decrypted_pixels = np.mod(decrypted_pixels - key, 256)

    # Reshape back to image
    decrypted_img = decrypted_pixels.reshape(img_array.shape)

    Image.fromarray(decrypted_img.astype(np.uint8)).save(output_path)
    print(f"Decrypted image saved as {output_path}")


# Menu
while True:
    print("\n=== Image Encryption Tool ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        image_path = input("Enter image path: ")
        output_path = input("Enter output encrypted image name: ")
        key = int(input("Enter encryption key: "))
        encrypt_image(image_path, output_path, key)

    elif choice == "2":
        image_path = input("Enter encrypted image path: ")
        output_path = input("Enter output decrypted image name: ")
        key = int(input("Enter decryption key: "))
        decrypt_image(image_path, output_path, key)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")