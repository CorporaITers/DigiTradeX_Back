import re

ocr_text = """
TOTAL 24,096.00 USD
"""

match = re.search(r"TOTAL\s+([\d]{1,3}(?:,\d{3})*(?:\.\d{2})?)", ocr_text)
if match:
    print("抽出結果:", match.group(1))  # → 24,096.00 となるはず
else:
    print("マッチしませんでした")
