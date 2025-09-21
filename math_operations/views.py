from django.shortcuts import render

def calculate(request):
    if request.method == "POST":
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        z = int(request.POST['z'])

        steps = []
        steps.append(f"x = {x}, y = {y}, z = {z}")

        x += y
        steps.append(f"x += y → {x}")

        x -= z
        steps.append(f"x -= z → {x}")

        x *= y
        steps.append(f"x *= y → {x}")

        x %= z
        steps.append(f"x %= z → {x}")

        if z != 0:
            x /= z
            steps.append(f"x /= z → {x}")

        result = x + y + z
        return render(request, "results.html", {"steps": steps, "result": result})
    return render(request, "math_form.html")