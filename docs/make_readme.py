#!/usr/bin/env python3

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import sys

from path import Path
from readmemaker import ReadmeMaker


PROJECT_NAME = "pytablewriter"
OUTPUT_DIR = ".."


def write_examples(maker: ReadmeMaker) -> None:
    maker.set_indent_level(0)
    maker.write_chapter("Examples")

    examples_root = Path("pages").joinpath("examples")

    maker.set_indent_level(1)
    maker.write_chapter("Write tables")
    maker.inc_indent_level()

    maker.write_chapter("Write a Markdown table")
    maker.write_file(examples_root.joinpath("table_format", "text", "markdown_example.txt"))

    maker.inc_indent_level()
    maker.write_chapter("Write a Markdown table with a margin")
    maker.write_file(
        examples_root.joinpath("table_format", "text", "markdown_example_with_margin.txt")
    )
    maker.dec_indent_level()

    maker.write_chapter("Write a reStructuredText table (Grid Tables)")
    maker.write_file(
        examples_root.joinpath("table_format", "text", "rst", "rst_grid_table_example.txt")
    )

    maker.write_chapter(
        "Write a table with JavaScript format (as a nested list variable definition)"
    )
    maker.write_file(
        examples_root.joinpath("table_format", "text", "sourcecode", "javascript_example.txt")
    )

    maker.write_chapter("Write a table to an Excel sheet")
    maker.write_file(
        examples_root.joinpath("table_format", "binary", "spreadsheet", "exel_single_example.txt")
    )

    maker.write_chapter("Write a Unicode table")
    maker.write_file(examples_root.joinpath("table_format", "text", "unicode_example.txt"))

    maker.write_chapter("Write a Markdown table from ``pandas.DataFrame`` instance")
    maker.write_file(examples_root.joinpath("datasource", "from_pandas_dataframe_example.txt"))

    maker.write_chapter("Write a markdown table from a space-separated values")
    maker.write_file(examples_root.joinpath("datasource", "from_ssv_example.txt"))

    maker.set_indent_level(1)
    maker.write_chapter("Get rendered tabular text as str")
    maker.write_file(examples_root.joinpath("output", "dump", "dumps.txt"))

    maker.set_indent_level(1)
    maker.write_chapter("Configure table styles")
    maker.inc_indent_level()
    maker.write_file(examples_root.joinpath("style", "style_example.txt"))

    maker.set_indent_level(1)
    maker.write_chapter("Make tables for specific applications")
    maker.inc_indent_level()

    maker.write_chapter("Create Elasticsearch index and put data")
    maker.write_file(examples_root.joinpath("table_format", "elasticsearch_example.txt"))

    maker.write_chapter("Render a table on Jupyter Notebook")
    maker.write_file(examples_root.joinpath("jupyter_notebook", "jupyter_notebook_example.txt"))

    maker.set_indent_level(1)
    maker.write_chapter("Multibyte character support")
    maker.inc_indent_level()

    maker.write_chapter("Write a table using multibyte character")
    maker.write_file(examples_root.joinpath("multibyte", "multibyte_table_example.txt"))

    maker.set_indent_level(1)
    maker.write_chapter("For more information")
    maker.write_lines(
        [
            "More examples are available at ",
            "https://{:s}.rtfd.io/en/latest/pages/examples/index.html".format(PROJECT_NAME),
        ]
    )


def main():
    maker = ReadmeMaker(
        PROJECT_NAME,
        OUTPUT_DIR,
        is_make_toc=True,
        project_url="https://github.com/thombashi/{}".format(PROJECT_NAME),
    )

    maker.write_chapter("Summary")
    maker.write_introduction_file("summary.txt")
    maker.write_introduction_file("badges.txt")
    maker.write_introduction_file("feature.txt")

    write_examples(maker)

    maker.write_file(maker.doc_page_root_dir_path.joinpath("installation.rst"))

    maker.set_indent_level(0)
    maker.write_chapter("Documentation")
    maker.write_lines(["https://{:s}.rtfd.io/".format(PROJECT_NAME)])

    maker.write_chapter("Related Project")
    maker.write_lines(
        [
            "- `pytablereader <https://github.com/thombashi/pytablereader>`__",
            "    - Tabular data loaded by ``pytablereader`` can be written "
            "another tabular data format with ``pytablewriter``.",
        ]
    )

    maker.write_chapter("Tasks")
    maker.write_lines(["https://trello.com/b/kE0XG34y"])

    return 0


if __name__ == "__main__":
    sys.exit(main())
