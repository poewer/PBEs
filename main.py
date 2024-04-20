from sanic import Sanic
from sanic.response import text

app = Sanic("PBEs-backend")

@app.route("/")
async def test(request):
    return text("Hello World!")

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
