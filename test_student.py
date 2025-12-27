from student import student_details

def test_student_details():
    expected_output = {
        "s.usn": "01fe24bca280",
        "s.name": "alice",
        "division": "E",
        "age": 14,
    }
    assert student_details("01fe24bca280", "alice", "E", 14) == expected_output