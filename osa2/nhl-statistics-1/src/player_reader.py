import ssl
from urllib import request
from player import Player

#url = "https://example.com"
#context = ssl._create_unverified_context()
#response = request.urlopen(url, context=context)
#content = response.read()

class PlayerReader:
    def __init__(self, url):
        self._url = url
        #self._url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"

    def get_players(self):
        players_file = request.urlopen(self._url)
        players = []

        for line in players_file:
            decoded_line = line.decode("utf-8")
            parts = decoded_line.split(";")

            if len(parts) > 3:
                player = Player(
                    parts[0].strip(),
                    parts[1].strip(),
                    int(parts[3].strip()),
                    int(parts[4].strip())
                )

                players.append(player)

        return players
