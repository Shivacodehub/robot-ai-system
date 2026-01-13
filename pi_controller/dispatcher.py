
def execute_step(step):
    action = step["action"]

    if action == "MOVE_FORWARD":
        move_forward(step.get("speed", 50))

    elif action == "MOVE_BACKWARD":
        move_backward(step.get("speed", 50))

    elif action == "TURN_LEFT":
        turn_left()

    elif action == "TURN_RIGHT":
        turn_right()

    elif action == "STOP":
        stop()

    elif action == "LOOK_UP":
        look_up(step.get("angle", 10))

    elif action == "LOOK_DOWN":
        look_down(step.get("angle", 10))

    elif action == "LOOK_CENTER":
        look_center()

    elif action == "LED_ON":
        led_on()

    elif action == "LED_OFF":
        led_off()

    elif action == "SPEAK":
        speak(step["text"])

    elif action == "CAPTURE_IMAGE":
        capture_image()
