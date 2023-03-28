import unittest
from unittest import TestCase

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Ivan")
        self.student_with_course = Student("Pesho", {'physics': ['Newton first low']})

    def test_instances_in_the_class(self):
        self.assertEqual(self.student.name, "Ivan")
        self.assertEqual(self.student_with_course.courses, {'physics': ['Newton first low']})

    def test_enroll_adding_course_notes_to_existing_course(self):
        result = self.student_with_course.enroll('physics', ['second Newton low'])
        self.assertEqual(self.student_with_course.courses['physics'][1], 'second Newton low')
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_enroll_adding_course_and_notes_if_non(self):
        result = self.student.enroll('math', ['new_notes'])
        self.assertEqual(self.student.courses['math'][0], 'new_notes')
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_adding_course_and_notes_if_non_with_third_param(self):
        result = self.student.enroll('math', ['new_notes'],'Y')
        self.assertEqual(self.student.courses['math'][0], 'new_notes')
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_adding_new_course_without_notes(self):
        result = self.student.enroll('math', 'adding', 'n')
        self.assertEqual(self.student.courses['math'], [])
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_to_course(self):
        result = self.student_with_course.add_notes('physics', 'notes to add')
        self.assertEqual(self.student_with_course.courses['physics'][1], 'notes to add')
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_to_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_course.add_notes('math', 'some notes')
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_course(self):
        results = self.student_with_course.leave_course('physics')
        self.assertEqual(len(self.student_with_course.courses), 0)
        self.assertEqual(results, "Course has been removed")

    def test_leave_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('math')
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    unittest.main()
