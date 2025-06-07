from .resume_builder_utils import (
    # print_splash,
    format_phone_num,
    format_date,
    build_minimal_md_table,
    build_minimal_row_md_table,
)


def build_resume_full_md(resume_info):
    out_file_full_md = open("build/resume-full.md", "w", encoding="utf-8")

    # -----
    # Intro

    # print_splash(out_file_full_md, "md")

    out_file_full_md.write(f"# {resume_info["name"]}\n\n")
    out_file_full_md.write(f"### {resume_info["subtitle"]}\n\n")

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

        start_date_str = format_date(work_exp["start_date"])
        end_date_str = (
            "Present" if not work_exp["end_date"] else format_date(work_exp["end_date"])
        )

        cells = [
            f"{start_date_str} — {end_date_str}",
            work_exp["org_location"],
            f"Core technologies — {', '.join(work_exp["skills"])}",
        ]
        out_file_full_md.write(f"{build_minimal_row_md_table(cells)}\n")

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
        start_date_str = format_date(proj_exp["start_date"])
        end_date_str = (
            "Present" if not proj_exp["end_date"] else format_date(proj_exp["end_date"])
        )

        cells = [
            f"{start_date_str} — {end_date_str}",
            proj_exp["org_location"],
            f"Core skills — {', '.join(proj_exp["skills"])}",
        ]
        out_file_full_md.write(f"{build_minimal_row_md_table(cells)}\n")

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
        start_date_str = format_date(edu_exp["start_date"])
        end_date_str = (
            "Present" if not edu_exp["end_date"] else format_date(edu_exp["end_date"])
        )

        cells = [
            f"{start_date_str} — {end_date_str}",
            edu_exp["org_location"],
            f"Core skills — {', '.join(edu_exp["skills"])}",
        ]
        out_file_full_md.write(f"{build_minimal_row_md_table(cells)}\n")

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
