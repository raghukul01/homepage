import sys

templete_file_name = sys.argv[1].strip()

# this is the defaul folder from which all files will be rendered
if templete_file_name.split("/",1)[1] == "index_templete.txt":
	output_file_name = "index.html"
	sec = "sections/" 
else:
	output_file_name = "blog.html"
	sec = "blog_html/"

output_file = open(output_file_name, "w")

with open(templete_file_name, "r") as templete:
	for line in templete:
		current = line.strip()
		if current[:1] == '#': # this file must be rendered
			# add this new file
			output_file.write("\n")

			sec_file_name = current[1:]
			current_file_name = sec + sec_file_name.strip()

			current_file = open(current_file_name, "r")
			output_file.write(current_file.read())
			
			output_file.write("\n")

		else:
			output_file.write(line)
