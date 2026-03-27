import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    sys.stdout.write(f"[STANDARD] Archive status from {archivist_id}: {status_report}\n")
    sys.stderr.write(f"[ALERT] System diagnostic: Communication channels verified\n")


if __name__ == "__main__":
    main()
