

from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getlogin()
    
    # Get server time in IST
    ist_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')

    # Get top output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    # Prepare response
    response = f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> Your Full Name</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
