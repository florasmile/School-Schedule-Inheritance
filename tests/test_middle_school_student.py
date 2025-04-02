from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    # Assert
    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes)

    # Assert
    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert not ellis.gets_transportation

def test_middle_school_student_summary_with_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    # Act
    summary_message = ellis.summary()
    expected_summary_message = "Ellis is a junior enrolled in 1 classes: Painting\nEllis has school transportation."

    # Assert
    assert summary_message == expected_summary_message

def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = MiddleSchoolStudent(name, grade, classes)

    # Act
    summary_message = ellis.summary()
    expected_summary_message = "Ellis is a junior enrolled in 1 classes: Painting\nEllis doesn't have school transportation."

    # Assert
    assert summary_message == expected_summary_message
