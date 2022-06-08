from __future__ import annotations

import random
import re
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM

from string import ascii_uppercase


class Multitheaded_Hangman_Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.wordlist: list[str] = ["APPLE", "BANANA", "ORANGE", "POMELO"]
        self.sock: socket = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen()
        self.clients: list[socket] = []
        self.threads: list[Thread] = []
        self.word_to_guess: str = ""
        self.user_display: str = ""
        self.guessed_chars: list[str] = []
        self.wrong_guesses: int = 0
        self.running: bool = True
        self.start()

    def start(self) -> None:
        print("Server started.. ")
        while self.running:
            connection, client_addr = self.sock.accept()
            self.clients.append(connection)
            self.threads.append(
                Thread(target=self.handle_client, args=(connection,))
            )
            self.threads[-1].start()
            print("Server started.. ")

            self.word_to_guess = random.choice(self.wordlist)
            self.user_display = "_" * len(self.word_to_guess)
            connection.sendall(self.user_display.encode("utf-8"))
            self.guessed_chars = []
            self.wrong_guesses = 0
            self.running = False
            break
        for thread in self.threads:
            thread.join()
        self.sock.close()

    def handle_client(self, connection: socket) -> None:
        while True:
            data = connection.recv(1024).decode("utf-8")
            
            if len(data) != 1 or data not in ascii_uppercase:
                connection.sendall("invalid input".encode("utf-8"))
                continue
            if data[0] in self.guessed_chars:
                connection.sendall(
                    "You have already guessed that character".encode("utf-8")
                )
                continue
            self.guessed_chars.append(data[0])
            response, correct = self.match_guess(self.word_to_guess, self.guessed_chars)
            if not correct:
                self.wrong_guesses += 1
            if self.wrong_guesses > 3:
                connection.sendall(
                    f"Game Over, you lost. The word was {self.word_to_guess}".encode(
                        "utf-8"
                    )
                )
                break
            if response == self.word_to_guess:
                connection.sendall(
                    f"Game Over, you guessed {self.word_to_guess} correctly".encode(
                        "utf-8"
                    )
                )
                break
            connection.sendall(response.encode("utf-8"))
        connection.close()

    def match_guess(self, word_to_guess: str, user_guesses: list[str]) -> tuple[str, bool]:
        correct = True
        response = ""
        for i in range(len(word_to_guess)):
            if word_to_guess[i] in user_guesses:
                response += word_to_guess[i]
            else:
                response += "_"
                correct = False
        return response, correct

    def run(self) -> None:
        while True:
            try:
                self.start()
            except KeyboardInterrupt:
                break
        self.sock.close()


multi_server = Multitheaded_Hangman_Server("localhost", 5050)
multi_server.run()
