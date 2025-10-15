import json
from rich.console import Console
from rich.table import Table

console = Console()

def print_console_report(report):
    """Display the detected issues in a formatted table."""
    table = Table(title="Code Review Report")
    table.add_column("Type", style="bold cyan")
    table.add_column("Pattern")
    table.add_column("Message")

    for issue in report:
        table.add_row(issue["type"], issue["pattern"], issue["message"])
    console.print(table)

def save_json_report(report, out_path="reports/result.json"):
    """Save the issues to a JSON file inside the reports folder."""
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2)
    console.print(f"[green]✅ Report saved to {out_path}[/green]")
