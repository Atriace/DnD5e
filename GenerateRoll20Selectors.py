import os
import urllib.parse

BASE_URL = "https://raw.githubusercontent.com/Atriace/DnD5e/refs/heads/main/Spells/"
SPELL_DIRS = ["Spells", "Homebrew_Spells"]
OUTPUT_FILE = "spell_selectors.css"

def main():
	total_files = 0
	out = open(OUTPUT_FILE, "w", encoding="utf-8")

	for directory in SPELL_DIRS:
		if not os.path.exists(directory):
			continue

		files = []

		for entry in os.listdir(directory):
			if entry.lower().endswith(".jpg"):
				files.append(entry)

		files.sort()  # sort each directory individually
		total_files += len(files)

		for filename in files:
			spell_name = filename[:-4]  # strip .jpg
			encoded_selector = urllib.parse.quote(spell_name)
			encoded_url = urllib.parse.quote(filename)

			# adjust URL for Homebrew_Spells
			if directory == "Homebrew_Spells":
				file_url = BASE_URL.replace("/Spells/", "/Homebrew_Spells/") + encoded_url
			else:
				file_url = BASE_URL + encoded_url

			out.write('.macrobox[data-macroid*="' + encoded_selector + '"] {\n')
			out.write('\tbackground-image: url(' + file_url + ');\n')
			out.write('}\n\n')

	out.close()

	print("Generated " + str(total_files) + " selectors into " + OUTPUT_FILE)

if __name__ == "__main__":
	main()
