def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours}시간 {minutes}분 {secs}초"

print(convert_seconds(12345))