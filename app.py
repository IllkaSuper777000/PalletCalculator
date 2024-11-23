from flask import Flask, render_template, request

# Ініціалізація Flask-додатку
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Головна сторінка з формою введення даних"""
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    """Обробка форми та відображення результатів"""
    try:
        # Отримуємо дані про вантажівку
        truck_length = float(request.form['truck-length'])
        truck_width = float(request.form['truck-width'])

        # Кількість палет
        pallet_count = int(request.form['pallet-count'])

        pallets = []

        # Проходимо по кожній палеті
        for i in range(1, pallet_count + 1):
            pallet_length = float(request.form[f'pallet-{i}-length'])
            pallet_width = float(request.form[f'pallet-{i}-width'])

            pallets.append({
                'length': pallet_length,
                'width': pallet_width
            })

        return render_template('results.html', truck={
            'length': truck_length,
            'width': truck_width,
        }, pallet_count=pallet_count, pallets=pallets)

    except ValueError as e:
        return render_template('results.html', error=str(e))
    except KeyError as e:
        return render_template('results.html', error=f'Missing form data: {str(e)}')
    except Exception as e:
        return render_template('results.html', error=f'An unexpected error occurred: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)