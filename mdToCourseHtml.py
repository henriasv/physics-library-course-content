import shutil
import errno
import os
import markdown
from markdown.extensions import Extension

import json

courseDefinitionFile = "course.json"

with open(courseDefinitionFile) as ifile:
	courseDefinition = json.load(ifile)
	courseName = courseDefinition["name"]

os.makedirs(courseName, exist_ok=True)

shutil.copy(courseDefinitionFile, os.path.join(courseName, courseDefinitionFile))

for module in courseDefinition["modules"]:
	filename = module["id"]+".md"
	if filename in os.listdir("markdown"):
		print(filename)
		with open(os.path.join("markdown", filename)) as ifile:
			fileHead = filename.replace(".md", "")
			text = ifile.read()
			md = markdown.Markdown(output_format="html5")
			html = md.convert(text)
			with open(os.path.join(courseName, fileHead+".html"), "w") as ofile:
				ofile.write(html)
	else:
		raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)

os.system("cp -r fysikk2 $HOME/repos/e-learning-simple/storage/app/courses/")
os.system("cp oppgaver/* $HOME/repos/e-learning-simple/storage/app/exercises/")
