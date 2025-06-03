def build_resume_full(complete_resume_info):
    out_file_full = open("../../build/resume-full.html", "w", encoding="utf-8")

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

    print(complete_resume_info.resume)
    out_file_full.write(complete_resume_info.resume)

    print(complete_resume_info.contact)
    out_file_full.write(complete_resume_info.contact)

    # -------------------------------
    # Experience, Education, Projects

    print(complete_resume_info.experience)
    out_file_full.write(complete_resume_info.experience)

    # ------------
    # Cover Letter

    print(complete_resume_info.cover)
    out_file_full.write(complete_resume_info.cover)

    # -------
    # CLEANUP
    # -------

    out_file_full.close()


def build_resume_short(complete_resume_info):
    out_file_short = open("../../build/resume-short.html", "w", encoding="utf-8")
    return 0


def build_resume_tiny(complete_resume_info):
    out_file_tiny = open("../../build/resume-tiny.html", "w", encoding="utf-8")
    return 0


def build_cover_letter(complete_resume_info):
    out_file_cover = open("../../build/cover.html", "w", encoding="utf-8")
    return 0
