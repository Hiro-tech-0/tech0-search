try:
    from database import init_db, get_all_pages, insert_page, log_search
    from ranking  import get_engine, rebuild_index
    from crawler  import crawl_url

    print("✅ 3つのモジュールを読み込めました")
    print()
    print("database.py から：")
    print(f"   init_db       → {init_db}")
    print(f"   get_all_pages → {get_all_pages}")
    print(f"   insert_page   → {insert_page}")
    print("ranking.py から：")
    print(f"   get_engine    → {get_engine}")
    print(f"   rebuild_index → {rebuild_index}")
    print("crawler.py から：")
    print(f"   crawl_url     → {crawl_url}")
    print()
    print("→ 統合の準備完了！")

except ModuleNotFoundError as e:
    print(f"❌ 読み込めませんでした： {e}")
    print()
    print("── これは想定どおりの結果です ──")
    print("import は「同じフォルダにあるファイル」を探しにいきます。")
    print("いまこのノートブックがある場所には、まだ3つの .py がありません。")
    print()
    print("試したい人は、次のどちらかで実行してみてください：")
    print("  ① 自分で作った tech0-search-v1.0/ フォルダにこのコードをコピーする")
    print("  ② answers/w4/ フォルダにコピーする（完成コードが置いてあります）")