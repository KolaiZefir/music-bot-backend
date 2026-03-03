from database import Database

db = Database()
tracks = db.get_user_tracks(1038348220)  # ваш ID

print("="*50)
print(f"Найдено треков: {len(tracks)}")
print("="*50)

for i, track in enumerate(tracks, 1):
    print(f"{i}. {track.get('title')} - {track.get('artist')}")
    print(f"   Файл: {track.get('file_name')}")
    print("-"*30)