import json
from .resume_builder_utils import print_splash


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
