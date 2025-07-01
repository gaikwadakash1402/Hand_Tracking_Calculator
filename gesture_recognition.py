# Mapping of finger states to calculator keys
GESTURE_MAP = {
    (0,1,0,0,0): '1',
    (0,1,1,0,0): '2',
    (0,1,1,1,0): '3',
    (0,1,1,1,1): '4',
    (1,1,1,1,1): '5',
    (0,0,0,0,0): '0',
    (0,1,0,0,1): '+',
    (0,1,0,1,0): '-',
    (0,1,1,0,1): '*',
    (1,0,0,1,0): '/',
    (1,0,0,0,1): '='
}

COOLDOWN_FRAMES = 20

class GestureRecognizer:
    def __init__(self):
        self.prev_gesture = None
        self.cooldown_counter = 0

    def get_finger_states(self, fingers):
        return tuple(fingers)

    def recognize(self, fingers):
        states = self.get_finger_states(fingers)
        gesture = GESTURE_MAP.get(states, None)

        if gesture == self.prev_gesture:
            self.cooldown_counter += 1
        else:
            self.prev_gesture = gesture
            self.cooldown_counter = 0

        if gesture and self.cooldown_counter >= COOLDOWN_FRAMES:
            self.cooldown_counter = 0
            return gesture
        return None