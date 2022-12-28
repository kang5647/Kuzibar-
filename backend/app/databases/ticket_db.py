from app.databases.db import DB_handler


class Ticket_DB_handler(DB_handler):
    def __init__(self) -> None:
        super().__init__()
        self.collection = self.db.ticket

    def get_one(self, lottery_id: str, user_id: str):
        """Get the ticket by lottery_id and user_id."""
        return self.collection.find_one({'lottery_id': lottery_id, 'user_id': user_id})

    def update_quantity(self, lottery_id: str, user_id: str, quantity: int):
        # Define the query and update
        query = {'lottery_id': lottery_id, 'user_id': user_id}
        update = {'$inc': {'entry_quantity': quantity}}

        # Update the document
        return self.collection.update_one(query, update)
