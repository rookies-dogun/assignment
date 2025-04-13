def convert_seconds(seconds):
    return f"{seconds // 3600}시간 {(seconds % 3600) // 60}분 {seconds % 60}초"

print(convert_seconds(12345))