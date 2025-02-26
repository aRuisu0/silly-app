from flask import Flask

app = Flask(__name__)

base_html = """
<html>
    <head>
        <title>{title}</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body {{
                background-color: #87CEEB;
                font-family: 'Press Start 2P', cursive;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }}
            .window {{
                background: #FF99CC;
                border: 5px solid #003366;
                padding: 20px;
                box-shadow: 10px 10px 0px #003366;
                border-radius: 10px;
                text-align: center;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                width: 60%;
                max-width: 500px;
            }}
            p {{
                color: #003366;
                margin-bottom: 20px;
            }}
            .gif-container img {{
                width: 450px;
                height: auto;
                margin-bottom: 20px;
            }}
            button {{
                background-color: #ffcc00;
                border: 3px solid #003366;
                font-family: 'Press Start 2P', cursive;
                padding: 10px;
                margin: 10px;
                cursor: pointer;
            }}
            button:hover {{
                background-color: #ff9900;
            }}
        </style>
    </head>
    <body>
        <div class='window'>
            <p>{message}</p>
            <div class='gif-container'>
                <img src="{gif}" alt="Animated GIF">
            </div>
            {buttons}
        </div>
    </body>
</html>
"""

@app.route('/')
def home():
    return base_html.format(
        title="Choice App",
        message="Hi I'm sorry for being mean to you earlier, Please select these two options on how you feel: (Tip: select both) ",
        gif="https://media.tenor.com/NZh6iP8wgKMAAAAM/crying-stitch.gif",  # Replace with your own GIF
        buttons="""
            <a href='/option1'><button>You still love me but think i'm annoying</button></a>
            <a href='/option2'><button>You think I'm annoying but still love me</button></a>
        """
    )

@app.route('/option1')
def option1():
    return base_html.format(
        title="Option 1",
        message="You chose Option 1!",
        gif="https://media.tenor.com/7gCOgRDEpxcAAAAM/disney-dance.gif",
        buttons="<a href='/'><button>I'm sorry I love you so much and I'll make it up to you</button></a>"
    )

@app.route('/option2')
def option2():
    return base_html.format(
        title="Option 2",
        message="You chose Option 2!",
        gif="https://media.tenor.com/uN8nTrfBEK0AAAAM/lilo-and-stitch-hugs.gif",
        buttons="<a href='/'><button>You're my family and I'm sorry for hurting you</button></a>"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
