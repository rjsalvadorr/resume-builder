import json


def print_splash(openfile, filetype="html"):
    splash_graphic = "\n"
    splash_graphic += "<!--------------------------------\n"
    splash_graphic += "   R E S U M E    B U I L D E R   \n"
    splash_graphic += "----------------------------------\n"
    splash_graphic += "   by Salvador Workshop           \n"
    splash_graphic += "--------------------------------->\n"
    splash_graphic += "\n"

    print(splash_graphic)
    openfile.write(splash_graphic)


def build_resume_full(complete_resume_info):
    print("\nbuild_resume_full()\n")
    print(complete_resume_info)
    out_file_full = open("build/resume-full.txt", "w", encoding="utf-8")

    # -----
    # Intro

    print_splash(out_file_full)

    # ------
    # Resume

    resume_obj = json.dumps(complete_resume_info["resume"], indent=2)
    print(resume_obj)
    out_file_full.write(resume_obj)
    out_file_full.write("\n")

    # -------
    # Cleanup
    # -------

    out_file_full.close()
    return 0


def build_resume_short(complete_resume_info):
    print("\nbuild_resume_short()\n")
    print(complete_resume_info)
    out_file_short = open("build/resume-short.txt", "w", encoding="utf-8")
    return 0


def build_resume_tiny(complete_resume_info):
    print("\nbuild_resume_tiny()\n")
    print(complete_resume_info)
    out_file_tiny = open("build/resume-tiny.txt", "w", encoding="utf-8")
    return 0


def build_cover_letter(complete_resume_info):
    print("\nbuild_cover_letter()\n")
    print(complete_resume_info)
    out_file_cover = open("build/cover.txt", "w", encoding="utf-8")

    # -----
    # Intro

    print_splash(out_file_cover)

    # ------------
    # Cover Letter

    cover_obj = json.dumps(complete_resume_info["cover"], indent=2)
    print(cover_obj)
    out_file_cover.write(cover_obj)
    out_file_cover.write("\n")

    # -------
    # Cleanup
    # -------

    out_file_cover.close()
    return 0
