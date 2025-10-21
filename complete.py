# Danh sách ban đầu
tasks = [
    {"name": "Học bài Git", "completed": False},
    {"name": "Làm bài tập", "completed": False},
    {"name": "Dọn phòng", "completed": False}
]

def list_tasks():
    for idx, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{idx + 1}. {status} {task['name']}")

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"✅ Đã đánh dấu hoàn thành: {tasks[task_index]['name']}")
    else:
        print("❌ Chỉ số công việc không hợp lệ.")

# Chạy thử
print("📋 Danh sách trước:")
list_tasks()

print("\n✅ Đánh dấu công việc số 2 là hoàn thành:")
complete_task(1)  # số 2 = index 1

print("\n📋 Danh sách sau:")
list_tasks()
