# THỐNG KÊ LỖ HỔNG SMART CONTRACT

## Tổng quan
- **Tổng số file Solidity**: 69 files
- **Tổng số lỗ hổng**: 109 lỗ hổng
- **Đã xóa**: 74 entry không có file tồn tại trong dataset

## Thống kê chi tiết theo danh mục

| STT | Danh mục | Số file | Số lỗ hổng | Tỷ lệ % |
|-----|----------|---------|------------|---------|
| 1 | **Access Control** | 17 | 20 | 18.35% |
| 2 | **Arithmetic** | 14 | 22 | 20.18% |
| 3 | **Denial of Service** | 6 | 7 | 6.42% |
| 4 | **Bad Randomness** | 8 | 31 | 28.44% |
| 5 | **Front Running** | 4 | 7 | 6.42% |
| 6 | **Reentrancy** | 7 | 7 | 6.42% |
| 7 | **Time Manipulation** | 4 | 5 | 4.59% |
| 8 | **Unchecked Low Calls** | 5 | 6 | 5.50% |
| 9 | **Other** | 3 | 3 | 2.75% |
| 10 | **Short Addresses** | 1 | 1 | 0.92% |
| | **TỔNG CỘNG** | **69** | **109** | **100%** |

## Phân tích

### Top 3 lỗ hổng phổ biến nhất:

1. **Bad Randomness (28.44%)**: 31 lỗ hổng trong 8 files
   - Lỗ hổng liên quan đến việc tạo số ngẫu nhiên không an toàn
   - Chiếm tỷ trọng cao nhất trong dataset

2. **Arithmetic (20.18%)**: 22 lỗ hổng trong 14 files
   - Lỗ hổng về integer overflow/underflow
   - Lỗ hổng phổ biến thứ 2

3. **Access Control (18.35%)**: 20 lỗ hổng trong 17 files
   - Lỗ hổng về kiểm soát truy cập và phân quyền
   - Lỗ hổng phổ biến thứ 3

### Lỗ hổng ít gặp nhất:

- **Short Addresses (0.92%)**: 1 lỗ hổng duy nhất
- **Other (2.75%)**: 3 lỗ hổng không thuộc danh mục chính

## Cấu trúc thư mục

```
dataset/
├── access_control/          # 17 files
├── arithmetic/              # 14 files
├── bad_randomness/          # 8 files
├── denial_of_service/       # 6 files
├── front_running/           # 4 files
├── other/                   # 3 files
├── reentrancy/              # 7 files
├── short_addresses/         # 1 file
├── time_manipulation/       # 4 files
└── unchecked_low_level_calls/ # 5 files
```

## Ghi chú

- File `vulnerabilities.json` đã được làm sạch và chỉ chứa các entry có file `.sol` tồn tại
- Mỗi file có thể chứa nhiều lỗ hổng trên các dòng code khác nhau
- Dataset được curated từ SmartBugs project
