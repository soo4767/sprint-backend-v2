import unittest
import os
from pathlib import Path


def sys_path_init():
    import sys
    # For tests/main.py Path
    path = Path(os.path.realpath(__file__)).parent.parent.parent.absolute()
    sys.path.append(str(path))
    # For test.sh Path
    path = Path(os.path.realpath(__file__)).parent.parent.absolute()
    sys.path.append(str(path))


def db_init():
    print('============ DB Initialize Start    ============')
    from sprint.board import model as board_model
    from sprint.category import model as category_model
    from sprint.comment import model as comment_model
    from sprint.team import model as team_model
    from sprint.user import model as user_model
    from database import engine
    models = [
        board_model,
        category_model,
        comment_model,
        user_model,
        team_model,
    ]
    for model in models:
        model.Base.metadata.create_all(engine)
    print('============ DB Initialize Complete ============')
    print()


def print_errors(elements):
    for element in elements:
        print(element[0])  # Error class.function_name
        print(element[1])  # Error Trace Back
        print()


def print_progress_line(first, second, third):
    print(f'============ {first:5s} {second:7s} {third:8s} ============')


def run_test_by_folder_name(folder_name: str, test_name: str, module_strings):
    print_progress_line(test_name, 'Test', 'Start')

    testSuite = unittest.TestSuite()

    module_strings = [folder_name + '.' + model_str for model_str in module_strings]
    [__import__(model_str) for model_str in module_strings]
    suites = [unittest.TestLoader().loadTestsFromName(model_str) for model_str in module_strings]
    [testSuite.addTest(suite) for suite in suites]

    result = unittest.TestResult()
    testSuite.run(result)

    print_progress_line(test_name, 'Result', 'Count')
    print(result)

    if len(result.errors) != 0:
        print_progress_line(test_name, 'Error', 'List')
        print_errors(result.errors)

    if len(result.failures) != 0:
        print_progress_line(test_name, 'Failure', 'List')
        print_errors(result.failures)

    print()


def service_test():
    # Crud Test module 이름들을 생성 순서에 맞게 작성합니다
    module_strings = ['auth',
                      ]

    run_test_by_folder_name('service', 'CRUD', module_strings)


def api_test():
    # API Test module 이름들을 생성 순서에 맞게 작성합니다
    module_strings = ['auth',
                      ]
    run_test_by_folder_name('api', 'API', module_strings)


def init_dummy_data():
    sys_path_init()

    db_init()

    service_test()

    api_test()


if __name__ == "__main__":
    init_dummy_data()
