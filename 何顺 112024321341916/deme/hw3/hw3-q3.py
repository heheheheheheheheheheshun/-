#借助大模型参考
def min_rooms(intervals):
    # 将课程按开始时间排序
    intervals.sort()

    # 使用最小堆来跟踪教室的最晚结束时间
    import heapq
    heap = []

    for start, end in intervals:
        # 如果最早结束的教室可以用于当前课程
        if heap and heap[0] <= start:
            heapq.heappop(heap)  # 复用该教室
        heapq.heappush(heap, end)  # 更新教室的结束时间

    return len(heap)


def assign_rooms(intervals):
    # 为每个课程添加索引，方便追踪
    indexed_intervals = [(idx, start, end) for idx, (start, end) in enumerate(intervals)]

    # 按开始时间排序
    indexed_intervals.sort(key=lambda x: x[1])

    # 使用优先队列（最小堆）存储教室的结束时间和教室编号
    import heapq
    heap = []
    room_assignments = {}
    next_room = 0

    for idx, start, end in indexed_intervals:
        # 检查是否有教室可用
        if heap and heap[0][0] <= start:
            _, room = heapq.heappop(heap)
            room_assignments.setdefault(room, []).append((idx, (start, end)))
        else:
            room = next_room
            next_room += 1
            room_assignments.setdefault(room, []).append((idx, (start, end)))

        # 将教室放回堆中
        heapq.heappush(heap, (end, room))

    return room_assignments


# 课程时间数据
courses = [
    (9.0, 12.5),  # 0 (9:00,12:30)
    (11.0, 14.0),  # 1 (11:00,14:00)
    (13.0, 14.5),  # 2 (13:00,14:30)
    (9.0, 10.5),  # 3 (9:00,10:30)
    (9.0, 10.5),  # 4 (9:00,10:30)
    (15.0, 16.5),  # 5 (15:00,16:30)
    (9.0, 10.5),  # 6 (9:00,10:30)
    (13.0, 14.5),  # 7 (13:00,14:30)
    (14.0, 16.5)  # 8 (14:00,16:30)
]

# 计算最少需要的教室数量
min_rooms_needed = min_rooms(courses)
print(f"最少需要 {min_rooms_needed} 间教室")

# 分配教室
assignments = assign_rooms(courses)

# 打印每个教室的课程安排
for room in sorted(assignments.keys()):
    courses_in_room = sorted(assignments[room], key=lambda x: x[1][0])
    print(f"\n教室 {room + 1} 安排的课程:")
    for idx, (start, end) in courses_in_room:
        # 转换时间格式为HH:MM
        start_time = f"{int(start)}:{'00' if start == int(start) else '30'}"
        end_time = f"{int(end)}:{'00' if end == int(end) else '30'}"
        print(f"课程 {idx + 1}: ({start_time}, {end_time})")