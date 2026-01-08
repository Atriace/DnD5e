import os
import cairosvg

# ==== CONFIG ====
PIXEL_SIZE = 256
# ================

def main():
	total = 0

	for root, dirs, files in os.walk("."):
		for name in files:
			if not name.lower().endswith(".svg"):
				continue

			in_path = os.path.join(root, name)
			out_name = name[:-4] + ".png"
			out_path = os.path.join(root, out_name)

			print("Converting:", in_path, "->", out_path)

			try:
				cairosvg.svg2png(
					url=in_path,
					write_to=out_path,
					output_width=PIXEL_SIZE,
					output_height=PIXEL_SIZE,
					background_color=None
				)
				total += 1
			except Exception as e:
				print("FAILED:", in_path)
				print(str(e))

	print("Converted", total, "files in place")

if __name__ == "__main__":
	main()
