import os
import webbrowser
from fpdf import FPDF


class PdfReport:
    """
    Generates a pdf file that contains data about flatmates such as
    their name, due amount for the period of the duration.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Image
        pdf.image('./files/house.png', w=50, h=50)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=50, txt='Flatmates Bill', border=1, align='C', ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=0)

        pdf.output(f"files/{self.filename}")

        webbrowser.open('file://'+os.path.realpath(f"files/{self.filename}"))
