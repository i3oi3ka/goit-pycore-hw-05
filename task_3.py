"""task 3"""

from collections import defaultdict
import sys


def parse_log_line(line: str) -> dict:
    """
    Parse a single log line into a dictionary.

    Args:
        line (str): A log line in the format 'date time level message'.

    Returns:
        dict: A dictionary containing parsed log information with keys
        'date', 'time', 'type', and 'msg'.
    """
    line_list = line.split()
    try:
        return {
            "date": line_list[0],
            "time": line_list[1],
            "level": line_list[2],
            "msg": " ".join(line_list[3:]),
        }
    except IndexError:
        print(f"Incorrect logfile in line: {line}")
        sys.exit(1)


def load_logs(file_path: str) -> list:
    """
    Load logs from a given file and parse each line.

    Args:
        file_path (str): The path to the log file.

    Returns:
        list: A list of dictionaries, each representing a parsed log entry.
    """
    logs_list = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                logs_list.append(parse_log_line(line))
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error loading file: {e}")
        sys.exit(1)
    return logs_list


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filter logs by a specified log level.

    Args:
        logs (list): A list of log entries (dictionaries).
        level (str): The log level to filter by.

    Returns:
        list: A list of log entries that match the specified log level.
    """
    return list(filter(lambda x: x["level"] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    """
    Count the number of log entries for each log level.

    Args:
        logs (list): A list of log entries (dictionaries).

    Returns:
        dict: A dictionary with log levels as keys and their respective counts as values.
    """
    count_logs = defaultdict(int)
    for log in logs:
        count_logs[log["level"]] += 1
    return dict(count_logs)


def display_log_counts(counts: dict):
    """
    Display the count of log entries for each log level.

    Args:
        counts (dict): A dictionary with log levels as keys and their respective counts as values.
    """
    print("Log Level       | Count")
    print("-" * 16 + "|" + "-" * 6)
    for error, count in counts.items():
        print(f"{error:<15} | {count}")


def display_logs_by_level(logs_by_level: list):
    """
    Display log entries of a specific log level.

    Args:
        logs_by_level (list): A list of log entries (dictionaries) to display.
    """
    for log in logs_by_level:
        print(f"{log['date']} {log['time']} - {log['msg']}")


def main():
    """
    Main function to execute the log processing script.
    """
    if len(sys.argv) < 2:
        print("Usage: python script.py <log_file_path> [log_level]")
        sys.exit(1)

    path = sys.argv[1]
    logs = load_logs(path)

    display_log_counts(count_logs_by_level(logs))

    if len(sys.argv) > 2:
        log_level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            print(f"\nDetails for logs with level '{log_level}':")
            display_logs_by_level(filtered_logs)
        else:
            print(f"No logs found for level '{log_level}'.")


if __name__ == "__main__":
    main()
