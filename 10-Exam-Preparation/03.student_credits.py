def students_credits(*courses_data):
    results = {}
    diploma = ''
    total_credits = 0
    diploma_credits = 240
    for i in range(len(courses_data)):
        current_credits = 0
        current_course = courses_data[i].split('-')
        course_name, received_credits, max_points, deyan_s_points = current_course[0], \
            int(current_course[1]), int(current_course[2]), int(current_course[3])
        current_credits = (deyan_s_points / max_points) * received_credits

        if course_name not in results.keys():
            results[course_name] = 0
        results[course_name] = current_credits

        total_credits += current_credits

    if total_credits >= diploma_credits:
        diploma = f'Diyan gets a diploma with {total_credits:.1f} credits.\n'
    else:
        diploma = f'Diyan needs {(diploma_credits - total_credits):.1f} credits more for a diploma.\n'

    for key, value in sorted(results.items(), key=  lambda x: -x[1]):
        diploma += f'{key} - {value:.1f}\n'

    return diploma

# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )
# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
