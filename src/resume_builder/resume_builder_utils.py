from datetime import datetime

typ_tbl_char_padding = 2


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
        output_num = f"+{country_code}{phone_num}"

    return output_num


def format_date(date_str, type="txt"):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    output_str = dt.strftime("%b %Y")

    return output_str


def get_dashline(line_len):
    out_str = ""
    for idx in range(line_len):
        out_str = out_str + "-"

    return out_str


def get_dashline_for_str(str):
    line_len = len(str) + typ_tbl_char_padding

    out_str = ""
    for idx in range(line_len):
        out_str = out_str + "-"

    return out_str


def get_padline(str, line_len):
    str_len = len(str)
    diff_len = line_len - str_len

    out_str = str
    for idx in range(diff_len):
        out_str = out_str + " "

    return out_str


def build_minimal_row_table(cells):
    """Builds a minimal (headless) one-row table."""
    borders = []
    contentlines = []

    for cell_str in cells:
        dashline = get_dashline_for_str(cell_str)
        borders.append(dashline)
        contentlines.append(get_padline(cell_str, len(dashline)))

    out_strs = ["  ".join(borders)]
    out_strs.append("  ".join(contentlines))
    out_strs.append("  ".join(borders))
    out_str = "\n".join(out_strs) + "\n"

    return out_str


def build_minimal_table(cells):
    """Builds a minimal (headless) two-dimensional table. Data formata: cells[rowIdx][colIdx]"""
    borders = []
    contentlines = {}
    contentlines_raw = {}
    line_lengths_by_col = {}
    highest_row_idx = 0
    highest_col_idx = 0
    content_elements = 0

    # ---
    # Reading
    # ---

    for row_idx in range(len(cells)):
        contentlines_raw[row_idx] = []
        if row_idx > highest_row_idx:
            highest_row_idx = row_idx
        for col_idx in range(len(cells[row_idx])):
            if col_idx not in line_lengths_by_col:
                line_lengths_by_col[col_idx] = []
            if col_idx > highest_col_idx:
                highest_col_idx = col_idx
            content_elements += 1

            curr_line = cells[row_idx][col_idx]
            contentlines_raw[row_idx].append(curr_line)
            line_lengths_by_col[col_idx].append(len(curr_line))

    print(line_lengths_by_col)
    print(highest_row_idx)
    print(highest_col_idx)
    print(contentlines_raw)

    # ---
    # Preparing
    # ---

    for row_idx in range(highest_col_idx + 1):
        borders.append(
            get_dashline(max(line_lengths_by_col[row_idx]))
        )

    for row_idx in range(len(cells)):
        contentlines[row_idx] = []
        contentline_pts = []
        for col_idx in range(len(cells[row_idx])):
            contentline_pts.append(
                get_padline(
                    contentlines_raw[row_idx][col_idx],
                    max(line_lengths_by_col[row_idx]),
                )
            )
        contentlines[row_idx].append("  ".join(contentline_pts))

    # ---
    # Writing
    # ---

    out_strs = ["  ".join(borders)]
    for content_row in contentlines:
        out_strs.append("\n".join(contentlines[content_row]))
    out_strs.append("  ".join(borders))
    out_str = "\n".join(out_strs) + "\n"

    print(out_str)

    return 0
