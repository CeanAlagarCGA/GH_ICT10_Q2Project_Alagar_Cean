from pyscript import display, document

names = {'cean alagar', 'joaquin tabije', 'cholo comanda',
         'jm piansay', 'mohammad calaca'}

def student_name(e):
    document.getElementById("output").innerHTML = ''
    first = document.getElementById("student_name_first").value.strip()
    last = document.getElementById("student_name_last").value.strip()

    full_name = (first + " " + last).lower()

    checker = full_name in names
    names.add(full_name)

    display_message = (f"Welcome {first}, you are now a part of the obmc club", f"Sorry {first}, you are already a member")

    display(display_message[checker], target="output")

