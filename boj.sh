#!/bin/bash

function open_boj() {
  local problem_number=$1
  local solve_number=$2

  local unit_digit="0"
  if [ $problem_number -ge 10000 ]; then
    unit_digit=$(printf "%d" $(($problem_number / 10000)))
  fi
  local thousand_digit=$(printf "%02d" $(($problem_number / 1000 % 100)))
  local path="./${unit_digit}/${thousand_digit}/${problem_number}"

  if [ ! -d "$path" ]; then
    echo "Error: Path '$path' does not exist."
    exit 1
  fi

  if [ -z "$solve_number" ]; then
    solve_number=$(find "$path" -maxdepth 1 -name "*.py" | sed 's/.*\/\([0-9]*\)\.py/\1/' | sort -n | tail -n 1)
    if [ -z "$solve_number" ]; then
      echo "Error: No solution files found in '$path'."
      exit 1
    fi
  fi

  local file_path="${path}/${solve_number}.py"

  if [ ! -f "$file_path" ]; then
    echo "Error: File '$file_path' does not exist."
    exit 1
  fi

  code "$file_path" -r
}

function create_boj() {
  local problem_number=$1

  local unit_digit="0"
  if [ $problem_number -ge 10000 ]; then
    unit_digit=$(printf "%d" $(($problem_number / 10000)))
  fi
  local thousand_digit=$(printf "%02d" $(($problem_number / 1000 % 100)))
  local path="./${unit_digit}/${thousand_digit}/${problem_number}"

  mkdir -p "$path"

  local next_solve_number=$(find "$path" -maxdepth 1 -name "*.py" | sed 's/.*\/\([0-9]*\)\.py/\1/' | sort -n | tail -n 1)
  if [ -z "$next_solve_number" ]; then
    next_solve_number=1
  else
    next_solve_number=$(($next_solve_number + 1))
  fi

  local file_path="${path}/${next_solve_number}.py"

  if [ ! -f "$file_path" ]; then
    echo "# Solution for problem $problem_number, attempt $next_solve_number" > "$file_path"
  fi

  code "$file_path" -r
}

problem_number=""
solve_number=""
create_mode=false

while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    -o|--open)
      problem_number="$2"
      shift
      shift
      ;;
    -n|--number)
      solve_number="$2"
      shift
      shift
      ;;
    -c|--create)
      problem_number="$2"
      create_mode=true
      shift
      shift
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

if [ -z "$problem_number" ]; then
  echo "Error: Problem number is required. Use -o, --open, or -c, --create."
  exit 1
fi

if $create_mode; then
  create_boj "$problem_number"
else
  open_boj "$problem_number" "$solve_number"
fi