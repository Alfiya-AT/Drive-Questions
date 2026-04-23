import csv

FILE = "students.txt"

subject_map = {
    "P": "Physics",
    "C": "Chemistry",
    "M": "Mathematics",
    "B": "Biology",
    "E": "Electronics",
    "S": "Computer Science"
}

subjects = ["Physics", "Chemistry", "Mathematics",
            "Computer Science", "Biology", "Electronics"]


# 🔹 Add Student
def add_student():
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)

        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")

        stream = input("Enter stream (e.g., PCMB): ").upper()

        # Convert stream → subjects
        chosen = []
        for ch in stream:
            if ch in subject_map:
                chosen.append(subject_map[ch])

        # Validate
        if len(chosen) != 4:
            print("❌ Please enter exactly 4 valid subjects")
            return

        marks_dict = {}

        for sub in subjects:
            if sub in chosen:
                marks_dict[sub] = int(input(f"Enter marks for {sub}: "))
            else:
                marks_dict[sub] = ""

        row = [sid, name] + [marks_dict[sub] for sub in subjects]
        writer.writerow(row)

        print("✅ Data stored\n")


# 🔹 Search
def search_student(search_id):
    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                if row[0] == search_id:
                    print_marksheet(row)
                    return

        print("❌ No data found")

    except FileNotFoundError:
        print("❌ File not found")


# 🔹 Print Marksheet
def print_marksheet(row):
    print("\n------------------------------------------")
    print("\tStudent Mark Sheet")
    print("------------------------------------------")
    print("Name       :", row[1])
    print("Student ID :", row[0])
    print("------------------------------------------")
    print("Subject\t\t\tMarks")
    print("------------------------------------------")

    total = 0
    count = 0

    for sub, mark in zip(subjects, row[2:]):
        if mark != "":
            mark = int(mark)
            print(f"{sub:<20} {mark}")
            total += mark
            count += 1

    avg = total / count if count else 0

    print("------------------------------------------")
    print("Total Marks        :", total)
    print("Average Marks      :", round(avg, 2))
    print("------------------------------------------\n")


# 🔥 Main
add_student()
sid = input("Enter ID to search: ")
search_student(sid)