#pip install fpdf2
from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_margin(10)
pdf.set_font("helvetica", "B", 40)
pdf.cell(190, 60, "CS50 Shirtificate", align="C", new_x="LEFT", new_y="NEXT")
pdf.image("./shirtificate.png", x=10, y=70, w=190)
pdf.set_font("helvetica", size=22)
pdf.set_text_color(255,255,255)
pdf.cell(190, 140, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")