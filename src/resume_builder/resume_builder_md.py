from .resume_builder_utils import (
    # print_splash,
    format_phone_num,
    format_date,
    build_minimal_md_table,
    build_minimal_row_md_table,
    build_multiline_md_table,
    sort_exp,
)


def build_resume_exp_md(exp, openfile):
    exp_title = ""

    if exp["exp_type"] == "work":
        exp_title = exp["exp_role"]
    elif exp["exp_type"] == "education":
        exp_title = exp["education_cred"]
    elif exp["exp_type"] == "project":
        exp_title = exp["project_name"]

    openfile.write(f"### {exp_title} — _{exp["org_name"]}_ {{.exp-heading}}\n\n")

    start_date_str = format_date(exp["start_date"])
    end_date_str = "Present" if not exp["end_date"] else format_date(exp["end_date"])

    skill_header = "Core technologies" if exp["exp_type"] == "work" else "Core skills"
    cells = [
        [
            f"_**{start_date_str} — {end_date_str}**\n{exp["org_location"]}_",
            f"_**{skill_header}** — {', '.join(exp["skills"])}_",
        ]
    ]
    openfile.write(f"{build_multiline_md_table(cells)}\n")

    for highlight in exp["highlights"]:
        openfile.write(f"- {highlight}\n")
    openfile.write("\n")


def build_resume_full_md(resume_info):
    out_file_full_md = open("build/resume-full.md", "w", encoding="utf-8")

    # -----
    # Intro

    # print_splash(out_file_full_md, "md")

    out_file_full_md.write(f"# {resume_info["name"]} {{#title}}\n\n")
    out_file_full_md.write(f"### {resume_info["subtitle"]} {{#subtitle}}\n\n")

    # ------------
    # Contact Info

    num_break = 3
    contact_cells = []
    contact_cells_row_idx = -1
    for contact_idx in range(len(resume_info["contact_info"])):
        contact = resume_info["contact_info"][contact_idx]
        if contact_idx % num_break == 0:
            contact_cells.append([])
            contact_cells_row_idx += 1
        link = contact["info"]
        copy = contact["info"].replace("https://", "")

        is_email = contact["type"] == "email"
        is_phone = contact["type"] == "phone"
        if is_email:
            link = f"mailto:{contact["info"] }"
        if is_phone:
            link = f"tel:{format_phone_num(contact["info"], "html")}"
            copy = format_phone_num(contact["info"])
        contact_cells[contact_cells_row_idx].append(f"[{copy}]({link})")

    contacts_table = build_minimal_md_table(contact_cells)

    out_file_full_md.write(contacts_table)
    out_file_full_md.write("\n")

    # ------------
    # Objective

    out_file_full_md.write(f"## Objective\n\n")
    out_file_full_md.write(f"{resume_info["objective"]}\n\n")

    # ------------
    # Skills & Qualifications

    out_file_full_md.write(f"## Skills & Qualifications {{#skills-quals}}\n\n")

    skill_cells = []
    for skill in resume_info["skills_qualifications"]:
        skill_cells.append(skill)
    skills_table = build_multiline_md_table([skill_cells])
    out_file_full_md.write(skills_table)
    out_file_full_md.write("\n")

    # ------------
    # Technical Experience

    out_file_full_md.write(f"## Technical Experience\n\n")

    for work_exp in sorted(resume_info["work_experience"], key=sort_exp, reverse=True):
        build_resume_exp_md(work_exp, out_file_full_md)

    # ------------
    # Projects

    out_file_full_md.write(f"## Projects\n\n")

    for proj_exp in sorted(resume_info["projects"], key=sort_exp, reverse=True):
        build_resume_exp_md(proj_exp, out_file_full_md)

    # ------------
    # Technical Education

    out_file_full_md.write(f"## Education\n\n")

    for edu_exp in sorted(resume_info["education"], key=sort_exp, reverse=True):
        build_resume_exp_md(edu_exp, out_file_full_md)

    # ------------
    # About Me

    out_file_full_md.write(f"## About Me\n\n")
    out_file_full_md.write(f"{resume_info["about"]}\n")

    # -------
    # Cleanup
    # -------

    out_file_full_md.close()
    return 0
