from yt_dlp import YoutubeDL
import json
import os
from datetime import datetime
import time
from youtube import get_video_urls, get_youtube_video_info
import random

def get_playlist_videos(channel_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            channel_info = ydl.extract_info(channel_url, download=False)
            playlists = channel_info.get('entries', [])
            
            playlist_data = []
            for playlist in playlists:
                # 요청 간격 추가 (1-3초)
                time.sleep(random.uniform(1, 3))
                
                playlist_url = f"https://www.youtube.com/playlist?list={playlist['id']}"
                video_urls = get_video_urls(playlist_url)
                
                playlist_data.append({
                    'id': playlist['id'],
                    'title': playlist.get('title', 'Unknown Playlist'),
                    'description': playlist.get('description', ''),
                    'video_count': len(video_urls),
                    'video_urls': video_urls
                })
            
            return playlist_data
        except Exception as e:
            print(f"플레이리스트 정보 추출 중 오류 발생: {str(e)}")
            return []

def get_video_info_with_retry(video_url, max_retries=3, delay=5):
    for attempt in range(max_retries):
        try:
            # 요청 간격 추가 (2-4초)
            time.sleep(random.uniform(2, 4))
            
            video_info = get_youtube_video_info(video_url)
            return video_info
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = delay * (attempt + 1)  # 점진적으로 대기 시간 증가
                print(f"시도 {attempt + 1}/{max_retries} 실패. {wait_time}초 후 재시도...")
                time.sleep(wait_time)
            else:
                raise e

def save_playlist_data(playlist_data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_dir = f'captions/{timestamp}'
    
    for playlist in playlist_data:
        # 플레이리스트 제목에서 특수문자 제거
        safe_playlist_title = "".join(c for c in playlist['title'] if c.isalnum() or c in (' ', '-', '_')).rstrip()
        
        # 플레이리스트 디렉토리 생성
        playlist_dir = f"{base_dir}/{safe_playlist_title}"
        if not os.path.exists(playlist_dir):
            os.makedirs(playlist_dir)
        
        # 플레이리스트 메타데이터 저장
        playlist_meta = {
            'id': playlist['id'],
            'title': playlist['title'],  # 원본 제목은 메타데이터에 저장
            'description': playlist['description'],
            'video_count': playlist['video_count'],
            'created_at': timestamp
        }
        
        with open(f'{playlist_dir}/playlist_meta.json', 'w', encoding='utf-8') as f:
            json.dump(playlist_meta, f, ensure_ascii=False, indent=2)
        
        # 각 비디오의 자막과 메타데이터 저장
        for video_url in playlist['video_urls']:
            try:
                print(f"자막 추출 중: {playlist['title']} - {video_url}")
                
                # 비디오 정보와 자막 추출 (재시도 로직 포함)
                video_info = get_video_info_with_retry(video_url)
                
                # 파일명에서 사용할 수 없는 문자 제거
                safe_title = "".join(c for c in video_info['title'] if c.isalnum() or c in (' ', '-', '_')).rstrip()
                
                # 비디오 디렉토리 생성
                video_dir = f"{playlist_dir}/{safe_title}"
                if not os.path.exists(video_dir):
                    os.makedirs(video_dir)
                
                # 메타데이터 저장
                with open(f'{video_dir}/meta.json', 'w', encoding='utf-8') as f:
                    json.dump(video_info, f, ensure_ascii=False, indent=2)
                
                # 자막 저장
                with open(f'{video_dir}/caption.txt', 'w', encoding='utf-8') as f:
                    f.write(video_info['caption'])
                
                print(f"저장 완료: {playlist['title']}/{safe_title}")
                
                # 비디오 처리 후 추가 대기 (3-5초)
                time.sleep(random.uniform(3, 5))
                
            except Exception as e:
                print(f"비디오 처리 중 오류 발생: {video_url} - {str(e)}")
                # 오류 발생 시 더 긴 대기 시간 (10-15초)
                time.sleep(random.uniform(10, 15))

def main():
    channel_url = "https://www.youtube.com/@IBMTechnology/playlists"
    
    # 결과를 저장할 디렉토리 생성
    if not os.path.exists('captions'):
        os.makedirs('captions')
    
    # 플레이리스트의 모든 비디오 정보 가져오기
    playlist_data = get_playlist_videos(channel_url)
    
    # 플레이리스트 데이터 저장
    if playlist_data:
        save_playlist_data(playlist_data)

if __name__ == "__main__":
    main() 