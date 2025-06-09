from datetime import datetime
from pprint import pprint

html_newline = "<br>"
typ_tbl_char_padding = 2 + len(html_newline)


def print_splash(openfile, filetype="html"):
    splash_graphic = "\n"
    splash_graphic += "<!--------------------------------\n"
    splash_graphic += "   R E S U M E    B U I L D E R   \n"
    splash_graphic += "----------------------------------\n"
    splash_graphic += "   by Salvador Workshop           \n"
    splash_graphic += "--------------------------------->\n"
    splash_graphic += "\n"

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


def build_minimal_row_md_table(cells):
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


def build_minimal_md_table(cells):
    """Builds a minimal (headless) two-dimensional table. Data formata: cells[rowIdx][colIdx]"""
    borders = []
    contentlines = {}
    contentlines_raw = {}
    line_lengths_by_col = {}
    highest_row_idx = 0
    highest_col_idx = 0

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

            curr_line = cells[row_idx][col_idx]
            contentlines_raw[row_idx].append(curr_line)
            line_lengths_by_col[col_idx].append(len(curr_line))

    # ---
    # Preparing
    # ---

    for row_idx in range(highest_col_idx + 1):
        borders.append(
            get_dashline(max(line_lengths_by_col[row_idx]) + typ_tbl_char_padding)
        )

    for row_idx in range(len(cells)):
        contentlines[row_idx] = []
        contentline_pts = []
        for col_idx in range(len(cells[row_idx])):
            max_line_len = max(line_lengths_by_col[col_idx])
            contentline_part = get_padline(
                contentlines_raw[row_idx][col_idx],
                max_line_len + typ_tbl_char_padding,
            )
            contentline_pts.append(contentline_part)
        contentlines[row_idx].append("  ".join(contentline_pts))

    # ---
    # Writing
    # ---

    out_strs = ["  ".join(borders)]
    for content_row in contentlines:
        out_strs.append("\n".join(contentlines[content_row]))
    out_strs.append("  ".join(borders))
    out_str = "\n".join(out_strs) + "\n"

    return out_str


def build_multiline_md_table(cells):
    """Builds a minimal (headless) two-dimensional table with multiline cells. Data formata: cells[rowIdx][colIdx]"""
    borders = []
    contentlines = []
    contentlines_raw = {}
    line_lengths_by_col = {}
    line_nums_by_row = {}
    highest_row_idx = 0
    highest_col_idx = 0

    # ---
    # Reading
    # ---

    for row_idx in range(len(cells)):
        contentlines_raw[row_idx] = []
        if row_idx > highest_row_idx:
            highest_row_idx = row_idx
        if row_idx not in line_nums_by_row:
            line_nums_by_row[row_idx] = []

        for col_idx in range(len(cells[row_idx])):
            if col_idx not in line_lengths_by_col:
                line_lengths_by_col[col_idx] = []
            if col_idx > highest_col_idx:
                highest_col_idx = col_idx

            contentlines_raw[row_idx].append([])
            curr_line = cells[row_idx][col_idx]

            # check the lengths of each line in the cell
            raw_lines = curr_line.splitlines()

            highest_line_idx = 0
            for line_idx in range(len(raw_lines)):
                highest_line_idx += 1
                cell_line = raw_lines[line_idx]
                line_lengths_by_col[col_idx].append(len(cell_line))
                contentlines_raw[row_idx][col_idx].append(cell_line)
            line_nums_by_row[row_idx].append(highest_line_idx)

        line_nums_by_row[row_idx] = max(line_nums_by_row[row_idx])

    # ---
    # Preparing
    # ---

    for row_idx in range(highest_col_idx + 1):
        borders.append(
            get_dashline(max(line_lengths_by_col[row_idx]) + typ_tbl_char_padding)
        )

    total_lines = 0
    for max_line_num in line_nums_by_row.values():
        total_lines += max_line_num

    for row_idx in range(len(contentlines_raw)):
        max_lines = line_nums_by_row[row_idx]

        for l_idx in range(max_lines):
            line_parts = []

            for col_idx in range(len(contentlines_raw[row_idx])):
                max_line_len = max(line_lengths_by_col[col_idx])

                try:
                    c_line = contentlines_raw[row_idx][col_idx][l_idx]
                    if (
                        len(contentlines_raw[row_idx][col_idx]) > 1
                        and l_idx != len(contentlines_raw[row_idx]) - 1
                    ):
                        c_line += html_newline
                    else:
                        c_line += get_padline("", len(html_newline))
                except IndexError:
                    c_line = ""

                c_line_part = get_padline(
                    c_line,
                    max_line_len + typ_tbl_char_padding,
                )
                line_parts.append(c_line_part)

            contentlines.append("  ".join(line_parts))

    # ---
    # Writing
    # ---

    out_strs = ["  ".join(borders)]
    out_strs.append("\n".join(contentlines))
    borderpad = ""
    if highest_row_idx == 0:
        # "It is possible for a multiline table to have just one row, but the row should
        # be followed by a blank line (and then the row of dashes that ends the table),
        # or the table may be interpreted as a simple table."
        borderpad = "\n"
    out_strs.append(borderpad + "  ".join(borders))
    out_str = "\n".join(out_strs) + "\n"

    return out_str
