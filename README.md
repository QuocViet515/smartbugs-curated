# SmartBugs Curated - Dataset lỗ hổng Smart Contract

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Solidity](https://img.shields.io/badge/Solidity-0.4.x-orange.svg)](https://docs.soliditylang.org/)

Đây là dataset được curated từ [SmartBugs Project](https://github.com/smartbugs/smartbugs), bao gồm các smart contract Solidity có chứa các lỗ hổng bảo mật đã được xác định và ghi chú chi tiết.

## 📊 Tổng quan Dataset

- **Tổng số file Solidity**: 69 contracts
- **Tổng số lỗ hổng**: 124 vulnerabilities
- **Phiên bản Solidity**: 0.4.x
- **Nguồn**: SmartBugs, SWC Registry, Etherscan, GitHub

## 📂 Cấu trúc thư mục

```
dataset/
├── access_control/              # 17 files - Lỗ hổng kiểm soát truy cập
├── arithmetic/                  # 14 files - Lỗ hổng số học (overflow/underflow)
├── bad_randomness/              # 8 files  - Số ngẫu nhiên không an toàn
├── denial_of_service/           # 6 files  - Tấn công từ chối dịch vụ
├── front_running/               # 4 files  - Tấn công front-running
├── reentrancy/                  # 7 files  - Lỗ hổng reentrancy
├── time_manipulation/           # 4 files  - Thao túng timestamp
├── unchecked_low_level_calls/   # 5 files  - Low-level call không kiểm tra
├── other/                       # 3 files  - Các lỗ hổng khác
└── short_addresses/             # 1 file   - Tấn công short address
```

## 🔍 Phân loại lỗ hổng

| Danh mục | Số file | Số lỗ hổng | Tỷ lệ % | Mô tả |
|----------|---------|------------|---------|-------|
| **Bad Randomness** | 8 | 34 | 27.42% | Sử dụng blockhash, timestamp để tạo số ngẫu nhiên |
| **Access Control** | 17 | 23 | 18.55% | Thiếu kiểm soát quyền truy cập, constructor sai tên |
| **Arithmetic** | 14 | 22 | 17.74% | Integer overflow/underflow |
| **Denial of Service** | 6 | 14 | 11.29% | Gas limit, vòng lặp không giới hạn |
| **Front Running** | 4 | 7 | 5.65% | Transaction ordering dependence |
| **Reentrancy** | 7 | 7 | 5.65% | Gọi lại hàm trước khi cập nhật state |
| **Unchecked Low Calls** | 5 | 6 | 4.84% | Không kiểm tra return value của call() |
| **Time Manipulation** | 4 | 5 | 4.03% | Phụ thuộc vào block.timestamp |
| **Other** | 3 | 5 | 4.03% | Các lỗ hổng khác |
| **Short Address** | 1 | 1 | 0.81% | Tấn công short address ERC20 |

## 📝 Định dạng dữ liệu

Mỗi lỗ hổng trong `vulnerabilities.json` được mô tả theo format:

```json
{
    "name": "tên_file.sol",
    "path": "đường_dẫn/tới/file.sol",
    "pragma": "phiên_bản_solidity",
    "source": "nguồn_gốc_file",
    "vulnerabilities": [
        {
            "lines": [số_dòng_chứa_lỗ_hổng],
            "category": "loại_lỗ_hổng"
        }
    ]
}
```

## 🎯 Mục đích sử dụng

Dataset này phù hợp cho:

- ✅ Huấn luyện mô hình machine learning phát hiện lỗ hổng
- ✅ Nghiên cứu về bảo mật smart contract
- ✅ Phát triển công cụ phân tích tĩnh/động
- ✅ Học tập và giảng dạy về lỗ hổng blockchain
- ✅ Benchmark cho các công cụ audit

## 🔥 Các lỗ hổng nổi bật

### 1. Bad Randomness (27.42%)
- Sử dụng `blockhash`, `block.timestamp`, `block.number` để tạo số ngẫu nhiên
- Miner có thể thao túng các giá trị này
- **Ví dụ**: lottery.sol, smart_billions.sol

### 2. Access Control (18.55%)
- Constructor có tên sai (Solidity <0.4.22)
- Thiếu modifier kiểm tra quyền
- Sử dụng `tx.origin` thay vì `msg.sender`
- **Ví dụ**: parity_wallet_bug_1.sol, rubixi.sol

### 3. Arithmetic Overflow/Underflow (17.74%)
- Không kiểm tra overflow khi cộng/nhân
- Không kiểm tra underflow khi trừ
- **Ví dụ**: BECToken.sol (lỗ hổng nổi tiếng), integer_overflow_mul.sol

### 4. Denial of Service (11.29%)
- Gas limit vượt quá giới hạn block
- Vòng lặp không kiểm soát được
- **Ví dụ**: Các contract với vòng lặp động không giới hạn


## 📚 Nguồn tham khảo

- [SmartBugs Framework](https://github.com/smartbugs/smartbugs)
- [SWC Registry](https://swcregistry.io/)
- [Ethereum Smart Contract Security Best Practices](https://consensys.github.io/smart-contract-best-practices/)
- [Not So Smart Contracts](https://github.com/crytic/not-so-smart-contracts)
- [Capture The Ether](https://capturetheether.com/)

## 📄 File hỗ trợ

- `vulnerabilities.json` - Metadata đầy đủ của tất cả lỗ hổng
- `clean_vulnerabilities.py` - Script làm sạch và xác thực dữ liệu
- `THONG_KE_LO_HONG.md` - Thống kê chi tiết bằng tiếng Việt

## ⚠️ Lưu ý

- ⚠️ Các contract trong dataset này chứa lỗ hổng bảo mật thực tế
- ⚠️ **KHÔNG triển khai** các contract này lên mainnet
- ⚠️ Chỉ sử dụng cho mục đích nghiên cứu và học tập
- ⚠️ Một số contract đã từng hoạt động trên Ethereum mainnet và gây thiệt hại thực tế


## 📜 License

Dataset này được chia sẻ cho mục đích nghiên cứu và giáo dục. Các contract riêng lẻ có thể có license từ nguồn gốc của chúng.

---

**⭐ Nếu thấy hữu ích, hãy star repository này!**
