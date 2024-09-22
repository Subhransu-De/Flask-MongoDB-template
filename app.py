from dotenv import load_dotenv

from app import create_app

if __name__ == "__main__":
    print(load_dotenv(".env"))
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
