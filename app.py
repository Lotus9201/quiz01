import os

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
}

# 取得當前Downloads資料夾路徑
downloads_folder = os.path.join(os.getcwd(), "Downloads")

# ifDownloads 資料夾不存在，就創建它並放入測試檔案
if not os.path.exists(downloads_folder):
    os.makedirs(downloads_folder)
    
    test_files = [
        "Scripting課程大綱.pdf", "期中報告草稿.docx", "cat_meme.jpg",
        "lofi_music.mp3", "screenshot_2025.png", "final_project.zip"
    ]
    # 使用 os.path.join() 來確保檔案會創建於 Downloads 資料夾中
    for file_name in test_files:
        file_path = os.path.join(downloads_folder, file_name)
        # 創建空檔案
        with open(file_path, 'w'):
            pass  # 只創建空檔案，不需要寫入內容

# 遍歷資料夾中的檔案並分類
for filename in os.listdir(downloads_folder):
    path = os.path.join(downloads_folder, filename)
    ext = os.path.splitext(filename)[1].lower()

    if ext and filename != "app.py":
        # 判斷檔案類型
        folder = next((folder_name for folder_name, exts in file_types.items() if ext in exts), "Others")
        # 確保目標資料夾存在，若無則創建
        target_path = os.path.join(downloads_folder, folder)
        os.makedirs(target_path, exist_ok=True)
        # 移動檔案
        os.rename(path, os.path.join(target_path, filename))

print("檔案分類完成！")
