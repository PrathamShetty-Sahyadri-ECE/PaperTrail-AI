
import pymupdf
from pathlib import Path
from datetime import datetime

papers_folder = Path("papers")
history_path = papers_folder / "search_history.txt"
report_path = papers_folder / "search_report.txt"


def view_history():
    if history_path.exists():
        print("\n--- Search History ---")
        print(history_path.read_text(encoding="utf-8"))
    else:
        print("No search history found.")


def search_papers():
    pdf_files = list(papers_folder.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found.")
        return

    keyword = input("Enter a keyword to search: ").strip()

    if not keyword:
        print("Please enter a keyword.")
        return

    min_input = input(
        "Minimum matching lines per paper (default 1): "
    ).strip()

    if min_input:
        try:
            min_matches = int(min_input)
            if min_matches < 1:
                print("Please enter a number of at least 1.")
                return
        except ValueError:
            print("Invalid number. Please enter an integer.")
            return
    else:
        min_matches = 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with history_path.open("a", encoding="utf-8") as history:
        history.write(f"{timestamp} | Keyword: {keyword}\n")

    results_by_paper = {}

    for pdf_path in pdf_files:
        matches = []

        try:
            with pymupdf.open(pdf_path) as document:
                for page_number, page in enumerate(document, start=1):
                    for line in page.get_text().splitlines():
                        if keyword.casefold() in line.casefold():
                            matches.append(
                                f"Page {page_number}: {line.strip()[:250]}"
                            )
        except Exception as error:
            print(f"Could not read {pdf_path.name}: {error}")
            continue

        if matches:
            results_by_paper[pdf_path.name] = matches

    ranked_papers = sorted(
        [
            item for item in results_by_paper.items()
            if len(item[1]) >= min_matches
        ],
        key=lambda item: len(item[1]),
        reverse=True
    )

    report_lines = [
        f"Search Report: {keyword}",
        f"Date and time: {timestamp}",
        f"Minimum matching lines per paper: {min_matches}",
        ""
    ]

    total_results = 0

    if ranked_papers:
        print("\n--- Ranked Search Results ---")

        for paper_name, matches in ranked_papers:
            print(f"\n{paper_name} - {len(matches)} matching lines")
            report_lines.append(
                f"{paper_name} - {len(matches)} matching lines"
            )

            for match in matches:
                print(" ", match)
                report_lines.append("  " + match)
                total_results += 1
    else:
        print("\nNo papers met the minimum match requirement.")
        report_lines.append("No papers met the minimum match requirement.")

    report_lines.extend([
        "",
        "Search Summary",
        f"Total matching lines in displayed papers: {total_results}",
        f"Papers displayed: {len(ranked_papers)}",
        f"Papers with any matches: {len(results_by_paper)}"
    ])

    report_path.write_text(
        "\n".join(report_lines),
        encoding="utf-8"
    )

    print("\nSearch Summary")
    print("Total matching lines in displayed papers:", total_results)
    print("Papers displayed:", len(ranked_papers))
    print("Papers with any matches:", len(results_by_paper))
    print("Search report saved:", report_path)


while True:
    print("\n=== PaperTrail AI ===")
    print("1. Search research papers")
    print("2. View search history")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        search_papers()
    elif choice == "2":
        view_history()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Enter 1, 2, or 3.")
