
import streamlit as st
import pymupdf
from datetime import datetime

# -------------------- PAGE CONFIGURATION --------------------

st.set_page_config(
    page_title="PaperTrail AI",
    page_icon="📚",
    layout="wide"
)

# -------------------- HEADER --------------------

st.title("📚 PaperTrail AI")
st.subheader("Research Paper Explorer")

st.write(
    "Upload research papers, search technical content, "
    "find relevant pages, and download search reports."
)

st.divider()

# -------------------- PDF UPLOAD --------------------

uploaded_files = st.file_uploader(
    "Upload research paper PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    papers = []

    # -------------------- TEXT EXTRACTION --------------------

    for pdf_file in uploaded_files:
        try:
            with pymupdf.open(
                stream=pdf_file.getvalue(),
                filetype="pdf"
            ) as document:

                pages = [
                    page.get_text()
                    for page in document
                ]

            papers.append({
                "name": pdf_file.name,
                "pages": pages
            })

        except Exception as error:
            st.error(
                f"Could not read {pdf_file.name}: {error}"
            )

    if papers:

        # -------------------- RESEARCH LIBRARY --------------------

        st.header("📚 Research Library")

        for paper in papers:
            page_count = len(paper["pages"])
            character_count = sum(
                len(page) for page in paper["pages"]
            )

            with st.expander(paper["name"]):
                st.write("Pages:", page_count)
                st.write(
                    "Extracted characters:",
                    f"{character_count:,}"
                )

        st.divider()

        # -------------------- DASHBOARD --------------------

        st.header("📊 Library Overview")

        total_pages = sum(
            len(paper["pages"]) for paper in papers
        )

        total_characters = sum(
            len(page)
            for paper in papers
            for page in paper["pages"]
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Papers Uploaded",
            len(papers)
        )

        col2.metric(
            "Total Pages",
            total_pages
        )

        col3.metric(
            "Extracted Characters",
            f"{total_characters:,}"
        )

        st.divider()

        # -------------------- PAPER SELECTION --------------------

        st.header("🔎 Search Research Papers")

        paper_names = [
            paper["name"] for paper in papers
        ]

        selected_papers = st.multiselect(
            "Select papers to search",
            options=paper_names,
            default=paper_names
        )

        selected_paper_data = [
            paper for paper in papers
            if paper["name"] in selected_papers
        ]

        # -------------------- KEYWORD SEARCH --------------------

        keyword = st.text_input(
            "Enter a keyword or phrase",
            placeholder="e.g. Python, IoT, machine learning"
        )

        if keyword.strip():

            results_by_paper = {}

            for paper in selected_paper_data:

                matches = []

                for page_number, page_text in enumerate(
                    paper["pages"],
                    start=1
                ):
                    for line in page_text.splitlines():

                        if keyword.casefold() in line.casefold():
                            matches.append({
                                "page": page_number,
                                "line": line.strip()
                            })

                if matches:
                    results_by_paper[paper["name"]] = matches

            # -------------------- MINIMUM MATCH FILTER --------------------

            min_matches = st.number_input(
                "Minimum matching lines per paper",
                min_value=1,
                value=1,
                step=1
            )

            # -------------------- RELEVANCE RANKING --------------------

            ranked_papers = sorted(
                [
                    item
                    for item in results_by_paper.items()
                    if len(item[1]) >= min_matches
                ],
                key=lambda item: len(item[1]),
                reverse=True
            )

            total_matches = sum(
                len(matches)
                for _, matches in ranked_papers
            )

            # -------------------- SEARCH METRICS --------------------

            st.subheader("Search Summary")

            metric1, metric2, metric3 = st.columns(3)

            metric1.metric(
                "Matching Lines",
                total_matches
            )

            metric2.metric(
                "Papers Found",
                len(ranked_papers)
            )

            metric3.metric(
                "Papers Searched",
                len(selected_paper_data)
            )

            # -------------------- DISPLAY RESULTS --------------------

            st.subheader("Ranked Results")

            if ranked_papers:

                for paper_name, matches in ranked_papers:

                    with st.expander(
                        f"{paper_name} | "
                        f"{len(matches)} matching lines",
                        expanded=True
                    ):

                        for result in matches:
                            st.markdown(
                                f"**Page {result['page']}**"
                            )

                            st.write(
                                result["line"][:250]
                            )

                            st.divider()

            else:
                st.info(
                    "No papers matched your keyword "
                    "and minimum-match settings."
                )

            # -------------------- DOWNLOAD REPORT --------------------

            report_lines = [
                "PAPERTRAIL AI - SEARCH REPORT",
                "=" * 35,
                f"Keyword: {keyword}",
                f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                f"Minimum matching lines: {min_matches}",
                f"Papers searched: {len(selected_paper_data)}",
                f"Papers found: {len(ranked_papers)}",
                f"Total matching lines: {total_matches}",
                "",
                "SEARCH RESULTS",
                "=" * 35,
                ""
            ]

            for paper_name, matches in ranked_papers:

                report_lines.append(
                    f"{paper_name} "
                    f"({len(matches)} matching lines)"
                )

                for result in matches:
                    report_lines.append(
                        f"Page {result['page']}: "
                        f"{result['line']}"
                    )

                report_lines.append("")

            if not ranked_papers:
                report_lines.append(
                    "No matching papers found."
                )

            report_text = "\n".join(report_lines)

            st.download_button(
                label="📥 Download Search Report",
                data=report_text,
                file_name="papertrail_search_report.txt",
                mime="text/plain"
            )

        else:
            st.info(
                "Enter a keyword above to search your papers."
            )

else:
    st.info(
        "Upload one or more PDF research papers to get started."
    )

# -------------------- FOOTER --------------------

st.divider()

st.caption(
    "PaperTrail AI | Research made easier"
)
