.. _example-latex-table-writer:

LaTeX table
-------------------------------------------
|LatexTableWriter| class can writes a table
with LaTeX ``array`` environment to the |stream| from a matrix of data.

:Sample Code:
    .. code-block:: python
        :caption: Write a LaTex table

        import pytablewriter

        def main():
            writer = pytablewriter.LatexTableWriter()
            writer.table_name = "example_table"
            writer.headers = ["int", "float", "str", "bool", "mix", "time"]
            writer.value_matrix = [
                [0,   0.1,      "hoge", True,   0,      "2017-01-01 03:04:05+0900"],
                [2,   "-2.23",  "foo",  False,  None,   "2017-12-23 45:01:23+0900"],
                [3,   0,        "bar",  "true",  "inf", "2017-03-03 33:44:55+0900"],
                [-10, -9.9,     "",     "FALSE", "nan", "2017-01-01 00:00:00+0900"],
            ]

            writer.write_table()

        if __name__ == "__main__":
            main()

:Output:
    .. code-block:: TeX

        \begin{array}{r | r | l | l | l | l} \hline
            \verb|int| & \verb|float| & \verb|str | & \verb|bool | & \verb| mix  | & \verb|          time          | \\ \hline
            \hline
              0 &  0.10 & hoge & True  &      0 & \verb|2017-01-01 03:04:05+0900| \\ \hline
              2 & -2.23 & foo  & False &        & \verb|2017-12-23 12:34:51+0900| \\ \hline
              3 &  0.00 & bar  & True  & \infty & \verb|2017-03-03 22:44:55+0900| \\ \hline
            -10 & -9.90 &      & False & NaN    & \verb|2017-01-01 00:00:00+0900| \\ \hline
        \end{array}

:Rendering Result:
    .. figure:: ss/latex_table.png
       :scale: 100%
       :alt: latex_table
