from resume_builder import resume_parser, resume_builder

resume_info = resume_parser.parse_resume()

resume_builder.build_resume_full(resume_info)
