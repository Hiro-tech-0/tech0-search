# ── 演習 5-A 解答欄 ──
# insert_page を使うための import 文を書いてみよう

# ここに書く ↓
# from _______ import _______
from database import init_db, insert_page, get_all_pages
init_db()

test_page = {
    "url": "https://example.com",
    "title": "テスト",
    "description": "",
    "full_text": "",
    "word_count": 0,
    "crawled_at": "2024-01-01T00:00:00",
}
insert_page(test_page)
print("✅ insert_page が使えた！")
print(f"DBの件数：{len(get_all_pages())} 件")


# ── 書けたか確認 ──
try:
    insert_page
    print("✅ insert_page を読み込めています")
except NameError:
    print("→ まだ import できていません。上に import 文を書いてみましょう。")
except ModuleNotFoundError as e:
    print(f"→ {e}")
    print("  （このノートブックの場所には database.py が無いため、これは想定どおりです）")
