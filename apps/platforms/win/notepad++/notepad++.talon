

## tab_previous():
     #  actions.key('ctrl-pageup')
## tab_next():
     #  actions.key('ctrl-pagedown')
## toggle_comment():
     #  actions.key('ctrl-q')
## line_clone():
     #  actions.key('ctrl-d')
## line_swap_up():
     #  actions.key('ctrl-shift-up')
## line_swap_down():
     #  actions.key('ctrl-shift-down')
## indent_more(): actions.key('tab')
## indent_less(): actions.key('shift-tab')
## jump_line(n: int):
     #  actions.key("ctrl-g")
     #  actions.insert(str(n))
     #  actions.key("enter")

## find(text: str):
     #  actions.key("ctrl-f")
     #  actions.insert(text)

## select_next_occurrence(text: str):
     #  actions.edit.find(text)
     #  actions.sleep("100ms")
     #  actions.key("enter esc")
     #  actions.sleep("100ms")

## select_previous_occurrence(text: str):
     #  actions.edit.find(text)
     #  actions.sleep("100ms")
     #  actions.key("shift-enter esc")
     #  actions.sleep("100ms")

## tab_jump(number: int):
     #  if number < 10:
     #      actions.key("ctrl-keypad_{}".format(number))

## tab_final():
     #  """Jumps to the final tab"""
     #  print("Notepad doesn't support this...")
     #   # actions.key("ctrl-numpad_0")

## find(text: str):
     #  """Triggers find in current editor"""
     #  actions.key("ctrl-f")

     #  if text:
     #      actions.insert(text)

## find_next():
     #  actions.key("enter")

## find_previous():
     #  actions.key("shift-enter")

## find_everywhere(text: str):
     #  """Triggers find across project"""

     #  actions.key("ctrl-shift-f")

     #  if text:
     #      actions.insert(text)

## find_toggle_match_by_case():
     #  """Toggles find match by case sensitivity"""
     #  actions.key("alt-c")

## find_toggle_match_by_word():
     #  """Toggles find match by whole words"""
     #  actions.key("alt-w")

## find_toggle_match_by_regex():
     #  """Toggles find match by regex"""
     #  actions.key("alt-g")

## replace(text: str):
     #  """Search and replaces in the active editor"""
     #  actions.key("esc ctrl-h")

     #  if text:
     #      actions.insert(text)

## replace_everywhere(text: str):
     #  """Search and replaces in the entire project"""
     #  actions.key("esc ctrl-shift-f")

     #  if text:
     #      actions.insert(text)

## replace_confirm():
     #  """Confirm replace at current position"""
     #  actions.key("alt-r")

## replace_confirm_all():