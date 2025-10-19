import json
import os
from pathlib import Path

# Lấy thư mục hiện tại
base_dir = os.path.dirname(os.path.abspath(__file__))

# Đọc file JSON
json_path = os.path.join(base_dir, 'vulnerabilities.json')
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Tổng số entry ban đầu: {len(data)}")

# Lọc những entry mà file tồn tại
cleaned_data = []
removed_count = 0

for entry in data:
    # Chuyển đường dẫn tương đối thành tuyệt đối
    relative_path = entry['path']
    # Loại bỏ "dataset/" ở đầu nếu có
    if relative_path.startswith('dataset/'):
        relative_path = relative_path.replace('dataset/', '', 1)
    
    full_path = os.path.join(base_dir, relative_path)
    
    if os.path.exists(full_path):
        cleaned_data.append(entry)
    else:
        removed_count += 1
        print(f"Xóa: {entry['name']} - File không tồn tại: {full_path}")

print(f"\nĐã xóa {removed_count} entry")
print(f"Còn lại {len(cleaned_data)} entry")

# Lưu file đã clean
with open('vulnerabilities.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, indent=4, ensure_ascii=False)

# Đếm lỗ hổng theo danh mục
category_mapping = {
    'access_control': 'Access Control',
    'arithmetic': 'Arithmetic',
    'denial_of_service': 'Denial of Service',
    'bad_randomness': 'Bad Randomness',
    'front_running': 'Front Running',
    'reentrancy': 'Reentrancy',
    'time_manipulation': 'Time Manipulation',
    'unchecked_low_level_calls': 'Unchecked Low Calls',
    'short_addresses': 'Short Addresses',
    'other': 'Other'
}

# Đếm số lượng file theo danh mục
category_file_count = {}
# Đếm số lượng lỗ hổng theo danh mục
category_vuln_count = {}

for entry in cleaned_data:
    for vuln in entry['vulnerabilities']:
        category = vuln['category']
        display_name = category_mapping.get(category, category)
        
        # Đếm file
        if display_name not in category_file_count:
            category_file_count[display_name] = set()
        category_file_count[display_name].add(entry['name'])
        
        # Đếm lỗ hổng
        if display_name not in category_vuln_count:
            category_vuln_count[display_name] = 0
        category_vuln_count[display_name] += 1

print("\n" + "="*80)
print("THỐNG KÊ LỖ HỔNG THEO DANH MỤC")
print("="*80)
print(f"{'Danh mục':<25} {'Số file':<15} {'Số lỗ hổng':<15}")
print("-"*80)

# Sắp xếp theo thứ tự mong muốn
desired_order = [
    'Access Control',
    'Arithmetic',
    'Denial of Service',
    'Bad Randomness',
    'Front Running',
    'Reentrancy',
    'Time Manipulation',
    'Unchecked Low Calls',
    'Other',
    'Short Addresses'
]

total_files = 0
total_vulns = 0

for category in desired_order:
    if category in category_file_count:
        file_count = len(category_file_count[category])
        vuln_count = category_vuln_count[category]
        total_files += file_count
        total_vulns += vuln_count
        print(f"{category:<25} {file_count:<15} {vuln_count:<15}")

print("-"*80)
print(f"{'TỔNG':<25} {total_files:<15} {total_vulns:<15}")
print("="*80)
