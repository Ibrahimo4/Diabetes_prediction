from app import app

#app = init_app()


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)
