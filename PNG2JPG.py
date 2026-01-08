import os
from PIL import Image

# ==== CONFIG ====
BG_COLOR = (25, 25, 25)  # #191919
# ================

def main():
	total = 0

	for root, dirs, files in os.walk("."):
		for name in files:
			if not name.lower().endswith(".png"):
				continue

			in_path = os.path.join(root, name)
			out_name = name[:-4] + ".jpg"
			out_path = os.path.join(root, out_name)

			print("Converting:", in_path, "->", out_path)

			try:
				img = Image.open(in_path).convert("RGBA")

				# Create a background image
				bg = Image.new("RGB", img.size, BG_COLOR)
				# Paste the PNG over the background using alpha as mask
				bg.paste(img, mask=img.split()[3])  # alpha channel as mask

				bg.save(out_path, "JPEG", quality=95)
				total += 1
			except Exception as e:
				print("FAILED:", in_path)
				print(str(e))

	print("Converted", total, "files to JPG with background", BG_COLOR)

if __name__ == "__main__":
	main()
