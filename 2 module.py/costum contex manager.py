print("\nTry This: Custom Context Manager")
print("=" * 50)

class Connection:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        self.open = False

    def __enter__(self):
        self.open = True
        print(f"Connecting to {self.endpoint}...")
        return self

    def __exit__(self, exc_type, exc, tb):
        self.open = False
        print(f"Disconnected from {self.endpoint}")
        # Returning False ensures exceptions are not suppressed
        return False

    def send(self, payload: str) -> str:
        if not self.open:
            raise RuntimeError("not connected")
        return f"ACK:{payload}"

try:
    with Connection("api.service.local") as conn:
        print(conn.send("PING"))
        # Uncomment the line below to test the error handling:
        # raise ValueError("simulated error")
except Exception as e:
    print("Error during connection:", e)