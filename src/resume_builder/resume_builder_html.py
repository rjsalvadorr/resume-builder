import pandoc
from pandoc.types import *
from .resume_builder_utils import print_splash, format_phone_num, format_date


def build_resume_full_html():
    markdown_data = open("build/resume-full.md", "r", encoding="utf-8")
    doc = pandoc.read(markdown_data.read())
    pandoc.write(doc, "build/resume-full.html")

    return 0
