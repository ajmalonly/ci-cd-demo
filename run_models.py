import os
from pathlib import Path

import duckdb

con = duckdb.connect()
con.execute("CREATE TABLE sales AS SELECT * FROM read_csv_auto('data/sales.csv')")

out = Path("output")
out.mkdir(exist_ok=True)
lines = ["# Latest sales report", ""]

for sql_file in sorted(Path("models").glob("*.sql")):
    result = con.sql(sql_file.read_text())
    result.write_csv(str(out / f"{sql_file.stem}.csv"))

    lines += [f"## {sql_file.stem}", ""]
    lines.append("| " + " | ".join(result.columns) + " |")
    lines.append("|" + " --- |" * len(result.columns))
    for row in result.fetchall():
        lines.append("| " + " | ".join(str(v) for v in row) + " |")
    lines.append("")

report = "\n".join(lines)
print(report)

summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    with open(summary, "a") as f:
        f.write(report)
