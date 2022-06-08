import socket

import random

import re


class Hangman_Server:
    def __init__(
        self,
        host,
        port,
    ):
        self.host = host
        self.port = port

    def match_guess(self, word_to_guess, user_guesses):
        state = list("_" * len(word_to_guess))
        for c in user_guesses:
            for match in list(re.finditer(c, word_to_guess)):
                state[match.start()] = c
        return "".join(state), user_guesses[-1] in word_to_guess

    def start(self, wordlist):
        print("Server started.. ")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen()
        connection, client_addr = sock.accept()
        print("Server started.. ")
        # Select a random word from the list of possible words​

        word_to_guess = random.choice(wordlist)
        user_display = "_" * len(word_to_guess)
        connection.sendall(user_display.encode("utf-8"))
        guessed_chars = []
        wrong_guesses = 0

        while True:
            data = connection.recv(1024).decode("utf-8")
            # Expecting only characters A-Z​

            # invalid data is ignored​
            print(data)
            if len(data) != 1 or ord(data[0]) < 65 or ord(data[0]) > 90:
                connection.sendall("invalid input".encode("utf-8"))

            else:

                guessed_chars.append(data[0])

                response, correct = self.match_guess(word_to_guess, guessed_chars)

                if not correct:
                    wrong_guesses += 1

                if wrong_guesses > 3:

                    connection.sendall(
                        f"Game Over, you lost. The word was {word_to_guess}".encode(
                            "utf-8"
                        )
                    )
                    break

                if response == word_to_guess:

                    connection.sendall(
                        f"Game Over, you guessed {word_to_guess} correctly".encode(
                            "utf-8"
                        )
                    )
                    break

                connection.sendall(response.encode("utf-8"))

        connection.close()


host = "localhost"

port = 5500

Hangman_Server(host, port).start(["APPLE", "BANANA", "ORANGE", "POMELO"])
