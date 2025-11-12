from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


formulas = [
    ('Кинематика', 'Путь при равномерном движении', ['static/images/f1.jpg']),
    ('Кинематика', 'Средняя скорость', ['static/images/f2.jpg']),
    ('Кинематика', 'Ускорение при равноускоренном движении', ['static/images/f3.jpg']),
    ('Кинематика', 'Зависимость скорости от времени', ['static/images/f4.jpg']),
    ('Кинематика', 'Перемещение при равноускоренном движении', ['static/images/f5(1).jpg', 'static/images/f5(2).jpg', 'static/images/f5(3).jpg']),
    ('Кинематика', 'Максимальная высота при вертикальном броске', ['static/images/f6(1).jpg', 'static/images/f6(2).jpg', 'static/images/f6(3).jpg']),
    ('Кинематика', 'Время подъема', ['static/images/f7.jpg']),
    ('Кинематика', 'Полное время полета', ['static/images/f8.jpg']),
    ('Динамика', 'Второй закон Ньютона', ['static/images/f9.jpg']),
    ('Динамика', 'Третий закон Ньютона', ['static/images/f10.jpg']),
    ('Динамика', 'Сила упругости', ['static/images/f11.jpg']),
    ('Динамика', 'Закон всемирного тяготения', ['static/images/f12.jpg']),
    ('Динамика', 'Первая космическая скорость', ['static/images/f13.jpg']),
    ('Статика', 'Момент силы определяется с помощью следующей формулы', ['static/images/f14.jpg']),
    ('Статика', 'Условие при котором тело не будет вращаться', ['static/images/f15.jpg']),
    ('Гидростатика', 'Определение давления задаётся следующей формулой', ['static/images/f16.jpg']),
    ('Гидростатика', 'Давление, которое создает столб жидкости находится по формуле', ['static/images/f17.jpg']),
    ('Гидростатика', 'Идеальный гидравлический пресс', ['static/images/f18.jpg']),
    ('Гидростатика', 'Любой гидравлический пресс', ['static/images/f19.jpg']),
    ('Гидростатика', 'Сила Архимеда', ['static/images/f20.jpg']),
    ('Импульс', 'Импульс тела', ['static/images/f21.jpg']),
    ('Импульс', 'Изменение импульса тела или системы тел', ['static/images/f22.jpg']),
    ('Импульс', 'Второй закон Ньютона в импульсной форме', ['static/images/f23.jpg']),
    ('Импульс', 'Закон сохранения импульса', ['static/images/f24.jpg']),
    ('Работа, мощность, энергия', 'Работа', ['static/images/f25.jpg']),
    ('Работа, мощность, энергия', 'Мощность', ['static/images/f26.jpg']),
    ('Работа, мощность, энергия', 'Кинетическая энергия', ['static/images/f27.jpg']),
    ('Работа, мощность, энергия', 'Потенциальная энергия', ['static/images/f28.jpg']),
    ('Работа, мощность, энергия', 'Коэффициент полезного действия', ['static/images/f29.jpg']),
    ('Термодинамика', 'Первый закон термодинамики', ['static/images/f30.jpg']),
    ('Термодинамика', 'Количество теплоты', ['static/images/f31.jpg']),
    ('Термодинамика', 'Работа идеального газа', ['static/images/f32.jpg']),
    ('Электростатика', 'Закон Кулона', ['static/images/f33.jpg']),
    ('Электростатика', 'Напряженность электрического поля', ['static/images/f34.jpg']),
    ('Электростатика', 'Электрическое напряжение', ['static/images/f35.jpg']),
    ('Электрический ток', 'Закон Ома', ['static/images/f36.jpg']),
    ('Электрический ток', 'Работа электрического тока', ['static/images/f37.jpg']),
    ('Электрический ток', 'Сила тока', ['static/images/f38.jpg']),
    ('Магнетизм', 'Сила Ампера', ['static/images/f39.jpg']),
    ('Магнетизм', 'ЭДС индукции', ['static/images/f40.jpg']),
    ('Магнетизм', 'Сила Лоренца', ['static/images/f41.jpg']),
    ('Оптика', 'Закон преломления', ['static/images/f42.jpg']),
    ('Оптика', 'Формула тонкой линзы', ['static/images/f43.jpg']),
    ('Оптика', 'Оптическая длина', ['static/images/f44.jpg']),
    ('Атомная и ядерная физика', 'Энергия кванта', ['static/images/f45.jpg']),
    ('Атомная и ядерная физика', 'Закон радиоактивного распада', ['static/images/f46.jpg']),
    ('Атомная и ядерная физика', 'Второй постулат Бора или правило частот', ['static/images/f47.jpg']),
    ('Основы специальной теории относительности', 'Релятивистская масса', ['static/images/f48.jpg']),
    ('Основы специальной теории относительности', 'Полная энергия', ['static/images/f49.jpg']),
    ('Основы специальной теории относительности', 'Энергия покоя тела', ['static/images/f50.jpg']),
]


formula_calculations = {
    # Кинематика
    'Путь при равномерном движении': lambda v, t: {'result': round(v * t, 2)},
    'Средняя скорость': lambda s, t: {'result': round(s / t, 2)},
    'Ускорение при равноускоренном движении': lambda v, v0, t: {'result': round((v - v0) / t, 2)},
    'Зависимость скорости от времени': lambda v0, a, t: {'result': round(v0 + a * t, 2)},
    'Перемещение при равноускоренном движении': lambda v0, a, t: {'result': round(v0 * t + 0.5 * a * t**2, 2)},
    'Максимальная высота при вертикальном броске': lambda v0, g: {'result': round(v0**2 / (2 * g), 2)},
    'Время подъема': lambda v0, g: {'result': round(v0 / g, 2)},
    'Полное время полета': lambda v0, g: {'result': round(2 * v0 / g, 2)},
    
    # Динамика
    'Второй закон Ньютона': lambda m, a: {'result': round(m * a, 2)},
    'Сила упругости': lambda k, x: {'result': round(k * x, 2)},
    'Закон всемирного тяготения': lambda G, m1, m2, r: {'result': round(G * m1 * m2 / r**2, 2)},
    'Первая космическая скорость': lambda g, R: {'result': round((g * R)**0.5, 2)},
    
    # Статика
    'Момент силы определяется с помощью следующей формулы': lambda F, l: {'result': round(F * l, 2)},
    
    # Гидростатика
    'Определение давления задаётся следующей формулой': lambda F, S: {'result': round(F / S, 2)},
    'Давление, которое создает столб жидкости находится по формуле': lambda rho, g, h: {'result': round(rho * g * h, 2)},
    'Сила Архимеда': lambda rho, g, V: {'result': round(rho * g * V, 2)},
    
    # Импульс
    'Импульс тела': lambda m, v: {'result': round(m * v, 2)},
    'Первый закон термодинамики': lambda Q, A: {'result': round(Q - A, 2)},  # ΔU = Q - A
    
    # Электростатика
    'Закон Кулона': lambda k, q1, q2, r: {'result': round(k * abs(q1 * q2) / r**2, 2)},
    'Напряженность электрического поля': lambda F, q: {'result': round(F / q, 2)},
    'Электрическое напряжение': lambda A, q: {'result': round(A / q, 2)},
    
    # Электрический ток
    'Закон Ома': lambda U, R: {'result': round(U / R, 2)},
    'Работа электрического тока': lambda I, U, t: {'result': round(I * U * t, 2)},
    'Сила тока': lambda q, t: {'result': round(q / t, 2)},
    
    # Магнетизм
    'Сила Ампера': lambda B, I, L, alpha: {'result': round(B * I * L * alpha, 2)},
    'ЭДС индукции': lambda delta_phi, delta_t: {'result': round(-delta_phi / delta_t, 2)},
    'Сила Лоренца': lambda q, v, B, alpha: {'result': round(abs(q) * v * B * alpha, 2)},
    
    # Термодинамика
    'Количество теплоты': lambda c, m, delta_t: {'result': round(c * m * delta_t, 2)},
    'Работа идеального газа': lambda P, delta_V: {'result': round(P * delta_V, 2)},
    
    # Работа, мощность, энергия
    'Работа': lambda F, s, cos_alpha: {'result': round(F * s * cos_alpha, 2)},
    'Мощность': lambda A, t: {'result': round(A / t, 2)},
    'Кинетическая энергия': lambda m, v: {'result': round(0.5 * m * v**2, 2)},
    'Потенциальная энергия': lambda m, g, h: {'result': round(m * g * h, 2)},
    'Коэффициент полезного действия': lambda A_pol, A_zat: {'result': round((A_pol / A_zat) * 100, 2)},
    
    # Оптика
    'Закон преломления': lambda sin_a, sin_b, n1, n2: {'result': round(n1 * sin_a / sin_b, 2)},
    'Формула тонкой линзы': lambda d, f: {'result': round(1 / d + 1 / f, 2)},
    'Оптическая длина': lambda n, l: {'result': round(n * l, 2)},
    
    # Атомная физика
    'Энергия кванта': lambda h, nu: {'result': round(h * nu, 2)},
    'Закон радиоактивного распада': lambda N0, half_life, t: {'result': round(N0 * (0.5)**(t / half_life), 2)},
    'Второй постулат Бора или правило частот': lambda E2, E1, h: {'result': round((E2 - E1) / h, 2)},
    
    # Теория относительности
    'Релятивистская масса': lambda m0, v, c: {'result': round(m0 / (1 - (v/c)**2)**0.5, 2)},
    'Полная энергия': lambda m, c: {'result': round(m * c**2, 2)},
    'Энергия покоя тела': lambda m, c: {'result': round(m * c**2, 2)},
}

@app.route('/')
def home():
    return render_template('formulas.html', formulas=formulas)

@app.route('/api/calculate/<formula_name>', methods=['POST'])
def calculate(formula_name):
    try:
        data = request.get_json()
        calculation_func = formula_calculations[formula_name]
        result = calculation_func(**data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)