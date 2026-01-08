import os
import urllib.parse

BASE_URL = "https://raw.githubusercontent.com/Atriace/DnD5e/refs/heads/main/"

DIRS = [
	"Gear",
	"Ammunition",
	"Armour",
	"Books",
	"Food",
	"Gaming",
	"Instruments",
	"Magical",
	"Mounts",
	"Potions",
	"Siege",
	"Components",
	"Tools",
	"Trade",
	"Treasure",
	"Vehicles",
	"Weapons",
	"Spells",
	"Homebrew_Spells"
]

OUTPUT_DIR = "css"
OUTPUT_FILE = "selectors.css"

def main():
	# create output directory if it doesn't exist
	if not os.path.exists(OUTPUT_DIR):
		os.makedirs(OUTPUT_DIR)

	total_files = 0
	out_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
	out = open(out_path, "w", encoding="utf-8")

	for directory in DIRS:
		if not os.path.exists(directory):
			continue

		files = []

		for entry in os.listdir(directory):
			if entry.lower().endswith(".jpg") or entry.lower().endswith(".png"):
				files.append(entry)

		files.sort()
		total_files += len(files)

		for filename in files:
			name = filename[:-4]
			encoded_selector = urllib.parse.quote(name)
			encoded_filename = urllib.parse.quote(filename)
			encoded_dir = urllib.parse.quote(directory)

			file_url = BASE_URL + encoded_dir + "/" + encoded_filename

			out.write('.macrobox[data-macroid$="' + encoded_selector + '"] {\n')
			out.write('\tbackground-image: url(' + file_url + ');\n')
			out.write('}\n\n')

	out.close()

	print("Generated " + str(total_files) + " selectors into " + out_path)

if __name__ == "__main__":
	main()
