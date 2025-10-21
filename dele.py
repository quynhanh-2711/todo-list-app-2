tasks = [
    {"name": "Học bài Git", "completed": False},
    {"name": "Làm bài tập", "completed": True},
    {"name": "Dọn phòng", "completed": False}
]

def list_tasks():
    for idx, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{idx + 1}. {status} {task['name']}")

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"✅ Đã xóa công việc: {removed['name']}")
    else:
        print("❌ Chỉ số công việc không hợp lệ.")

# Thử hiển thị và xóa công việc số 2
print("📋 Danh sách trước khi xóa:")
list_tasks()

print("\n🗑️ Xóa công việc số 2:")
delete_task(1)  # Lưu ý: số 2 tương ứng với index 1

print("\n📋 Danh sách sau khi xóa:")
list_tasks()
