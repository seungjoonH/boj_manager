import subprocess
import time
import sys
import psutil
from threading import Thread
import argparse
import os
import termios
import tty
import select

def create_dir():
  current_dir = os.path.dirname(os.path.abspath(__file__))
  if current_dir not in sys.path:
    sys.path.append(current_dir)


def compute_path_parts(problem_number: int):
  unit_digit = "0"
  if problem_number >= 10000:
    unit_digit = str(problem_number // 10000)
  thousand_digit = f"{(problem_number // 1000) % 100:02d}"
  return unit_digit, thousand_digit


def parse_script_path(input_path: str):
  try:
    parts = input_path.split("/")
    if len(parts) != 2:
      raise ValueError("Path must be in 'problem_number/solution_number' format (e.g., 1002/2).")

    problem_number = int(parts[0])
    solve_number = parts[1]

    if not solve_number.isdigit():
      raise ValueError("Solution number must be a digit.")

    unit_digit, thousand_digit = compute_path_parts(problem_number)

    script_path = f"./{unit_digit}/{thousand_digit}/{problem_number}/{solve_number}.py"

    if not os.path.isfile(script_path):
      raise FileNotFoundError(f"Script not found: {script_path}")

    return script_path, problem_number, unit_digit, thousand_digit

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


def read_input_from_file(unit_digit, thousand_digit, problem_number, filename):
  input_path = f"./{unit_digit}/{thousand_digit}/{problem_number}/input/{filename}.txt"
  if not os.path.isfile(input_path):
    print(f"Input file not found: {input_path}")
    sys.exit(1)
  with open(input_path, "r", encoding="utf-8") as f:
    return f.read(), input_path


def write_output_to_file(unit_digit, thousand_digit, problem_number, filename, content):
  output_path = f"./{unit_digit}/{thousand_digit}/{problem_number}/output/{filename}.txt"
  os.makedirs(os.path.dirname(output_path), exist_ok=True)
  with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)
  return output_path


def is_q_pressed():
  dr, _, _ = select.select([sys.stdin], [], [], 0)
  if dr:
    return sys.stdin.read(1).lower() == 'q'
  return False


def measure_execution_time_and_memory(
  script_path,
  problem_number,
  unit_digit,
  thousand_digit,
  delay_on_hash,
  input_file=None,
  output_file=None,
  timeout_ms=None
):
  try:
    print()
    print("=" * 30)

    if input_file:
      user_input, input_display_path = read_input_from_file(unit_digit, thousand_digit, problem_number, input_file)
      print("INPUT:")
      print(f"input/{input_file}.txt")
    else:
      print("INPUT (Ctrl+D to end):")
      user_input = sys.stdin.read()

    print("=" * 30)

    process = subprocess.Popen(
      ["python3", script_path],
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      text=True
    )
    psutil_process = psutil.Process(process.pid)

    memory_usage = []
    killed_by_timeout = False
    stop_by_keypress = False

    monitor_thread = Thread(target=monitor_memory, args=(psutil_process, 0.1, memory_usage))
    monitor_thread.start()

    def timeout_killer():
      nonlocal killed_by_timeout
      time.sleep(timeout_ms / 1000)
      if process.poll() is None:
        killed_by_timeout = True
        process.terminate()

    if timeout_ms:
      timeout_thread = Thread(target=timeout_killer)
      timeout_thread.start()

    start_time = time.time()

    def live_timer():
      nonlocal stop_by_keypress
      old_settings = termios.tcgetattr(sys.stdin)
      try:
        tty.setcbreak(sys.stdin.fileno())
        while process.poll() is None:
          elapsed = time.time() - start_time
          print(f"\rRUNNING TIME: {elapsed:.1f}s", end="", flush=True)
          if is_q_pressed():
            stop_by_keypress = True
            process.terminate()
            break
          time.sleep(0.1)
      finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    timer_thread = Thread(target=live_timer)
    timer_thread.start()

    try:
      stdout, stderr = process.communicate(input=user_input)
    except Exception:
      process.kill()
      stdout, stderr = process.communicate()

    end_time = time.time()

    if timeout_ms:
      timeout_thread.join()

    monitor_thread.join()
    timer_thread.join()
    print(f"\r{' ' * 100}\r", end="")

    output_content = stdout

    print("OUTPUT:")
    if killed_by_timeout:
      print("[!] TIMED OUT")
    elif stop_by_keypress:
      print("[!] TERMINATED BY USER (q key)")

    if output_file:
      written_path = write_output_to_file(unit_digit, thousand_digit, problem_number, output_file, output_content)
      print(f"output/{output_file}.txt")
    else:
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
      print("PEAK MEMORY USAGE: Unable to measure")

    print()

  except FileNotFoundError:
    print(f"Error: Script not found: '{script_path}'")
  except Exception as e:
    print(f"Error: {e}")


def main():
  parser = argparse.ArgumentParser(
    description="Run a Python script and measure execution time and memory usage.",
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=40, width=200)
  )
  parser.add_argument("input_path", type=str, help="Script path in the format 'problem_number/solution_number' (e.g., 1002/2)")
  parser.add_argument("-i", "--input_file", type=str, help="Input file name (without extension). Ex: -i sample → input/sample.txt")
  parser.add_argument("-o", "--output_file", type=str, help="Output file name (without extension). Ex: -o result → output/result.txt")
  parser.add_argument("-d", "--interval", type=int, default=100, help="Delay when '@' or '#' is printed (milliseconds, default: 100)")
  parser.add_argument("-t", "--timeout", type=int, help="Max execution time (milliseconds). Process will be terminated if exceeded.")
  args = parser.parse_args()

  script_path, problem_number, unit_digit, thousand_digit = parse_script_path(args.input_path)
  measure_execution_time_and_memory(
    script_path,
    problem_number,
    unit_digit,
    thousand_digit,
    args.interval,
    input_file=args.input_file,
    output_file=args.output_file,
    timeout_ms=args.timeout
  )


if __name__ == "__main__":
  create_dir()
  main()