#Tentei fazer de novo, mas de outra forma
#pip install fpdf2
from fpdf import FPDF

class PDF(FPDF):
    def add_title(self):
        # Setting font: helvetica Bold 40
        self.set_font("helvetica", "B", 40)
        #Setting vertical position
        self.set_y(30)
        # Printing exercise title:
        self.cell(0, 20, "Shirtificate CS50", new_x="LMARGIN", new_y="NEXT", align="C")
        # Performing a line break:
        self.ln(20)

    def add_shirt(self):
        self.image("./shirtificate.png", x=10, y=80, w=210-20)

    def add_shirt_message(self, name):
        # Setting font: helvetica 22
        self.set_font("helvetica", "", 22)
        #Settirn text color:
        self.set_text_color(255,255,255)
        #Setting text vertical position
        self.set_y(140)
        # Printing shit's message:
        self.cell(0, 10, f"{name} took CS50", new_x="LMARGIN", new_y="NEXT", align="C")


    def print_shirtificate(self):
        self.add_page()
        self.add_title()
        self.add_shirt()
        self.add_shirt_message(input("Name: "))
        self.output("shirtificate2.pdf")

    @classmethod
    def new_shirt(cls):
        return cls().print_shirtificate()


def main():
    PDF.new_shirt()


if __name__ == "__main__":
    main()