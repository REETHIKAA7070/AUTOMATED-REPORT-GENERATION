from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

file = open("data.txt", "r")
lines = file.readlines()
file.close()

total = 0
students = []

for line in lines:
    name, mark = line.strip().split(",")
    mark = int(mark)
    students.append((name, mark))
    total += mark

average = total / len(students)

pdf = canvas.Canvas("Student_Report.pdf", pagesize=A4)
pdf.setFont("Helvetica", 12)

pdf.drawString(50, 800, "AUTOMATED STUDENT REPORT")
pdf.drawString(50, 770, "------------------------")

y = 740
for s in students:
    pdf.drawString(50, y, f"Name: {s[0]} | Marks: {s[1]}")
    y -= 20

pdf.drawString(50, y - 20, f"Average Marks: {average}")
pdf.save()

print("PDF GENERATED")
