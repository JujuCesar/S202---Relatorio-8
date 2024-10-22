class GameDatabase:
    def __init__(self, database):
        self.db = database

    # Create a new player
    def create_player(self, player_id, name):
        query = "CREATE (:Player {id: $player_id, name: $name})"
        parameters = {"player_id": player_id, "name": name}
        self.db.execute_query(query, parameters)

    # Create a new match
    def create_match(self, match_id):
        query = "CREATE (:Match {id: $match_id})"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)

    # Link a player to a match with their score
    def add_player_to_match(self, player_id, match_id, score):
        query = """
        MATCH (p:Player {id: $player_id}), (m:Match {id: $match_id})
        CREATE (p)-[:JOGOU_EM {score: $score}]->(m)
        """
        parameters = {"player_id": player_id, "match_id": match_id, "score": score}
        self.db.execute_query(query, parameters)

    # Get all players
    def get_players(self):
        query = "MATCH (p:Player) RETURN p.id AS id, p.name AS name"
        results = self.db.execute_query(query)
        return [{"id": result["id"], "name": result["name"]} for result in results]

    # Get all matches
    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.id AS id"
        results = self.db.execute_query(query)
        return [{"id": result["id"]} for result in results]

    # Get match details, including participating players and their scores
    def get_match_details(self, match_id):
        query = """
        MATCH (p:Player)-[r:JOGOU_EM]->(m:Match {id: $match_id})
        RETURN p.name AS player_name, r.score AS score
        """
        parameters = {"match_id": match_id}
        results = self.db.execute_query(query, parameters)
        return [{"player_name": result["player_name"], "score": result["score"]} for result in results]

    # Update player's name
    def update_player(self, player_id, new_name):
        query = "MATCH (p:Player {id: $player_id}) SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    # Update a player's score in a specific match
    def update_player_score(self, player_id, match_id, new_score):
        query = """
        MATCH (p:Player {id: $player_id})-[r:JOGOU_EM]->(m:Match {id: $match_id})
        SET r.score = $new_score
        """
        parameters = {"player_id": player_id, "match_id": match_id, "new_score": new_score}
        self.db.execute_query(query, parameters)

    # Delete a player and all their relationships
    def delete_player(self, player_id):
        query = "MATCH (p:Player {id: $player_id}) DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    # Delete a match and all related relationships
    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)
