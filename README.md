Hosted at: cse.iitk.ac.in/users/raghukul

Any line starting with '#' in templetes/index_templete.txt will be rendered from sections/ where file name is written after '#'

Usage of generate_index.py script:
	`python generate_index.py path/to/template`

To add a new section:
	1. Add the html file in sections/
	2. add the file name with # in the templetes/index_templete.txt file, and place this line, where it needs to be rendered
	3. also add this section detail in sections/sidebar.html
	4. finally run python scripts/generate_index.py

To add a new blog
	