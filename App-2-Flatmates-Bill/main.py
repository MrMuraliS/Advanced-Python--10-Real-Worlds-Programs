from flat import Bill, Flatmate
from reports import PdfReport

the_bill = Bill(amount=float(input('Enter the total bill Amount: ')),
                period=input('Enter the month of bill, Eg. December 2021: '))
RoomMate1 = input('Enter the Name of the Room Mate 1: ')
RoomMate1 = Flatmate(name=RoomMate1,
                     days_in_house=float(input(f'How many days did {RoomMate1} stay in the Room during bill period: ')))
RoomMate2 = input('Enter the Name of the Room Mate 2: ')
RoomMate2 = Flatmate(name=RoomMate2,
                     days_in_house=float(input(f'How many days did {RoomMate2} stay in the Room during bill period: ')))

print(f"{RoomMate1.name} Pays: ", RoomMate1.pays(bill=the_bill, flatmate2=RoomMate2))
print(f"{RoomMate2.name} Pays: ", RoomMate2.pays(bill=the_bill, flatmate2=RoomMate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=RoomMate1, flatmate2=RoomMate2, bill=the_bill)
