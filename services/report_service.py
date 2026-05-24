from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
import re

styles = getSampleStyleSheet()

def markdown_to_pdf_elements(md_text, elements):
    lines = md_text.split("\n")
    
    for line in lines:
        line = line.strip()
        if not line:
            elements.append(Spacer(1, 8))
            continue

        line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)

        line = re.sub(r'\*(.*?)\*', r'\1', line)
        
        if line.startswith("# "):
            elements.append(Spacer(1, 10))
            elements.append(Paragraph(line[2:], styles["Heading1"]))
        
        elif line.startswith("## "):
            elements.append(Spacer(1, 8))
            elements.append(Paragraph(line[3:], styles["Heading2"]))
        
        elif line.startswith("### "):
            elements.append(Spacer(1, 6))
            elements.append(Paragraph(line[4:], styles["Heading3"]))

        elif line.startswith("* ") or line.startswith("- "):
            elements.append(Paragraph(f"• {line[2:]}", styles["BodyText"]))

        else:
            elements.append(Paragraph(line, styles["BodyText"]))
    
    return elements


def generate_pdf_report(symbol, stock_data, ai_analysis):
    filename = f"{symbol}_report.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    title = Paragraph(
        f"<b>{symbol} Financial Report</b>",
        styles["Title"]
    )
    elements.append(title)
    elements.append(Spacer(1, 20))

    latest_price = Paragraph(
        f"<b>Latest Close:</b> {stock_data['latest_close']}",
        styles["BodyText"]
    )
    elements.append(latest_price)

    recommendation = Paragraph(
        f"<b>Recommendation:</b> {stock_data['signals']['recommendation']}",
        styles["BodyText"]
    )
    elements.append(recommendation)
    elements.append(Spacer(1, 20))

    ai_title = Paragraph("<b>AI Financial Analysis</b>", styles["Heading2"])
    elements.append(ai_title)

    elements = markdown_to_pdf_elements(ai_analysis, elements)

    doc.build(elements)
    return filename