import json


def parse_resume():
    # -------------
    # LOADING FILES
    # -------------

    resume_data = open("data/resume.json", "r", encoding="utf-8")
    contact_data = open("data/contacts.json", "r", encoding="utf-8")
    experience_data = open("data/experience.json", "r", encoding="utf-8")
    cover_data = open("data/cover.json", "r", encoding="utf-8")

    resume_info = json.load(resume_data)
    contact_info = json.load(contact_data)
    experience_info = json.load(experience_data)
    cover_info = json.load(cover_data)

    # ---------------
    # DEFINITIONS
    # ---------------

    modes = {
        "full": {"desc": "Full resume (2 pg max)"},
        "short": {"desc": "Compact resume (1 pg max)"},
        "tiny": {"desc": "Very compact summary (150 char max)"},
        "cover": {"desc": "Cover letter"},
    }

    complete_resume_info = {
        "resume": resume_info,
        "contact": contact_info,
        "experience": experience_info,
        "cover": cover_info,
    }

    return complete_resume_info
