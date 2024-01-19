from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.lib.pagesizes import letter
from reportlab.platypus import TableStyle, Paragraph
from reportlab.lib import colors


def accepted(courses_title, courses_score, user_name, file_name):
    buffer = BytesIO()

    data = [
        courses_title,
        courses_score
    ]

    style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')
    ])
    ts = TableStyle(
        [
            ('BOX', (0, 0), (-1, -1), 2, colors.black),
            ('LINEBEFORE', (0, 1), (1, 0), 2, colors.black),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)

        ]
    )
    pdf = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )

    table = Table(data, colWidths=[100, 200])

    table.setStyle(style)
    table.setStyle(ts)

    header_text = f"username: {user_name}"
    styles = getSampleStyleSheet()
    header_paragraph = Paragraph(header_text, styles['Heading1'])

    elms = [header_paragraph, table]
    pdf.build(elms)


    buffer.seek(0)
    return buffer.read()
