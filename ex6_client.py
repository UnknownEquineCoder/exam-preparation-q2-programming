from __future__ import annotations

from socket import socket, AF_INET, SOCK_STREAM


class Hangman_Client:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.sock: socket = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def guess(self) -> str:
        choice: str = input("Enter a character: ")
        self.sock.sendall(choice.encode("utf-8"))
        data: str = self.sock.recv(1024).decode("utf-8")

        match data:
            case "invalid input":
                print("Invalid input")
            case "Game Over":
                print("Game Over")
            case _:
                print(data)
        return data


    def run(self) -> None:
        while True:
            try:
                self.guess()
            except KeyboardInterrupt:
                break

    def close(self) -> None:
        self.sock.close()


if __name__ == "__main__":
    client = Hangman_Client("localhost", 5050)
    client.run()
    client.close()
    print("Client closed")
