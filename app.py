from flask import Flask, render_template, request, jsonify

from gpiozero import LED

app = Flask(__name__)
led_state = False;
led = LED(17)
led.off()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led', methods=['POST'])
def onoff():
    global led_state
    if led_state == False:
        led.on()
        led_state = not led_state
        return jsonify(status="on")
    else:
        led.off()
        led_state = not led_state
        return jsonify(status="off")
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
