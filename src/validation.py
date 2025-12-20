def is_valid_grade(grade: float) -> bool:
  """
  Valid grades: 0.0 – 10.0
  """


def has_passed_course(student_id: int, course: str, history: list) -> bool:
  """
  Checks if student has passed a prerequisite course
  Pass threshold: grade >= 5.0
  """


def check_prerequisites(student_id: int, course: str, curriculum: dict, history: list) -> bool:
  """
  Returns True if all prerequisites are satisfied
  """



def log_issue(message: str, logfile="logs/issues.log"):
  """
  Writes error messages without crashing the program
  """
