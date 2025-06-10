import pandoc
from pandoc.types import *
from .resume_builder_utils import print_splash, format_phone_num, format_date


def build_resume_full_pdf():
    markdown_data = open("build/resume-full.md", "r", encoding="utf-8")
    doc = pandoc.read(markdown_data.read())

    weasyprint_opts = "-e utf8 --hinting"
    write_opts = [
        "--css",
        "src/resume_builder/util/r_style.css",
        "--to",
        "html",
        "--pdf-engine-opt",
        weasyprint_opts,
    ]
    pandoc.write(doc, "build/resume-full.pdf", format="pdf", options=write_opts)

    return 0
