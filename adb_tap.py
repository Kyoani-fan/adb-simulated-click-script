import time
import subprocess
import datetime

def run_command(command):
    """执行系统命令并返回结果"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

# 检查设备连接
command = 'adb devices'
return_code, stdout, stderr = run_command(command)
print("Connected devices:")
print(stdout)
if stderr:
    print("Error:", stderr)

# 设置目标执行时间（精确到毫秒）
target_time = datetime.datetime(2025, 10, 20, 21, 0, 0, 0)  # 格式: 年, 月, 日, 时, 分, 秒, 微秒
target_timestamp = target_time.timestamp()

print(f"等待执行时间: {target_time}")

# 高精度等待至目标时间
while True:
    now = time.time()
    delta = target_timestamp - now

    if delta <= 0:
        break

    # 分阶段 sleep，越接近目标时间，sleep 越短，提高精度
    if delta < 0.1:  # 100ms 内
        time.sleep(delta / 2)
    elif delta < 1:  # 1s 内
        time.sleep(0.01)
    else:
        time.sleep(0.1)

print("开始执行操作...")


# 定义滑动操作,(x1,y1)滑动至(x2,y2),持续时间duration(ms)
def swipe(x1, y1, x2, y2, duration):
    command_swipe = f'adb shell input swipe {x1} {y1} {x2} {y2} {duration}'
    return_code, stdout, stderr = run_command(command_swipe)
    if return_code != 0:
        print("滑动失败:", stderr)
    else:
        print("滑动执行完成")
        # 获取完成确切时间并打印，用于调试
        completion_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # 精确到毫秒
        print(f"执行滑动完成 @ {completion_time}")

# 定义点击操作,点击坐标(x,y)
def tap(x,y):
    command_tap = f'adb shell input tap {x} {y}'
    print(command_tap)
    return_code, stdout, stderr = run_command(command_tap)
    if return_code != 0:
        print(f"点击 ({x},{y}) 失败:", stderr)
    else:
        print(f"点击 ({x},{y}) 完成")
        completion_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # 精确到毫秒
        print(f"执行点击({x},{y}) @ {completion_time}")
    
# 等待命令:此处实例为 10 毫秒
# time.sleep(0.1)

# ===在此处添加操作序列===
completion_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(f"开始执行时间 @ {completion_time}")
tap(500,2000)
time.sleep(0.3)
tap(600,3000)
time.sleep(0.3)
swipe(100,1000,200,2000,300)

# ===操作序列结束===


print("所有操作已完成。")
# 输出完成时间
completion_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # 精确到毫秒
print(f"执行完成 @ {completion_time}")