import json
import os


def compare_json_files():
    results_dir = 'results'
    demo_json_path = os.path.join(results_dir, 'demo.json')
    test_json_path = os.path.join(results_dir, 'test.json')
    
    if not os.path.exists(demo_json_path):
        print(f"Ошибка: Файл {demo_json_path} не найден")
        return False
    
    if not os.path.exists(test_json_path):
        print(f"Ошибка: Файл {test_json_path} не найден")
        return False
    
    with open(demo_json_path, 'r') as f:
        demo_data = json.load(f)
    
    with open(test_json_path, 'r') as f:
        test_data = json.load(f)
    
    print("Сравнение JSON файлов...")
    print(f"Файл 1: {demo_json_path}")
    print(f"Файл 2: {test_json_path}")
    print()
    
    demo_keys = set(demo_data.keys())
    test_keys = set(test_data.keys())
    
    if demo_keys != test_keys:
        print("ОШИБКА: Различия в структуре JSON")
        print(f"Ключи в demo.json: {demo_keys}")
        print(f"Ключи в test.json: {test_keys}")
        return False
    else:
        print("Структура JSON совпадает")
    
    differences = []
    
    for key in demo_keys:
        demo_value = demo_data[key]
        test_value = test_data[key]
        
        if key == 'uv':
            if len(demo_value) != len(test_value):
                differences.append(f"Количество точек в uv: demo={len(demo_value)}, test={len(test_value)}")
            else:
                for i, (demo_point, test_point) in enumerate(zip(demo_value, test_value)):
                    if abs(demo_point[0] - test_point[0]) > 1e-6 or abs(demo_point[1] - test_point[1]) > 1e-6:
                        differences.append(
                            f"Точка {i}: demo=[{demo_point[0]}, {demo_point[1]}], "
                            f"test=[{test_point[0]}, {test_point[1]}]"
                        )
        else:
            if abs(demo_value - test_value) > 1e-6:
                differences.append(f"{key}: demo={demo_value}, test={test_value}")
    
    if differences:
        print("ОШИБКИ НАЙДЕНЫ:")
        for diff in differences:
            print(f"  - {diff}")
        return False
    else:
        print("Ошибок не найдено")
        print("JSON файлы полностью совпадают")
        return True


if __name__ == '__main__':
    success = compare_json_files()
    exit(0 if success else 1)
