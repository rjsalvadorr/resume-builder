import json


def print_splash(openfile, filetype="html"):
    splash_graphic = "\n"
    splash_graphic += "<!--------------------------------\n"
    splash_graphic += "   R E S U M E    B U I L D E R   \n"
    splash_graphic += "----------------------------------\n"
    splash_graphic += "   by Salvador Workshop           \n"
    splash_graphic += "--------------------------------->\n"
    splash_graphic += "\n"

    # print(splash_graphic)
    openfile.write(splash_graphic)


def format_phone_num(phone_num, type="txt"):
    country_code = "1"
    area_code = phone_num[0:3]
    mid = phone_num[3:6]
    end = phone_num[6:10]

    output_num = f"({area_code}) {mid} {end}"

    if type == "html":
        output_num = f"+{country_code}{area_code}{phone_num}"

    return output_num


def build_resume_full_md(resume_info):
    out_file_full_md = open("build/resume-full.md", "w", encoding="utf-8")

    # -----
    # Intro

    print_splash(out_file_full_md, "md")

    out_file_full_md.write(f"# {resume_info["name"]}\n\n")
    out_file_full_md.write(f"#### {resume_info["subtitle"]}\n\n")

    # ------------
    # Contact Info

    for contact in resume_info["contact_info"]:
        link = contact["info"]
        copy = contact["info"].replace("https://", "")

        is_email = contact["type"] == "email"
        is_phone = contact["type"] == "phone"
        if is_email:
            link = f"mailto:{contact["info"] }"
        if is_phone:
            link = f"tel:{format_phone_num(contact["info"], "html")}"
            copy = format_phone_num(contact["info"])

        out_file_full_md.write(f"[{copy}]({link})  \n")
    out_file_full_md.write("\n")

    # ------------
    # Objective

    out_file_full_md.write(f"## Objective\n\n")
    out_file_full_md.write(f"{resume_info["objective"]}\n\n")

    # ------------
    # Skills & Qualifications

    out_file_full_md.write(f"## Skills & Qualifications\n\n")

    for skill in resume_info["skills_qualifications"]:
        out_file_full_md.write(f"- {skill}\n")
    out_file_full_md.write("\n")

    # ------------
    # Technical Experience

    out_file_full_md.write(f"## Technical Experience\n\n")

    for work_exp in resume_info["work_experience"]:
        out_file_full_md.write(
            f"### {work_exp["exp_role"]}, {work_exp["org_name"]}\n\n"
        )

        end_date_str = "Present" if not work_exp["end_date"] else work_exp["end_date"]
        out_file_full_md.write(f"_{work_exp["start_date"]} — {end_date_str}  \n")
        out_file_full_md.write(f"{work_exp["org_location"]}  \n")
        out_file_full_md.write(
            f"Core technologies — {', '.join(work_exp["skills"])}_\n\n"
        )
        for highlight in work_exp["highlights"]:
            out_file_full_md.write(f"- {highlight}\n")
        out_file_full_md.write("\n")

    # ------------
    # Projects

    out_file_full_md.write(f"## Projects\n\n")

    for proj_exp in resume_info["projects"]:
        out_file_full_md.write(
            f"### {proj_exp["project_name"]}, {proj_exp["org_name"]}\n\n"
        )
        end_date_str = "Present" if not proj_exp["end_date"] else proj_exp["end_date"]
        out_file_full_md.write(f"_{proj_exp["start_date"]} — {end_date_str}  \n")
        out_file_full_md.write(f"{proj_exp["org_location"]}  \n")
        out_file_full_md.write(f"Core skills — {', '.join(proj_exp["skills"])}_\n\n")
        for highlight in proj_exp["highlights"]:
            out_file_full_md.write(f"- {highlight}\n")
        out_file_full_md.write("\n")

    # ------------
    # Technical Education

    out_file_full_md.write(f"## Technical Education\n\n")

    for edu_exp in resume_info["education"]:
        out_file_full_md.write(
            f"### {edu_exp["education_cred"]}, {edu_exp["org_name"]}\n\n"
        )
        end_date_str = "Present" if not edu_exp["end_date"] else edu_exp["end_date"]
        out_file_full_md.write(f"_{edu_exp["start_date"]} — {end_date_str}  \n")
        out_file_full_md.write(f"{edu_exp["org_location"]}  \n")
        out_file_full_md.write(
            f"Core technologies — {', '.join(edu_exp["skills"])}_\n\n"
        )
        for highlight in edu_exp["highlights"]:
            out_file_full_md.write(f"- {highlight}\n")
        out_file_full_md.write("\n")

    # ------------
    # About Me

    out_file_full_md.write(f"## About Me\n\n")
    out_file_full_md.write(f"{resume_info["about"]}\n")

    # -------
    # Cleanup
    # -------

    out_file_full_md.close()
    return 0


def build_resume_full_txt(resume_info):
    out_file_full_txt = open("build/resume-full.txt", "w", encoding="utf-8")

    # -----
    # Intro

    print_splash(out_file_full_txt, "txt")

    # ------
    # Resume

    # print(json.dumps(resume_info, indent=2))
    out_file_full_txt.write(json.dumps(resume_info, indent=2))
    out_file_full_txt.write("\n")

    # -------
    # Cleanup
    # -------

    out_file_full_txt.close()
    return 0


def build_resume_full(complete_resume_info):
    # print("\nbuild_resume_full()\n")
    # print(complete_resume_info)

    build_resume_full_txt(complete_resume_info["resume"])
    build_resume_full_md(complete_resume_info["resume"])

    return 0


def build_resume_short(complete_resume_info):
    # print("\nbuild_resume_short()\n")
    # print(complete_resume_info)
    out_file_short = open("build/resume-short.txt", "w", encoding="utf-8")
    return 0


def build_resume_tiny(complete_resume_info):
    # print("\nbuild_resume_tiny()\n")
    # print(complete_resume_info)
    out_file_tiny = open("build/resume-tiny.txt", "w", encoding="utf-8")
    return 0


def build_cover_letter(complete_resume_info):
    # print("\nbuild_cover_letter()\n")
    # print(complete_resume_info)
    out_file_cover = open("build/cover.txt", "w", encoding="utf-8")

    # -----
    # Intro

    print_splash(out_file_cover)

    # ------------
    # Cover Letter

    cover_obj = json.dumps(complete_resume_info["cover"], indent=2)
    # print(cover_obj)
    out_file_cover.write(cover_obj)
    out_file_cover.write("\n")

    # -------
    # Cleanup
    # -------

    out_file_cover.close()
    return 0
