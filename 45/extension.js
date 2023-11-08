import * as KeyboardUI from 'resource:///org/gnome/shell/ui/keyboard.js';

function _modifiedLastDeviceIsTouchscreen() {
    return false;
}

export default class BlockCaribou {
    constructor() {
        this._originalLastDeviceIsTouchscreen = null;
    }

    enable() {
        this._originalLastDeviceIsTouchscreen = KeyboardUI.KeyboardManager.prototype._lastDeviceIsTouchscreen;
        KeyboardUI.KeyboardManager.prototype._lastDeviceIsTouchscreen = _modifiedLastDeviceIsTouchscreen;
    }

    disable() {
        if (this._originalLastDeviceIsTouchscreen !== null) {
            KeyboardUI.KeyboardManager.prototype._lastDeviceIsTouchscreen = this._originalLastDeviceIsTouchscreen;
            this._originalLastDeviceIsTouchscreen = null;
        }
    }
}
