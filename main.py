from database import Database
from gamedatabase import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.205.26.89:7687", "neo4j", "exhibits-drills-workman")
db.drop_all()

# Criando uma instância da classe GameDatabase para interagir com o banco de dados
game_db = GameDatabase(db)

# Criando jogadores
game_db.create_player(1,"Joao")
game_db.create_player(2, "Vinicius")
game_db.create_player(3, "Marcos")
game_db.create_player(4, "Wagner")
game_db.create_player(5, "Julio")

# Criando partidas
game_db.create_match(10)
game_db.create_match(20)
game_db.create_match(30)

# Adicionando jogadores às partidas
# jogo 1
game_db.add_player_to_match(1,10,40)
game_db.add_player_to_match(2,10,35)

#jogo 2
game_db.add_player_to_match(3,20,40)
game_db.add_player_to_match(4,20,25)

# Atualizando jogadores
game_db.update_player(1, "Joao Carlos")
game_db.update_player(2, "Vinicius de Moraes")

# Atualizando pontuação do jogador
game_db.update_player_score(4,20, 30)

# Deletando um jogador
game_db.delete_player(5)

# Deletando uma partida
game_db.delete_match(30)

# Lendo jogadores
game_db.get_players()

#Lendo partidas
game_db.get_matches()

# Lendo detalhes da partida
game_db.get_match_details(10)
game_db.get_match_details(20)

