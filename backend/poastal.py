from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import os, sys
sys.path.append(os.path.abspath('./modules'))

#import modules
from twitter import twitter_email
from snapchat import snapchat_email
# from parler import parler_email
from mewe import mewe_email
from rumble import rumble_email
from verify import *
from duolingo import duolingo_name_check, duolingo_email, duolingo_image
from adobe import *
from wordpress import wordpress_email
from imgur import imgur_email
from hulu import hulu_email
from rubmaps import rubmaps_email
from github import *
from gravatar import hash_email, parse_json, gravatar_email
from discord import *

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

@app.route('/')
def poastal():
    email = request.args.get('email')
    if email:
        twitter_result = twitter_email(email)
        snapchat_result = snapchat_email(email)
        mewe_result = mewe_email(email)
        rumble_result = rumble_email(email)
        disposable_result = disposable(email)
        spam_result = spam(email)
        deliverable_result = deliverable(email)
        duolingo_result = duolingo_email(email)
        duolingo_name = duolingo_name_check(email)
        duolingo_image_url = duolingo_image(email)
        adobe_result = adobe_email(email)
        adobe_image_url = adobe_image(email)
        adobe_facebook_result = adobe_facebook_email(email)
        wordpress_result = wordpress_email(email)
        imgur_result = imgur_email(email)
        hulu_result = hulu_email(email)
        rubmaps_result = rubmaps_email(email)
        github_result = github_email(email)
        github_name = githubname_email(email)
        github_location = githublocation_email(email)
        github_image = github_avatar_url(email)
        gravatar_response = hash_email(email)
        gravatar_image = parse_json(gravatar_response, 'thumbnailUrl')
        gravatar_result = gravatar_email(email)
        discord_result = discord_email(email)

        return jsonify({
            'Duolingo Name': duolingo_name,
            'GitHub Name': github_name,  # Add GitHub Name to the table
            'Location': github_location,  # Add GitHub Location to the table
            'Image': {
                'Duolingo': duolingo_image_url,
                'GitHub': github_image,
                'Gravatar': gravatar_image,
                'Adobe': adobe_image_url,
            },
            'Deliverable': deliverable_result,
            'Disposable': disposable_result,
            'Spam': spam_result,
            #start profiles
            'profiles':{
                'Facebook': adobe_facebook_result,
                'Twitter': twitter_result,
                'Snapchat': snapchat_result,
                'Rumble': rumble_result,
                'MeWe': mewe_result,
                'Imgur': imgur_result,
                'Adobe': adobe_result,
                'Wordpress': wordpress_result,
                'Duolingo': duolingo_result,
                'Hulu': hulu_result,
                'Rubmaps': rubmaps_result,
                'Github': github_result,
                'Gravatar': gravatar_result,
                'Discord': discord_result,
            }
        })
    else:
        html_response = """
        <!DOCTYPE html>
        <html lang=\"en\">
        <head>
            <meta charset=\"utf-8\">
            <title>Poastal Email Lookup</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 2rem; background: #0f172a; color: #e2e8f0; }
                h1 { color: #38bdf8; }
                form { margin-top: 1.5rem; }
                label { display: block; margin-bottom: 0.5rem; font-weight: bold; }
                input[type=email] {
                    padding: 0.6rem 0.8rem;
                    width: 100%;
                    max-width: 26rem;
                    border: 1px solid #475569;
                    border-radius: 0.5rem;
                    background: #1e293b;
                    color: inherit;
                }
                button {
                    margin-top: 1rem;
                    padding: 0.6rem 1.4rem;
                    border: none;
                    border-radius: 0.5rem;
                    background: #38bdf8;
                    color: #0f172a;
                    font-weight: bold;
                    cursor: pointer;
                }
                button:hover { background: #0ea5e9; }
                code { background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.3rem; }
            </style>
        </head>
        <body>
            <h1>Poastal Email Lookup</h1>
            <p>Provide an email address to retrieve OSINT results for that account.</p>
            <form action="/" method="get">
                <label for="email">Email address</label>
                <input id="email" name="email" type="email" placeholder="example@gmail.com" required>
                <button type="submit">Look up email</button>
            </form>
            <p>Or call this endpoint directly: <code>/?email=example@gmail.com</code></p>
        </body>
        </html>
        """

        return Response(html_response, mimetype='text/html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
