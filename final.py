import instaloader

def download_latest_posts(username, count, save_directory):
    L = instaloader.Instaloader()
    
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()
        
        for post in posts:
            if count == 0:
                break
            
            L.download_post(post, target=save_directory)
            count -= 1

        print(f"Success: {count} latest Instagram posts saved at {save_directory}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    instagram_username = input("Enter the Instagram username: ")
    post_count = int(input("How many posts? : "))
    save_directory = "C:\Users\jun\Desktop\before"

    download_latest_posts(instagram_username, post_count, save_directory)

import os
import shutil

def filter_and_save_jpg_files(source_folder, destination_folder):
    try:
        # 폴더가 없으면 생성
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # 폴더 안의 파일들을 검사하여 jpg 파일만 복사
        for filename in os.listdir(source_folder):
            full_file_path = os.path.join(source_folder, filename)
            if os.path.isfile(full_file_path) and filename.lower().endswith('.jpg'):
                # jpg 파일을 목적 폴더로 복사
                shutil.copy(full_file_path, os.path.join(destination_folder, filename))
        
        print("jpg 파일만 저장되었습니다.")
    except Exception as e:
        print("오류 발생:", e)

# 사용 예시
source_folder = "C:\\Users\\jun\\Desktop\\before"  # 원본 폴더 경로를 적절하게 변경해주세요
destination_folder = f"C:\\Users\\jun\\Desktop\\{instagram_username}"  

filter_and_save_jpg_files(source_folder, destination_folder)



def delete_folder(folder_path):
    try:
        # 폴더가 존재하는지 확인
        if os.path.exists(folder_path):
            # 폴더와 그 안의 모든 파일, 하위 폴더 삭제
            shutil.rmtree(folder_path)
            print(f"{folder_path} 폴더가 삭제되었습니다.")
        else:
            print(f"{folder_path} 폴더가 존재하지 않습니다.")
    except Exception as e:
        print("오류 발생:", e)

# 사용 예시
folder_to_delete = "C:\\Users\\jun\\Desktop\\before"  

delete_folder(folder_to_delete)


