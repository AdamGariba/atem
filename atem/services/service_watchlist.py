from rich.console import Console
from rich.table import Table


from database import create_connection

class WatchList:
    def __init__(self):
        pass
    
    def getWatchList(self):
        # Create connection
        conn = create_connection()
        # Get a cursor
        cur = conn.cursor()
        # Query all rows of database
        cur.execute("SELECT * FROM ANIME")
        # Fetch all rows
        result_rows = cur.fetchall()

        # Create a Rich console
        console = Console()

        # Build the table
        table = Table(show_header=True, header_style="bold yellow2", show_lines=True)
        table.add_column("Title", style="dim")
        table.add_column("Rating")
        table.add_column("Review")
        table.add_column("Watched")

        # Fill the rows
        for row in result_rows:
            # Get the data for each row
            title = row[1]
            rating = str(row[2])
            review = row[3]

            if row[4] == 1:
                isFinished = ":white_check_mark:"
            else:
                isFinished = ":cross_mark:"

            table.add_row(title, rating, review, isFinished)
        

        # Print the table to the screen
        console.print(table)