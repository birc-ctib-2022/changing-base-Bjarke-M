[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8448315&assignment_repo_type=AssignmentRepo)
# Changing base

In `src/base.py` you will find a function, `change_to_base(n, b)` that should change the number `n` to a string that is the same number but in base `b`. It doesn't do that right now, but you can fix that (I know you can!).

But maybe, just maybe, there are some special cases that you hadn't thought about.

- Can you handle when `n` is zero?
- What about when `n` is negative?
    - Do you know how integer division works on negative numbers?
    - Did you know that it depends on the programming language and sometimes the hardware?
- If you are thinking of changing signs, did you know that in most languages, you don't have the same number of positive and negative numbers? Usually, there is one more negative number, that doesn't have a corresponding positive number. Could you handle that?

Have fun!
