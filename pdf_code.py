from fpdf import FPDF


def generate_pdf(good_name, good_price):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Receipt nr.1", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Article: {good_name}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Price: {good_price}", ln=1)

    pdf.output("receipt.pdf")
