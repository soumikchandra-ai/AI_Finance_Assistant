from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
styles=getSampleStyleSheet()

def generate_pdf_report(symbol, stock_data, ai_analysis):

    filename = f"{symbol}_report.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    elements = []

    title = Paragraph(
        f"<b>{symbol} Financial Report</b>",
        styles["Title"]
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    latest_price = Paragraph(
        f"""
        <b>Latest Close:</b>
        {stock_data["latest_close"]}
        """,
        styles["BodyText"]
    )

    elements.append(latest_price)

    recommendation = Paragraph(
        f"""
        <b>Recommendation:</b>
        {stock_data["signals"]["recommendation"]}
        """,
        styles["BodyText"]
    )

    elements.append(recommendation)

    elements.append(Spacer(1, 20))

    ai_title = Paragraph(
        "<b>AI Financial Analysis</b>",
        styles["Heading2"]
    )

    elements.append(ai_title)

    ai_text = Paragraph(
        ai_analysis.replace("\n", "<br/>"),
        styles["BodyText"]
    )

    elements.append(ai_text)

    doc.build(elements)

    return filename