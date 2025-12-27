def student_details(usn, name, division, age):
    result = (
        f"student.usn={usn}\n"
        f"student.name={name}\n"
        f"division={division}\n"
        f"age={age}\n"
    )
    return result


if __name__ == "__main__":
    usn = "01fe24bca280"
    name = "alice"
    division = "E"
    age = 14
    print(student_details(usn, name, division, age))