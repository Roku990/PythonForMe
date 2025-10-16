from flask import Flask, render_template_string, request

app = Flask(__name__)


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 100px;}
        input, select, button {padding: 10px; margin; 5px; font-size: 16px;}
    </style>
</head>
<body>
    <h1> Flask Calculator </h1>
    <form method="POST">
        <input type="number" name="num1" step="any" required placeholder= "First number">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="num2" step="any" required placeholder="Second number">
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h2>Result: {{result}}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = "Error: divide by zero" if num2 == 0 else num1/num2
        except ValueError:
            result = "invalid input"
    return render_template_string(HTML, result = result)

if __name__ == "__main__":
    app.run(debug=True)