class Robot:
    def __init__(self, speed, id):
        self.speed = speed  # 机器人的插秧速度，单位：米/小时
        self.id = id  # 机器人ID


def calculate_total_time(field_length, field_width, robot_speeds):
    """
    计算所有机器人完成任务所需的总时间。

    参数:
        field_length (float): 田地的长度（米）。
        field_width (float): 田地的宽度（米）。
        robot_speeds (list): 一个包含了每个机器人的插秧速度的列表，单位为米/小时。

    返回值:
        float: 所有机器人完成任务的总时间。
    """
    total_area = field_length * field_width  # 田地的总面积
    total_speed = sum(robot_speeds)  # 所有机器人的总插秧速度
    total_time = total_area / total_speed  # 总时间是总面积除以总速度

    return total_time


def calculate_work_distribution(field_length, field_width, robot_speeds, total_time):
    """
    根据每个机器人负责的面积计算每个机器人负责的行数和起始位置。

    参数:
        field_length (float): 田地的长度（米）。
        field_width (float): 田地的宽度（米）。
        robot_speeds (list): 一个包含了每个机器人的插秧速度的列表，单位为米/小时。
        total_time (float): 所有机器人完成任务的总时间。

    返回值:
        list: 每个机器人应负责的行数列表和起始位置列表。
    """
    total_area = field_length * field_width  # 田地的总面积
    area_per_robot = [speed * total_time for speed in robot_speeds]  # 每个机器人应负责的面积
    rows_per_robot = [area / field_length for area in area_per_robot]  # 每个机器人应负责的行数

    # 确保总行数一致
    total_rows = sum(rows_per_robot)
    adjustment_factor = num_rows / total_rows
    rows_per_robot = [r * adjustment_factor for r in rows_per_robot]

    start_positions = []
    start_row = 0  # 初始化起始行
    for rows in rows_per_robot:
        start_positions.append((start_row, 0))
        start_row += rows

    return rows_per_robot, start_positions


def insert_rice(robot, field_length, row_height, start_row, start_x, rows_to_cover, direction):
    """
    模拟给定机器人以蛇形路径插秧的过程。

    参数:
        robot (Robot): 要执行插秧的机器人对象。
        field_length (float): 田地的长度（米）。
        row_height (float): 每行的高度（米）。
        start_row (int): 插秧的起始行。
        start_x (float): 插秧的起始列。
        rows_to_cover (int): 需要插秧的行数。
        direction (int): 初始方向，1表示从左到右，-1表示从右到左。

    返回值:
        float: 完成插秧所需的总时间。
    """
    total_time = 0
    x, y = start_x, start_row * row_height  # 机器人起始位置

    for _ in range(int(rows_to_cover)):
        # 计算覆盖一行所需的时间
        time_to_cover_row = field_length / robot.speed
        total_time += time_to_cover_row
        x += field_length * direction

        # 检查机器人是否到达边界
        if x >= field_length or x < 0:
            x = max(0, min(field_length, x))  # 保持在边界内
            y += row_height  # 移动到下一行
            direction *= -1  # 改变方向

    return total_time


# 输入参数
field_length = 10.0  # 田地长度（米）
field_width = 10.0  # 田地宽度（米）
num_rows = 10  # 行数
row_height = field_width / num_rows  # 计算每行的高度

# 机器人速度
robot_speeds = [2, 2.5, 4]

# 创建机器人对象
robots = [Robot(speed, i + 1) for i, speed in enumerate(robot_speeds)]

# 计算总时间
total_time = calculate_total_time(field_length, field_width, robot_speeds)

# 计算每个机器人需要覆盖的行数和起始位置
rows_per_robot, start_positions = calculate_work_distribution(field_length, field_width, robot_speeds, total_time)

# 确定每个机器人从哪个位置开始插秧，并随机初始方向
for i, (rows, start_pos) in enumerate(zip(rows_per_robot, start_positions)):
    robot = robots[i]
    start_row, start_x = start_pos
    direction = 1 if i % 2 == 0 else -1  # 初始方向交替选择
    time = insert_rice(robot, field_length, row_height, start_row, start_x, rows, direction)
    print(f"机器人 {robot.id} 从第 {start_row} 行第 {start_x:.2f} 米开始插秧，覆盖 {rows:.2f} 行，需要 {time:.2f} 小时")

print(f"\n所有机器人同时完成任务，总时间：{total_time:.2f} 小时")
