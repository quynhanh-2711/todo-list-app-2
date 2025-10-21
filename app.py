# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
    
# Hàm liệt kê tất cả công việc trong danh sách
def list_tasks():
    print("\nDanh sách công việc hiện tại:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Điểm bắt đầu của chương trình
if __name__ == "__main__":
    print("Chào mừng bạn đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

#Gọi hàm liệt kê các công việc
    list_tasks()  # Hiển thị danh sách công việc