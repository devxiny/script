import os
import requests


def download_files(file_path, save_directory, base_url):
    # 确保保存目录存在
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # 读取文件地址
    with open(file_path, "r") as file:
        urls = file.readlines()

    # 下载每个文件
    for url in urls:
        url = url.strip()  # 去除行尾的换行符
        if url:  # 确保url不为空
            file_name = url.split("/")[-1]  # 获取文件名
            full_url = base_url + url  # 构建完整的下载链接
            save_path = os.path.join(save_directory, file_name)  # 构建保存路径

            # 下载文件
            response = requests.get(full_url)
            if response.status_code == 200:
                with open(save_path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {file_name} to {save_path}")
            else:
                print(
                    f"Failed to download {file_name}. Status code: {response.status_code}"
                )


# 示例调用
file_path = r"C:\Users\devxiny\Desktop\身份证地址.txt"  # 包含文件地址的txt文件路径
save_directory = r"C:\Users\devxiny\Downloads\id_card"  # 保存目录
base_url = "http://cloud.xxx.net:8083/"  # 基础URL

download_files(file_path, save_directory, base_url)
