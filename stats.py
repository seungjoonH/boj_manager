import subprocess
import time
import sys
import psutil
from threading import Thread
import argparse
import os

def create_dir():
  current_dir = os.path.dirname(os.path.abspath(__file__))
  if current_dir not in sys.path:
    sys.path.append(current_dir)

def parse_script_path(input_path: str):
  try:
    parts = input_path.split("/")
    if len(parts) != 2:
      raise ValueError("경로는 '문제번호/풀이번호' 형식이어야 합니다 (예: 1002/2).")

    problem_number = int(parts[0])
    solve_number = parts[1]

    if not solve_number.isdigit():
      raise ValueError("풀이 번호는 숫자여야 합니다.")

    unit_digit = "0"
    if problem_number >= 10000:
      unit_digit = str(problem_number // 10000)
    thousand_digit = f"{(problem_number // 1000) % 100:02d}"

    script_path = f"./{unit_digit}/{thousand_digit}/{problem_number}/{solve_number}.py"

    if not os.path.isfile(script_path):
      raise FileNotFoundError(f"파일이 존재하지 않습니다: {script_path}")

    return script_path

  except (ValueError, FileNotFoundError) as e:
    print(f"Error: {e}")
    sys.exit(1)

def monitor_memory(process, interval, memory_list):
  try:
    while process.is_running():
      memory_list.append(process.memory_info().rss)
      time.sleep(interval)
  except psutil.NoSuchProcess:
    pass

def measure_execution_time_and_memory(script_path, delay_on_hash):
  try:
    print()
    print("=" * 30)
    print("INPUT(Ctrl+D 로 종료):")
    user_input = sys.stdin.read()

    process = subprocess.Popen(
      ["python3", script_path],
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      text=True
    )
    psutil_process = psutil.Process(process.pid)

    memory_usage = []
    monitor_thread = Thread(target=monitor_memory, args=(psutil_process, 0.1, memory_usage))
    monitor_thread.start()

    start_time = time.time()
    stdout, stderr = process.communicate(input=user_input)
    end_time = time.time()

    monitor_thread.join()

    print()
    print("=" * 30)

    if stdout:
      print("OUTPUT:")
      for line in stdout.splitlines():
        for char in line:
          print(char, end="")
          if char == "@":
            time.sleep(delay_on_hash / 1000)
        print()

    if stderr:
      print("ERROR:")
      for line in stderr.splitlines():
        for char in line:
          print(char, end="")
          if char == "#":
            time.sleep(delay_on_hash / 1000)
        print()

    print("=" * 30)
    duration = end_time - start_time
    print(f"RUNTIME: {duration:.6f} s")

    if memory_usage:
      peak_memory = max(memory_usage)
      mem_size_kb = peak_memory / 1024
      mem_size_mb = mem_size_kb / 1024
      print(f"PEAK MEMORY USAGE: {mem_size_mb:.2f} MB ({mem_size_kb:.2f} KB)")
    else:
      print("PEAK MEMORY USAGE: 측정 불가")

    print()

  except FileNotFoundError:
    print(f"Error: 파일 '{script_path}' 이 존재하지 않습니다.")
  except Exception as e:
    print(f"Error: {e}")

def main():
  parser = argparse.ArgumentParser(description="Run a script and measure its execution time and memory usage.")
  parser.add_argument("input_path", type=str, help="Path to the script in '문제번호/풀이번호' format (e.g., 1002/2)")
  parser.add_argument("-i", "--interval", type=int, default=100, help="Delay in milliseconds when '#' is printed (default: 100ms)")

  args = parser.parse_args()

  script_path = parse_script_path(args.input_path)
  measure_execution_time_and_memory(script_path, args.interval)

if __name__ == "__main__":
  create_dir()
  main()