from PIL import Image
# PIL is simpler for basic tasks like creating and manipulating images.

# The colors list contains four tuples representing colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Red, Green, Blue, Yellow

# creates a new image of size 50x50 pixels using the color from the colors list.
images = [Image.new("RGB", (50, 50), color) for color in colors]

# Step 2: Attach the images together to form a 100x100 image
combined_image = Image.new("RGB", (100, 100))

# the 4 images in a 2x2 grid
combined_image.paste(images[0], (0, 0))   # Top-left
combined_image.paste(images[1], (50, 0))  # Top-right
combined_image.paste(images[2], (0, 50))  # Bottom-left
combined_image.paste(images[3], (50, 50))   # Bottom-right

# Resize the combined image to 200x200
resized_image = combined_image.resize((200, 200))

# Save the resulting image
resized_image_path = "combined_resized_image.png"
resized_image.save(resized_image_path)

resized_image.show(), resized_image_path
