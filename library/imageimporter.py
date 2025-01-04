# # from PIL import Image, ImageDraw, ImageFont
# # import os

# # def add_text_to_image(image_path, output_path, text_lines, font_path, font_size=30):
# #     # Open the image
# #     img = Image.open(image_path)
# #     draw = ImageDraw.Draw(img)

# #     # Load font
# #     font = ImageFont.truetype(font_path, font_size)

# #     # Starting position
# #     text_position = (20, img.height - (len(text_lines) + 1) * (font_size + 10))

# #     # Draw each line of text
# #     for line in text_lines:
# #         draw.text(text_position, line, fill="white", font=font, stroke_width=2, stroke_fill="black")
# #         text_position = (text_position[0], text_position[1] + font_size + 10)

# #     # Save the output image
# #     img.save(output_path)

# # # Input image and text
# # input_image = "/Users/vishnuagrawal/Desktop/Project/image1.jpg"
# # output_image = "/Users/vishnuagrawal/Desktop/Project/output_image_with_text.jpg"
# # font_path = "/Users/vishnuagrawal/Desktop/Project/Noto_Sans_Devanagari/NotoSansDevanagari-VariableFont_wdth,wght.ttf"  # Replace with a path to a TTF font file on your system
# # text = [
# #     "नाम-रहित सड़क, सलीहे, छत्तीसगढ़ 493112, भारत",
# #     "Latitude   21.213906666666667°",
# #     "Longitude  82.752705°",
# #     "Local      12:16:20 pm",
# #     "GMT        06:46:20 am",
# #     "Altitude   294 मीटर",
# #     "गुरुवार, 07.11.2024"
# # ]

# # # Add text to image
# # add_text_to_image(input_image, output_image, text, font_path)


# # print(f"Image saved with text at: {output_image}")

# from PIL import Image, ImageDraw, ImageFont

# def add_text_with_black_background(image_path, output_path, text_lines, font_path, font_size=30):
#     # Open the image
#     img = Image.open(image_path)
#     draw = ImageDraw.Draw(img)

#     # Load font
#     font = ImageFont.truetype(font_path, font_size)

#     # Calculate the height needed for the text background
#     text_height = (font_size + 10) * len(text_lines) + 10
#     background_y = img.height - text_height

#     # Draw a black rectangle at the bottom
#     draw.rectangle([(0, background_y), (img.width, img.height)], fill="black")

#     # Starting position for text
#     text_position = (20, background_y + 10)

#     # Draw each line of text in white
#     for line in text_lines:
#         draw.text(text_position, line, fill="white", font=font)
#         text_position = (text_position[0], text_position[1] + font_size + 10)

#     # Save the output image
#     img.save(output_path)
#     print(f"Image saved with text and black background at: {output_path}")

# # Input image and text
# input_image = "/Users/vishnuagrawal/Desktop/Project/image1.jpg"
# output_image = "/Users/vishnuagrawal/Desktop/Project/output_image_with_text.jpg"
# font_path = "/Users/vishnuagrawal/Desktop/Project/Noto_Sans_Devanagari/NotoSansDevanagari-VariableFont_wdth,wght.ttf" 
# text = [
#     "नाम-रहित सड़क, सलीहे, छत्तीसगढ़ 493112, भारत",
#     "Latitude   21.213906666666667°",
#     "Longitude  82.752705°",
#     "Local      12:16:20 pm",
#     "GMT        06:46:20 am",
#     "Altitude   294 मीटर",
#     "गुरुवार, 07.11.2024"
# ]

# # Add text with a black background
# add_text_with_black_background(input_image, output_image, text, font_path)




from PIL import Image, ImageDraw, ImageFont

def add_text_with_translucent_background(image_path, output_path, text_lines, font_path, font_size=30, transparency=200):
    """
    Add text with a translucent black background at the bottom of an image.
    
    Args:
    - image_path: Path to the input image.
    - output_path: Path to save the output image.
    - text_lines: List of text lines to overlay on the image.
    - font_path: Path to the .ttf font file.
    - font_size: Font size for the text.
    - transparency: Transparency level for the black background (0-255, where 255 is opaque).
    """
    # Open the image
    img = Image.open(image_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))  # Create a transparent overlay
    draw = ImageDraw.Draw(overlay)

    # Load font
    font = ImageFont.truetype(font_path, font_size)

    # Calculate the height needed for the text background
    text_height = (font_size + 10) * len(text_lines) + 10
    background_y = img.height - text_height

    # Draw a translucent black rectangle at the bottom
    draw.rectangle(
        [(0, background_y), (img.width, img.height)], 
        fill=(0, 0, 0, transparency)  # Translucent black
    )

    # Starting position for text
    text_position = (20, background_y + 10)

    # Draw each line of text in white
    for line in text_lines:
        draw.text(text_position, line, fill="white", font=font)
        text_position = (text_position[0], text_position[1] + font_size + 10)

    # Merge the overlay with the original image
    combined = Image.alpha_composite(img, overlay)

    # Convert back to RGB and save the output image
    combined.convert("RGB").save(output_path)
    print(f"Image saved with translucent text background at: {output_path}")

# Input image and text
# input_image = "/Users/vishnuagrawal/Desktop/Project/data/inputImages/image1.jpg"
# output_image = "/Users/vishnuagrawal/Desktop/Project/data/outputImages/output_image_with_text.jpg"
# font_path = "/Users/vishnuagrawal/Desktop/Project/font/Noto_Sans_Devanagari/NotoSansDevanagari-VariableFont_wdth,wght.ttf" 
# text = [
#     "नाम-रहित सड़क, सलीहे, छत्तीसगढ़ 493112, भारत",
#     "Latitude   21.213906666666667°",
#     "Longitude  82.752705°",
#     "Local      12:16:20 pm",
#     "GMT        06:46:20 am",
#     "Altitude   294 मीटर",
#     "गुरुवार, 07.11.2024"
# ]

# Add text with a translucent black background
# add_text_with_translucent_background(input_image, output_image, text, font_path)
