not mode: sleep
-
^mixed mode$:
    mode.disable("sleep")
    mode.enable("dictation")
    mode.enable("command")
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")
^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
