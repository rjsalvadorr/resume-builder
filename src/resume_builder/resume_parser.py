import random
import json
from random import randrange
from datetime import datetime, timedelta


# -------------
# LOADING FILES
# -------------

contact_data = open("data/contacts.json", "r", encoding="utf-8")
experience_data = open("data/experience.json", "r", encoding="utf-8")
resume_data = open("data/resume.json", "r", encoding="utf-8")
cover_data = open("data/cover.json", "r", encoding="utf-8")

contact_info = json.load(contact_data)
experience_info = json.load(experience_data)
resume_info = json.load(resume_data)
cover_info = json.load(cover_data)

# with open('sample.json', 'r') as openfile:
#     json_object = json.load(openfile)


# ---------------
# DEFINITIONS
# ---------------

modes = {
    "full": {"desc": "Full resume (2 pg max)"},
    "short": {"desc": "Compact resume (1 pg max)"},
    "tiny": {"desc": "Very compact summary (150 char max)"},
    "cover": {"desc": "Cover letter"},
}


# ---------------
# TEXT GENERATION
# ---------------

out_file_full = open("build/resume-full.html", "w", encoding="utf-8")
out_file_short = open("build/resume-short.html", "w", encoding="utf-8")
out_file_tiny = open("build/resume-tiny.html", "w", encoding="utf-8")
out_file_cover = open("build/cover.html", "w", encoding="utf-8")


# -----
# Intro

splash_graphic = "\n"
splash_graphic += "<!--------------------------------\n"
splash_graphic += "   R E S U M E    B U I L D E R   \n"
splash_graphic += "----------------------------------\n"
splash_graphic += "   by Salvador Workshop           \n"
splash_graphic += "--------------------------------->\n"
splash_graphic += "\n"

print(splash_graphic)
out_file_full.write(splash_graphic)


# ------
# Resume

print(resume_info)
out_file_full.write(resume_info)

print(contact_info)
out_file_full.write(contact_info)


# -------------------------------
# Experience, Education, Projects

print(experience_info)
out_file_full.write(experience_info)


# ------------
# Cover Letter

print(cover_info)
out_file_full.write(cover_info)


# -------
# CLEANUP
# -------

out_file_full.close()
